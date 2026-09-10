import csv
from pathlib import Path
from typing import Iterable, List
from datetime import date

from .models import AIUseCase, Control, ControlResult
from .evidence import parse_evidence, aggregate_evidence_quality
from .exceptions import exception_map


STATUS_SCORES = {
    "implemented": 1.0,
    "partial": 0.5,
    "planned": 0.2,
    "not_implemented": 0.0,
    "not_applicable": 1.0,
}


def load_controls(path: str | Path) -> List[Control]:
    controls = []
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            controls.append(
                Control(
                    control_id=row["control_id"],
                    domain=row["domain"],
                    title=row["title"],
                    description=row["description"],
                    minimum_risk=int(row["minimum_risk"]),
                    critical=row["critical"].strip().lower() == "true",
                )
            )
    return controls


def applicable_controls(controls: Iterable[Control], risk_band: str) -> List[Control]:
    rank = {"low": 1, "medium": 2, "high": 3, "critical": 4}
    current = rank[risk_band]
    return [c for c in controls if current >= c.minimum_risk]


def evaluate_controls(
    use_case: AIUseCase,
    controls: Iterable[Control],
    as_of: date | None = None,
) -> List[ControlResult]:
    results = []
    exceptions = exception_map(use_case.exceptions, as_of=as_of)

    for control in controls:
        status = use_case.control_status.get(control.control_id, "not_implemented")
        if status not in STATUS_SCORES:
            raise ValueError(f"Unknown control status for {control.control_id}: {status}")

        raw_evidence = use_case.evidence.get(control.control_id, [])
        evidence_items = [parse_evidence(item) for item in raw_evidence]
        evidence_quality = aggregate_evidence_quality(evidence_items)
        base = STATUS_SCORES[status]

        # Evidence quality becomes part of assurance rather than a binary attachment check.
        if status == "implemented":
            score = base * (0.55 + 0.45 * evidence_quality)
        elif status == "partial":
            score = base * (0.70 + 0.30 * evidence_quality)
        else:
            score = base

        ex_record = None
        ex_valid = False
        if control.control_id in exceptions:
            ex_record, ex_valid = exceptions[control.control_id]

        # A valid, formally approved exception gives limited credit only.
        # It never converts a missing control into an implemented control.
        if status in {"planned", "not_implemented"} and ex_valid:
            score = max(score, 0.25)

        results.append(
            ControlResult(
                control_id=control.control_id,
                title=control.title,
                domain=control.domain,
                status=status,
                evidence_count=len(evidence_items),
                evidence_quality=evidence_quality,
                score=round(score, 3),
                critical=control.critical,
                owner=use_case.control_owners.get(control.control_id, ""),
                due_date=use_case.control_due_dates.get(control.control_id, ""),
                exception_id=ex_record.exception_id if ex_record else "",
                exception_valid=ex_valid,
            )
        )
    return results


def calculate_coverage(results: Iterable[ControlResult]) -> float:
    results = list(results)
    if not results:
        return 100.0
    return round(sum(r.score for r in results) / len(results) * 100, 1)


def calculate_evidence_assurance(results: Iterable[ControlResult]) -> float:
    relevant = [
        r for r in results
        if r.status in {"implemented", "partial"} and r.status != "not_applicable"
    ]
    if not relevant:
        return 0.0
    return round(sum(r.evidence_quality for r in relevant) / len(relevant) * 100, 1)
