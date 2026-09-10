# Assurance model — v0.2

The lab uses a deliberately transparent assurance model.

## 1. Inherent risk

Eight factors are scored from 1 to 5:

- business criticality,
- data sensitivity,
- autonomy,
- external exposure,
- model dependency,
- human impact,
- regulatory impact,
- security impact.

Weighted values are normalized to a 0–100 score.

## 2. Applicable controls

Each control specifies the minimum risk band at which it becomes applicable.

## 3. Evidence-aware control effectiveness

Implementation status establishes a nominal control score. Evidence quality then changes the amount of assurance credit received.

An "implemented" control with weak or absent evidence therefore receives materially less credit than a well-evidenced control.

## 4. Evidence assurance

The engine separately reports aggregate evidence assurance so that a high implementation score cannot hide poor substantiation.

## 5. Ownership and due dates

Unresolved controls can be assigned an accountable owner and remediation due date. Missing ownership and overdue actions are evaluated through policy gates.

## 6. Exceptions

Temporary exceptions must have a rationale, approver and non-expired date. Exceptions give limited credit only and remain visible in the report.

## 7. Policy-as-code gates

Deterministic policy gates can override or constrain a numerical score. Critical unexcepted gaps and invalid/expired exceptions are blocking conditions for high-risk systems.

## 8. Residual risk and decision

Control coverage reduces inherent risk, subject to a cap. The final decision considers residual risk, evidence assurance and policy-gate outcomes.

Possible outcomes are:

- `APPROVE`
- `CONDITIONAL_APPROVAL`
- `REVIEW_REQUIRED`
- `BLOCK`

The model is intentionally explainable rather than mathematically sophisticated. Its value is in traceability and experimentation, not in claiming that AI risk can be reduced to a single objective number.
