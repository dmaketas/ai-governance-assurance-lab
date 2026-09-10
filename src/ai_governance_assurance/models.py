from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class EvidenceItem:
    evidence_id: str
    evidence_type: str
    reference: str
    quality: str = "medium"
    verified: bool = False
    freshness_days: Optional[int] = None
    description: str = ""


@dataclass
class ExceptionRecord:
    exception_id: str
    control_id: str
    rationale: str
    approver: str
    expiry_date: str
    compensating_controls: List[str] = field(default_factory=list)


@dataclass
class AIUseCase:
    name: str
    description: str
    owner: str
    factors: Dict[str, int]
    control_status: Dict[str, str] = field(default_factory=dict)
    evidence: Dict[str, List[dict]] = field(default_factory=dict)
    control_owners: Dict[str, str] = field(default_factory=dict)
    control_due_dates: Dict[str, str] = field(default_factory=dict)
    exceptions: List[dict] = field(default_factory=list)


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
    evidence_quality: float
    score: float
    critical: bool
    owner: str = ""
    due_date: str = ""
    exception_id: str = ""
    exception_valid: bool = False


@dataclass
class PolicyGateResult:
    gate_id: str
    name: str
    passed: bool
    severity: str
    message: str


@dataclass
class AssuranceResult:
    inherent_risk: float
    risk_band: str
    control_coverage: float
    evidence_assurance: float
    residual_risk: float
    decision: str
    control_results: List[ControlResult]
    policy_gates: List[PolicyGateResult]
    reasons: List[str]
