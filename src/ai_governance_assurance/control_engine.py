import csv
from pathlib import Path
from typing import Iterable, List

from .models import AIUseCase, Control, ControlResult


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


def evaluate_controls(use_case: AIUseCase, controls: Iterable[Control]) -> List[ControlResult]:
    results = []
    for control in controls:
        status = use_case.control_status.get(control.control_id, "not_implemented")
        if status not in STATUS_SCORES:
            raise ValueError(f"Unknown control status for {control.control_id}: {status}")

        evidence_count = len(use_case.evidence.get(control.control_id, []))
        base = STATUS_SCORES[status]

        # Evidence matters: implemented/partial controls without evidence
        # receive only 70% of their nominal assurance credit.
        if status in {"implemented", "partial"} and evidence_count == 0:
            score = base * 0.70
        else:
            score = base

        results.append(
            ControlResult(
                control_id=control.control_id,
                title=control.title,
                domain=control.domain,
                status=status,
                evidence_count=evidence_count,
                score=round(score, 2),
                critical=control.critical,
            )
        )
    return results


def calculate_coverage(results: Iterable[ControlResult]) -> float:
    results = list(results)
    if not results:
        return 100.0
    return round(sum(r.score for r in results) / len(results) * 100, 1)
