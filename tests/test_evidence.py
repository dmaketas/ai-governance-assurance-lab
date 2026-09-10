from ai_governance_assurance.evidence import parse_evidence, score_evidence_item, aggregate_evidence_quality


def test_verified_authoritative_evidence_scores_higher():
    strong = parse_evidence({
        "evidence_id":"E1", "evidence_type":"audit_record", "reference":"audit",
        "quality":"authoritative", "verified":True, "freshness_days":30
    })
    weak = parse_evidence({
        "evidence_id":"E2", "evidence_type":"self_attestation", "reference":"statement",
        "quality":"low", "verified":False, "freshness_days":30
    })
    assert score_evidence_item(strong) > score_evidence_item(weak)


def test_aggregate_evidence_quality_is_bounded():
    items = [
        parse_evidence({"evidence_id":"E1","evidence_type":"test_results","reference":"t","quality":"high","verified":True}),
        parse_evidence({"evidence_id":"E2","evidence_type":"architecture","reference":"a","quality":"medium","verified":False}),
    ]
    score = aggregate_evidence_quality(items)
    assert 0 < score <= 1
