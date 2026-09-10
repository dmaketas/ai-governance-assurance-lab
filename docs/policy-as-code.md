# Policy-as-code gates

Version 0.2 adds deterministic gates that sit above the numerical risk score.

A deployment decision can therefore be blocked even when aggregate coverage appears acceptable.

Current gates:

| Gate | Purpose | Severity |
|---|---|---|
| POL-001 | No unexcepted critical control gaps | blocking |
| POL-002 | No invalid or expired exceptions | blocking |
| POL-003 | Unresolved controls have accountable owners | review |
| POL-004 | No overdue remediation actions | review |
| POL-005 | Minimum evidence assurance | review |

This prevents the governance model from becoming a simple weighted average in which a strong score in one area can hide a critical weakness elsewhere.

The gate implementation is intentionally readable Python so reviewers can inspect and challenge the decision logic.
