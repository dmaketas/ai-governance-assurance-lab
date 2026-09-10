from __future__ import annotations

from datetime import date

from .models import ExceptionRecord


def parse_exception(raw: dict) -> ExceptionRecord:
    return ExceptionRecord(
        exception_id=str(raw["exception_id"]),
        control_id=str(raw["control_id"]),
        rationale=str(raw.get("rationale", "")),
        approver=str(raw.get("approver", "")),
        expiry_date=str(raw["expiry_date"]),
        compensating_controls=list(raw.get("compensating_controls", [])),
    )


def exception_is_valid(record: ExceptionRecord, as_of: date | None = None) -> bool:
    as_of = as_of or date.today()
    try:
        expiry = date.fromisoformat(record.expiry_date)
    except ValueError:
        return False

    return bool(record.approver.strip()) and bool(record.rationale.strip()) and expiry >= as_of


def exception_map(raw_exceptions: list[dict], as_of: date | None = None):
    result = {}
    for raw in raw_exceptions:
        record = parse_exception(raw)
        result[record.control_id] = (record, exception_is_valid(record, as_of))
    return result
