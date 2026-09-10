from pathlib import Path
from typing import List
from datetime import date

from .models import AIUseCase, AssuranceResult
from .risk_engine import calculate_inherent_risk
from .control_engine import (
    applicable_controls,
    evaluate_controls,
    calculate_coverage,
    calculate_evidence_assurance,
    load_controls,
)
from .policy import evaluate_policy_gates


def _decision(
    inherent_risk: float,
    residual_risk: float,
    coverage: float,
    policy_gates,
) -> tuple[str, List[str]]:
    reasons: List[str] = []
    blocking_failures = [g for g in policy_gates if g.severity == "blocking" and not g.passed]
    review_failures = [g for g in policy_gates if g.severity == "review" and not g.passed]

    if blocking_failures and inherent_risk >= 55:
        reasons.append("One or more blocking policy-as-code gates failed.")
        return "BLOCK", reasons

    if residual_risk >= 60:
        reasons.append("Residual risk remains high after current controls.")
        return "REVIEW_REQUIRED", reasons

    if coverage < 70 or len(review_failures) >= 2:
        reasons.append("Assurance coverage or policy-gate performance requires formal review.")
        return "REVIEW_REQUIRED", reasons

    if residual_risk >= 35 or coverage < 85 or review_failures:
        reasons.append("Material residual risk, incomplete control coverage, or review-level policy failures remain.")
        return "CONDITIONAL_APPROVAL", reasons

    reasons.append("Residual risk, evidence and policy gates are within the lab's approval thresholds.")
    return "APPROVE", reasons


def assess(
    use_case: AIUseCase,
    controls_path: str | Path,
    as_of: date | None = None,
) -> AssuranceResult:
    inherent_risk, risk_band = calculate_inherent_risk(use_case.factors)
    controls = load_controls(controls_path)
    applicable = applicable_controls(controls, risk_band)
    control_results = evaluate_controls(use_case, applicable, as_of=as_of)
    coverage = calculate_coverage(control_results)
    evidence_assurance = calculate_evidence_assurance(control_results)

    # Transparent educational residual-risk model:
    # evidence-aware control coverage can reduce, but never erase, inherent risk.
    reduction = min(coverage * 0.75, 75)
    residual = round(inherent_risk * (1 - reduction / 100), 1)

    gates = evaluate_policy_gates(
        use_case,
        risk_band,
        control_results,
        evidence_assurance,
        as_of=as_of,
    )
    decision, reasons = _decision(inherent_risk, residual, coverage, gates)

    failed = [g for g in gates if not g.passed]
    if failed:
        reasons.append("Failed policy gates: " + ", ".join(g.gate_id for g in failed) + ".")

    if any(r.status == "partial" for r in control_results):
        reasons.append("One or more controls are only partially implemented.")

    weak_evidence = [
        r for r in control_results
        if r.status in {"implemented", "partial"} and r.evidence_quality < 0.50
    ]
    if weak_evidence:
        reasons.append("Some implemented/partial controls have weak or missing evidence.")

    return AssuranceResult(
        inherent_risk=inherent_risk,
        risk_band=risk_band,
        control_coverage=coverage,
        evidence_assurance=evidence_assurance,
        residual_risk=residual,
        decision=decision,
        control_results=control_results,
        policy_gates=gates,
        reasons=reasons,
    )
