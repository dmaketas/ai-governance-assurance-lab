from datetime import date
from ai_governance_assurance.models import AIUseCase, Control
from ai_governance_assurance.control_engine import evaluate_controls, calculate_coverage


def test_missing_evidence_reduces_implemented_control_score():
    use_case = AIUseCase(
        name="test", description="test", owner="test", factors={},
        control_status={"SEC-01": "implemented"}, evidence={}
    )
    controls = [Control("SEC-01", "Security", "Identity", "desc", 1, True)]
    results = evaluate_controls(use_case, controls, as_of=date(2026,9,10))
    assert results[0].score < 1.0
    assert results[0].evidence_quality == 0.0


def test_strong_evidenced_control_scores_high():
    use_case = AIUseCase(
        name="test", description="test", owner="test", factors={},
        control_status={"SEC-01": "implemented"},
        evidence={"SEC-01": [{
            "evidence_id":"E1","evidence_type":"audit_record","reference":"audit",
            "quality":"authoritative","verified":True,"freshness_days":20
        }]}
    )
    controls = [Control("SEC-01", "Security", "Identity", "desc", 1, True)]
    results = evaluate_controls(use_case, controls, as_of=date(2026,9,10))
    assert results[0].score >= 0.95
    assert calculate_coverage(results) >= 95
