from __future__ import annotations

from typing import Iterable

from .models import EvidenceItem


QUALITY_SCORES = {
    "low": 0.40,
    "medium": 0.70,
    "high": 0.90,
    "authoritative": 1.00,
}

TYPE_WEIGHTS = {
    "self_attestation": 0.60,
    "policy": 0.70,
    "design": 0.75,
    "architecture": 0.85,
    "configuration": 0.90,
    "test_results": 0.95,
    "approval_record": 0.90,
    "monitoring_record": 0.95,
    "audit_record": 1.00,
    "external_assurance": 1.00,
}


def parse_evidence(raw: dict | str) -> EvidenceItem:
    if isinstance(raw, str):
        return EvidenceItem(
            evidence_id=raw,
            evidence_type="self_attestation",
            reference=raw,
            quality="low",
            verified=False,
        )

    return EvidenceItem(
        evidence_id=str(raw.get("evidence_id", raw.get("reference", "evidence"))),
        evidence_type=str(raw.get("evidence_type", "self_attestation")),
        reference=str(raw.get("reference", raw.get("evidence_id", ""))),
        quality=str(raw.get("quality", "medium")).lower(),
        verified=bool(raw.get("verified", False)),
        freshness_days=raw.get("freshness_days"),
        description=str(raw.get("description", "")),
    )


def score_evidence_item(item: EvidenceItem) -> float:
    quality = QUALITY_SCORES.get(item.quality, 0.50)
    type_weight = TYPE_WEIGHTS.get(item.evidence_type, 0.70)
    verified_factor = 1.0 if item.verified else 0.85

    freshness_factor = 1.0
    if item.freshness_days is not None:
        if item.freshness_days > 730:
            freshness_factor = 0.70
        elif item.freshness_days > 365:
            freshness_factor = 0.85

    return round(quality * type_weight * verified_factor * freshness_factor, 3)


def aggregate_evidence_quality(items: Iterable[EvidenceItem]) -> float:
    scores = sorted((score_evidence_item(i) for i in items), reverse=True)
    if not scores:
        return 0.0

    # Strongest evidence carries most weight, while corroborating evidence adds confidence.
    weights = [1.0, 0.5, 0.25]
    weighted = sum(score * weights[i] for i, score in enumerate(scores[:3]))
    maximum = sum(weights[: min(3, len(scores))])
    return round(weighted / maximum, 3)
