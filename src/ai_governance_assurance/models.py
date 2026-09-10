from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class AIUseCase:
    name: str
    description: str
    owner: str
    factors: Dict[str, int]
    control_status: Dict[str, str] = field(default_factory=dict)
    evidence: Dict[str, List[str]] = field(default_factory=dict)


@dataclass
class Control:
    control_id: str
    domain: str
    title: str
    description: str
    minimum_risk: int = 1
    critical: bool = False


@dataclass
class ControlResult:
    control_id: str
    title: str
    domain: str
    status: str
    evidence_count: int
    score: float
    critical: bool


@dataclass
class AssuranceResult:
    inherent_risk: float
    risk_band: str
    control_coverage: float
    residual_risk: float
    decision: str
    control_results: List[ControlResult]
    reasons: List[str]
