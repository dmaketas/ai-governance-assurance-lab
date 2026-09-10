from pathlib import Path
from typing import List

from .models import AIUseCase, AssuranceResult
from .risk_engine import calculate_inherent_risk
from .control_engine import applicable_controls, evaluate_controls, calculate_coverage, load_controls


def _decision(inherent_risk: float, residual_risk: float, coverage: float, critical_gaps: int) -> tuple[str, List[str]]:
    reasons: List[str] = []

    if critical_gaps > 0 and inherent_risk >= 55:
        reasons.append(f"{critical_gaps} critical control(s) are not implemented.")
        return "BLOCK", reasons

    if residual_risk >= 60:
        reasons.append("Residual risk remains high after current controls.")
        return "REVIEW_REQUIRED", reasons

    if coverage < 70:
        reasons.append("Control coverage is below the 70% assurance threshold.")
        return "REVIEW_REQUIRED", reasons

    if residual_risk >= 35 or coverage < 85:
        reasons.append("Material residual risk or incomplete control coverage remains.")
        return "CONDITIONAL_APPROVAL", reasons

    reasons.append("Residual risk and control coverage are within the lab's approval thresholds.")
    return "APPROVE", reasons


def assess(use_case: AIUseCase, controls_path: str | Path) -> AssuranceResult:
    inherent_risk, risk_band = calculate_inherent_risk(use_case.factors)
    controls = load_controls(controls_path)
    applicable = applicable_controls(controls, risk_band)
    control_results = evaluate_controls(use_case, applicable)
    coverage = calculate_coverage(control_results)

    # Simple transparent residual-risk model for educational use:
    # effective controls can reduce but never erase inherent risk.
    reduction = min(coverage * 0.75, 75)
    residual = round(inherent_risk * (1 - reduction / 100), 1)

    critical_gaps = sum(
        1 for r in control_results
        if r.critical and r.status in {"not_implemented", "planned"}
    )

    decision, reasons = _decision(inherent_risk, residual, coverage, critical_gaps)

    if critical_gaps:
        reasons.append(f"Critical unresolved controls: {critical_gaps}.")
    if any(r.status == "partial" for r in control_results):
        reasons.append("One or more controls are only partially implemented.")
    if any(r.status == "implemented" and r.evidence_count == 0 for r in control_results):
        reasons.append("Some implemented controls have no evidence attached.")

    return AssuranceResult(
        inherent_risk=inherent_risk,
        risk_band=risk_band,
        control_coverage=coverage,
        residual_risk=residual,
        decision=decision,
        control_results=control_results,
        reasons=reasons,
    )
