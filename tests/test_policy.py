from datetime import date
from ai_governance_assurance.models import AIUseCase, ControlResult
from ai_governance_assurance.policy import evaluate_policy_gates


def test_unexcepted_critical_gap_fails_blocking_gate():
    uc = AIUseCase(name="x", description="x", owner="x", factors={})
    results = [
        ControlResult(
            control_id="SEC-01", title="Security", domain="Security",
            status="not_implemented", evidence_count=0, evidence_quality=0,
            score=0, critical=True
        )
    ]
    gates = evaluate_policy_gates(uc, "high", results, 70, as_of=date(2026,9,10))
    gate = next(g for g in gates if g.gate_id == "POL-001")
    assert not gate.passed
    assert gate.severity == "blocking"


def test_unresolved_control_requires_owner():
    uc = AIUseCase(name="x", description="x", owner="x", factors={})
    results = [
        ControlResult(
            control_id="MOD-01", title="Supplier", domain="Model",
            status="partial", evidence_count=1, evidence_quality=.7,
            score=.45, critical=False, owner=""
        )
    ]
    gates = evaluate_policy_gates(uc, "high", results, 70, as_of=date(2026,9,10))
    gate = next(g for g in gates if g.gate_id == "POL-003")
    assert not gate.passed
