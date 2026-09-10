# Assurance model

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

This is intentionally simple. In a production governance system, applicability would also depend on characteristics such as personal data, external users, agentic capabilities, safety relevance, jurisdiction and procurement model.

## 3. Control effectiveness

Each control status has a nominal value:

| Status | Credit |
|---|---:|
| implemented | 1.0 |
| partial | 0.5 |
| planned | 0.2 |
| not implemented | 0.0 |
| not applicable | 1.0 |

Implemented and partial controls without evidence are discounted.

## 4. Residual risk

Control coverage reduces inherent risk, but the model caps the reduction so residual risk cannot be reduced to zero simply by checking boxes.

## 5. Decision

The engine considers:

- residual risk,
- overall control coverage,
- unresolved critical controls,
- evidence gaps.

Possible outcomes are APPROVE, CONDITIONAL_APPROVAL, REVIEW_REQUIRED and BLOCK.

## Important

The model is intentionally explainable rather than mathematically sophisticated. Its value is in traceability and experimentation, not in claiming that AI risk can be represented by a single objective number.
