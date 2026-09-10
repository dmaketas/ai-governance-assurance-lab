from pathlib import Path
from ai_governance_assurance.models import AIUseCase
from ai_governance_assurance.assurance import assess

CONTROLS = Path(__file__).parents[1] / "data" / "controls.csv"


def test_critical_case_with_control_gaps_blocks():
    use_case = AIUseCase(
        name="Autonomous agent",
        description="test",
        owner="test",
        factors={
            "business_criticality": 5,
            "data_sensitivity": 5,
            "autonomy": 5,
            "external_exposure": 5,
            "model_dependency": 5,
            "human_impact": 5,
            "regulatory_impact": 5,
            "security_impact": 5,
        },
        control_status={},
        evidence={},
    )
    result = assess(use_case, CONTROLS)
    assert result.risk_band == "critical"
    assert result.decision == "BLOCK"


def test_result_has_traceable_controls():
    use_case = AIUseCase(
        name="Internal assistant",
        description="test",
        owner="test",
        factors={
            "business_criticality": 2,
            "data_sensitivity": 2,
            "autonomy": 1,
            "external_exposure": 1,
            "model_dependency": 2,
            "human_impact": 2,
            "regulatory_impact": 2,
            "security_impact": 2,
        },
        control_status={
            "GOV-01": "implemented",
            "GOV-02": "implemented",
            "DATA-01": "implemented",
            "SEC-01": "implemented",
            "EVAL-02": "implemented",
        },
        evidence={
            "GOV-01": ["e1"],
            "GOV-02": ["e2"],
            "DATA-01": ["e3"],
            "SEC-01": ["e4"],
            "EVAL-02": ["e5"],
        },
    )
    result = assess(use_case, CONTROLS)
    assert result.control_results
    assert result.control_coverage > 0
