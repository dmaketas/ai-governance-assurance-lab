from __future__ import annotations

from datetime import date

from .models import AIUseCase, ControlResult, PolicyGateResult


def _expired_due_date(due_date: str, as_of: date) -> bool:
    if not due_date:
        return False
    try:
        return date.fromisoformat(due_date) < as_of
    except ValueError:
        return True


def evaluate_policy_gates(
    use_case: AIUseCase,
    risk_band: str,
    results: list[ControlResult],
    evidence_assurance: float,
    as_of: date | None = None,
) -> list[PolicyGateResult]:
    as_of = as_of or date.today()
    gates: list[PolicyGateResult] = []

    unresolved_critical = [
        r for r in results
        if r.critical
        and r.status in {"not_implemented", "planned"}
        and not r.exception_valid
    ]
    gates.append(PolicyGateResult(
        gate_id="POL-001",
        name="No unexcepted critical control gaps",
        passed=not unresolved_critical,
        severity="blocking",
        message=(
            "No unresolved critical control gaps."
            if not unresolved_critical
            else "Critical gaps without valid exceptions: " +
                 ", ".join(r.control_id for r in unresolved_critical)
        ),
    ))

    expired_exceptions = [
        r for r in results if r.exception_id and not r.exception_valid
    ]
    gates.append(PolicyGateResult(
        gate_id="POL-002",
        name="No invalid or expired exceptions",
        passed=not expired_exceptions,
        severity="blocking",
        message=(
            "All referenced exceptions are valid."
            if not expired_exceptions
            else "Invalid/expired exceptions: " +
                 ", ".join(r.exception_id for r in expired_exceptions)
        ),
    ))

    missing_owners = [
        r for r in results
        if r.status in {"partial", "planned", "not_implemented"} and not r.owner.strip()
    ]
    gates.append(PolicyGateResult(
        gate_id="POL-003",
        name="Unresolved controls have accountable owners",
        passed=not missing_owners,
        severity="review",
        message=(
            "All unresolved controls have accountable owners."
            if not missing_owners
            else "Controls without owners: " +
                 ", ".join(r.control_id for r in missing_owners)
        ),
    ))

    overdue_actions = [
        r for r in results
        if r.status in {"partial", "planned", "not_implemented"}
        and _expired_due_date(r.due_date, as_of)
    ]
    gates.append(PolicyGateResult(
        gate_id="POL-004",
        name="No overdue remediation actions",
        passed=not overdue_actions,
        severity="review",
        message=(
            "No overdue remediation actions."
            if not overdue_actions
            else "Overdue controls: " +
                 ", ".join(r.control_id for r in overdue_actions)
        ),
    ))

    minimum_evidence = 55.0 if risk_band in {"high", "critical"} else 40.0
    evidence_ok = evidence_assurance >= minimum_evidence
    gates.append(PolicyGateResult(
        gate_id="POL-005",
        name="Minimum evidence assurance",
        passed=evidence_ok,
        severity="review",
        message=(
            f"Evidence assurance {evidence_assurance}% meets the {minimum_evidence}% threshold."
            if evidence_ok
            else f"Evidence assurance {evidence_assurance}% is below the {minimum_evidence}% threshold."
        ),
    ))

    return gates
