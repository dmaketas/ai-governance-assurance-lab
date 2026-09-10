# AI Assurance Report — High-Autonomy Service Agent

**Owner:** Digital Innovation

**Decision:** `BLOCK`

## Risk and assurance summary

- Inherent risk: **89.7/100 (critical)**
- Control coverage: **39.2%**
- Evidence assurance: **27.9%**
- Residual risk: **63.3/100**

## Policy-as-code gates

| Gate | Severity | Result | Message |
|---|---|---:|---|
| POL-001 — No unexcepted critical control gaps | blocking | FAIL | Critical gaps without valid exceptions: GOV-03, EVAL-01, IR-01, RES-01 |
| POL-002 — No invalid or expired exceptions | blocking | FAIL | Invalid/expired exceptions: EX-GOV-OLD |
| POL-003 — Unresolved controls have accountable owners | review | FAIL | Controls without owners: GOV-02, DATA-02, RAG-01, MOD-01, MOD-02, EVAL-02, HUM-01, PRV-01, CHG-01 |
| POL-004 — No overdue remediation actions | review | PASS | No overdue remediation actions. |
| POL-005 — Minimum evidence assurance | review | FAIL | Evidence assurance 27.9% is below the 55.0% threshold. |

## Decision rationale

- One or more blocking policy-as-code gates failed.
- Failed policy gates: POL-001, POL-002, POL-003, POL-005.
- One or more controls are only partially implemented.
- Some implemented/partial controls have weak or missing evidence.

## Control results

| Control | Domain | Status | Owner | Due | Evidence | Evidence quality | Score | Exception | Critical |
|---|---|---:|---|---|---:|---:|---:|---|---:|
| GOV-01 — Named accountable owner | Governance | implemented | — | — | 1 | 0.810 | 0.915 | — | Yes |
| GOV-02 — Documented intended use and prohibited use | Governance | partial | — | — | 0 | 0.000 | 0.350 | — | No |
| GOV-03 — Risk acceptance authority | Governance | planned | AI Governance Board | 2026-09-25 | 0 | 0.000 | 0.200 | EX-GOV-OLD (invalid/expired) | Yes |
| DATA-01 — Data classification and handling | Data | implemented | — | — | 1 | 0.675 | 0.854 | — | Yes |
| DATA-02 — Training and retrieval data provenance | Data | partial | — | — | 0 | 0.000 | 0.350 | — | No |
| SEC-01 — Strong identity and authorization | Security | implemented | — | — | 1 | 0.810 | 0.915 | — | Yes |
| SEC-02 — Prompt and input security | Security | partial | AppSec Lead | 2026-09-30 | 1 | 0.565 | 0.435 | — | Yes |
| RAG-01 — Retrieved-content trust controls | RAG Security | partial | — | — | 0 | 0.000 | 0.350 | — | Yes |
| AGT-01 — Tool-use authorization | Agent Security | partial | Enterprise Architecture | 2026-09-28 | 1 | 0.506 | 0.426 | — | Yes |
| AGT-02 — Human approval for high-impact actions | Agent Security | planned | Product Owner | 2026-09-20 | 0 | 0.000 | 0.250 | EX-AGT-001 (valid) | Yes |
| MOD-01 — Model and supplier due diligence | Model Risk | partial | — | — | 0 | 0.000 | 0.350 | — | No |
| MOD-02 — Model change and version control | Model Risk | planned | — | — | 0 | 0.000 | 0.200 | — | No |
| EVAL-01 — Security and misuse testing | Evaluation | planned | AI Security Lead | 2026-10-10 | 0 | 0.000 | 0.200 | — | Yes |
| EVAL-02 — Quality and performance evaluation | Evaluation | partial | — | — | 0 | 0.000 | 0.350 | — | No |
| MON-01 — Security logging and traceability | Monitoring | partial | Security Operations | 2026-10-05 | 1 | 0.535 | 0.430 | — | Yes |
| MON-02 — Operational monitoring | Monitoring | partial | AI Platform Team | 2026-10-05 | 0 | 0.000 | 0.350 | — | No |
| HUM-01 — Human oversight design | Human Oversight | planned | — | — | 0 | 0.000 | 0.200 | — | No |
| PRV-01 — Privacy and personal-data controls | Privacy | partial | — | — | 0 | 0.000 | 0.350 | — | No |
| IR-01 — AI incident response | Incident Response | planned | Incident Response Lead | 2026-10-15 | 0 | 0.000 | 0.200 | — | Yes |
| RES-01 — Fallback and safe failure | Resilience | planned | Service Owner | 2026-10-20 | 0 | 0.000 | 0.200 | — | Yes |
| CHG-01 — Controlled AI change process | Change Management | partial | — | — | 0 | 0.000 | 0.350 | — | No |

## Unresolved items

- **GOV-02** Documented intended use and prohibited use: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **GOV-03** Risk acceptance authority: planned; owner: AI Governance Board; due: 2026-09-25.
- **DATA-02** Training and retrieval data provenance: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **SEC-02** Prompt and input security: partial; owner: AppSec Lead; due: 2026-09-30.
- **RAG-01** Retrieved-content trust controls: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **AGT-01** Tool-use authorization: partial; owner: Enterprise Architecture; due: 2026-09-28.
- **AGT-02** Human approval for high-impact actions: planned; owner: Product Owner; due: 2026-09-20.
- **MOD-01** Model and supplier due diligence: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **MOD-02** Model change and version control: planned; owner: UNASSIGNED; due: NO DUE DATE.
- **EVAL-01** Security and misuse testing: planned; owner: AI Security Lead; due: 2026-10-10.
- **EVAL-02** Quality and performance evaluation: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **MON-01** Security logging and traceability: partial; owner: Security Operations; due: 2026-10-05.
- **MON-02** Operational monitoring: partial; owner: AI Platform Team; due: 2026-10-05.
- **HUM-01** Human oversight design: planned; owner: UNASSIGNED; due: NO DUE DATE.
- **PRV-01** Privacy and personal-data controls: partial; owner: UNASSIGNED; due: NO DUE DATE.
- **IR-01** AI incident response: planned; owner: Incident Response Lead; due: 2026-10-15.
- **RES-01** Fallback and safe failure: planned; owner: Service Owner; due: 2026-10-20.
- **CHG-01** Controlled AI change process: partial; owner: UNASSIGNED; due: NO DUE DATE.

## Exceptions

- **EX-AGT-001** for AGT-02: Pilot limited to non-production synthetic transactions while approval workflow is completed.; approver: AI Risk Owner; expires: 2026-09-30.
- **EX-GOV-OLD** for GOV-03: Temporary governance route used during pilot.; approver: Programme Sponsor; expires: 2026-08-31.

## Important limitation

This report is generated by an educational assurance model. It is not certification evidence, legal advice, or a substitute for expert review.
