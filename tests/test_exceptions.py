from datetime import date
from ai_governance_assurance.exceptions import parse_exception, exception_is_valid


def test_valid_exception():
    ex = parse_exception({
        "exception_id":"EX-1", "control_id":"SEC-01", "rationale":"Temporary",
        "approver":"Risk Owner", "expiry_date":"2026-12-31"
    })
    assert exception_is_valid(ex, date(2026, 9, 10))


def test_expired_exception():
    ex = parse_exception({
        "exception_id":"EX-2", "control_id":"SEC-01", "rationale":"Temporary",
        "approver":"Risk Owner", "expiry_date":"2026-01-01"
    })
    assert not exception_is_valid(ex, date(2026, 9, 10))
