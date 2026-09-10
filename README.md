# AI Governance & Assurance Lab

A practical Python lab for turning an AI use case into a traceable, evidence-based governance and assurance decision.

**Version:** 0.2.0

The project implements the workflow:

```text
AI use case
    ↓
inherent risk
    ↓
applicable controls
    ↓
implementation status
    ↓
evidence quality
    ↓
exceptions + owners + due dates
    ↓
policy-as-code gates
    ↓
residual risk
    ↓
assurance decision
```

## Why this project exists

AI governance often stops at principles, questionnaires or compliance checklists. This lab explores a more operational model:

**risk → controls → evidence → exceptions → policy gates → residual risk → decision**

The objective is not to generate a green dashboard. It is to make an AI assurance decision traceable enough that an architect, security practitioner, risk owner, auditor or approval body can understand:

- what the system does,
- what could go wrong,
- which controls apply,
- who owns unresolved actions,
- what evidence supports implementation claims,
- whether exceptions are valid and time-bound,
- which policy gates pass or fail,
- what residual risk remains,
- why the deployment decision was reached.

## What is new in v0.2

### Evidence-quality scoring

Evidence is now scored using:

- evidence type,
- intrinsic quality,
- verification status,
- freshness.

An implemented control without strong evidence no longer receives full assurance credit.

### Control ownership and due dates

Unresolved controls can have:

- accountable owners,
- remediation due dates.

Policy gates identify unassigned and overdue actions.

### Exception management

Exceptions record:

- the affected control,
- rationale,
- approver,
- expiry date,
- compensating controls.

Expired or invalid exceptions are surfaced explicitly and can block approval.

### Policy-as-code

Deterministic gates prevent aggregate numerical scores from hiding critical weaknesses.

Current gates cover:

- critical control gaps,
- invalid/expired exceptions,
- missing control owners,
- overdue remediation,
- minimum evidence assurance.

### Committed assurance reports

The repository includes generated reports for:

1. an **Enterprise RAG Assistant**, and
2. a **High-Autonomy Service Agent**.

These show the full decision chain, including risk score, evidence assurance, control results, exceptions and failed policy gates.

## Framework alignment

The lab uses original control statements and does **not** reproduce proprietary standards.

Its taxonomy is designed to be compatible with concepts commonly found in:

- ISO/IEC 42001,
- NIST AI Risk Management Framework,
- cybersecurity and privacy management systems,
- secure software and enterprise architecture practices,
- LLM application security and adversarial testing.

Mappings are illustrative and are not certification evidence.

## Repository structure

```text
ai-governance-assurance-lab/
├── data/
│   ├── controls.csv
│   └── sample-evidence.csv
├── docs/
│   ├── assurance-model.md
│   ├── evidence-quality.md
│   ├── exception-management.md
│   ├── policy-as-code.md
│   ├── framework-mapping.md
│   └── threat-and-risk-model.md
├── examples/
│   ├── enterprise-rag-assistant.json
│   └── high-autonomy-agent.json
├── reports/
│   ├── enterprise-rag-assistant-assurance.md
│   └── high-autonomy-agent-assurance.md
├── scripts/
│   ├── assess.py
│   └── generate_report.py
├── src/ai_governance_assurance/
│   ├── assurance.py
│   ├── control_engine.py
│   ├── evidence.py
│   ├── exceptions.py
│   ├── models.py
│   ├── policy.py
│   ├── reporting.py
│   └── risk_engine.py
├── tests/
├── .github/workflows/tests.yml
├── LICENSE
└── pyproject.toml
```

## Quick start

Requires Python 3.10+.

```bash
python -m pip install -e ".[dev]"
pytest -q
```

Run an assessment:

```bash
python scripts/assess.py   examples/enterprise-rag-assistant.json   --as-of 2026-09-10
```

Generate a report:

```bash
python scripts/generate_report.py   examples/enterprise-rag-assistant.json   --as-of 2026-09-10   --output assurance-report.md
```

## Design principles

### Evidence over assertion

The presence of a policy, diagram or statement is not automatically proof of control effectiveness.

### Critical gaps should not disappear inside averages

Policy-as-code gates can block a decision even when aggregate scores look acceptable.

### Exceptions should expire

Risk acceptance should be explicit, approved, time-bound and visible.

### Accountability should be operational

Unresolved controls should have identifiable owners and dates, not simply appear in a risk register.

### Architecture is part of governance

AI governance cannot be separated from identity, APIs, data, cloud architecture, RAG trust boundaries, tool permissions, application security and monitoring.

### Residual risk must remain visible

The purpose of assurance is to support an informed decision, not to force a predetermined approval.

## Roadmap

### v0.3
- import findings from `llm-security-lab`,
- dedicated secure-RAG assurance profile,
- dedicated agentic-AI assurance profile,
- supplier/model dependency scoring,
- machine-readable decision output.

### v0.4
- portfolio/batch assessment,
- historical assurance comparison,
- exception register dashboard,
- audit trail,
- optional web interface.

## Disclaimer

This project is educational and experimental. It does not constitute legal advice, certification guidance or a complete AI governance programme.
