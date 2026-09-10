from ai_governance_assurance.models import AIUseCase, Control
from ai_governance_assurance.control_engine import evaluate_controls, calculate_coverage


def test_evidence_discount():
    use_case = AIUseCase(
        name="test",
        description="test",
        owner="test",
        factors={},
        control_status={"SEC-01": "implemented"},
        evidence={},
    )
    controls = [Control("SEC-01", "Security", "Identity", "desc", 1, True)]
    results = evaluate_controls(use_case, controls)
    assert results[0].score == 0.70


def test_evidenced_control_gets_full_credit():
    use_case = AIUseCase(
        name="test",
        description="test",
        owner="test",
        factors={},
        control_status={"SEC-01": "implemented"},
        evidence={"SEC-01": ["evidence-1"]},
    )
    controls = [Control("SEC-01", "Security", "Identity", "desc", 1, True)]
    results = evaluate_controls(use_case, controls)
    assert calculate_coverage(results) == 100.0
