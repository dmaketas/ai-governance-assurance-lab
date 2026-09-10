from typing import Dict, Tuple

FACTOR_WEIGHTS = {
    "business_criticality": 1.2,
    "data_sensitivity": 1.4,
    "autonomy": 1.4,
    "external_exposure": 1.2,
    "model_dependency": 1.0,
    "human_impact": 1.5,
    "regulatory_impact": 1.3,
    "security_impact": 1.5,
}


def validate_factors(factors: Dict[str, int]) -> None:
    missing = set(FACTOR_WEIGHTS) - set(factors)
    if missing:
        raise ValueError(f"Missing risk factors: {', '.join(sorted(missing))}")
    invalid = {k: v for k, v in factors.items() if k in FACTOR_WEIGHTS and not 1 <= int(v) <= 5}
    if invalid:
        raise ValueError("Risk factor values must be between 1 and 5.")


def calculate_inherent_risk(factors: Dict[str, int]) -> Tuple[float, str]:
    validate_factors(factors)
    weighted = sum(int(factors[k]) * w for k, w in FACTOR_WEIGHTS.items())
    max_weighted = sum(5 * w for w in FACTOR_WEIGHTS.values())
    score = round((weighted / max_weighted) * 100, 1)

    if score >= 75:
        band = "critical"
    elif score >= 55:
        band = "high"
    elif score >= 35:
        band = "medium"
    else:
        band = "low"
    return score, band
