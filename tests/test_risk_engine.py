import pytest
from ai_governance_assurance.risk_engine import calculate_inherent_risk


def test_high_risk_case():
    factors = {
        "business_criticality": 5,
        "data_sensitivity": 5,
        "autonomy": 5,
        "external_exposure": 4,
        "model_dependency": 5,
        "human_impact": 4,
        "regulatory_impact": 5,
        "security_impact": 5,
    }
    score, band = calculate_inherent_risk(factors)
    assert score >= 75
    assert band == "critical"


def test_missing_factor_rejected():
    with pytest.raises(ValueError):
        calculate_inherent_risk({"business_criticality": 3})
