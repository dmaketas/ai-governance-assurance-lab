# AI Governance & Assurance Lab

A practical Python lab for turning an AI use case into a traceable governance and assurance decision.

**Version:** 0.1.0

The project demonstrates a lightweight workflow for:

1. registering an AI use case,
2. assessing inherent risk,
3. identifying governance and security controls,
4. attaching evidence,
5. evaluating control coverage,
6. calculating residual risk,
7. producing a decision-oriented assurance report.

It is intentionally implementation-focused rather than a collection of policy notes.

## Why this project exists

AI governance often stops at principles, questionnaires, or compliance checklists. This lab explores a more operational model: **risk → controls → evidence → residual risk → decision**.

The goal is to make assurance traceable enough that an architect, security practitioner, risk owner, auditor, or approval body can understand:

- what the AI system does,
- what could go wrong,
- which controls are expected,
- what evidence actually exists,
- what remains unresolved,
- whether deployment should be approved, conditionally approved, or blocked.

## Framework alignment

The lab uses original control statements and does **not** reproduce proprietary standards.

Its control taxonomy is designed to be compatible with concepts commonly found in:

- ISO/IEC 42001 AI management systems,
- NIST AI Risk Management Framework,
- cybersecurity and privacy management systems,
- secure software and enterprise architecture practices.

Mappings are illustrative and should not be treated as certification evidence or a substitute for the official standards.

## Current capabilities

### Risk assessment

The engine scores an AI use case across:

- business criticality,
- data sensitivity,
- autonomy,
- external exposure,
- model dependency,
- human impact,
- regulatory impact,
- security impact.

### Control library

The included control catalogue covers:

- governance and accountability,
- AI inventory and ownership,
- data governance,
- model and supplier risk,
- secure architecture,
- access control,
- prompt and input security,
- retrieval-augmented generation controls,
- agent/tool-use controls,
- human oversight,
- logging and monitoring,
- evaluation and red teaming,
- incident response,
- privacy,
- change management,
- resilience and fallback.

### Evidence-based assurance

Controls can be marked as:

- `implemented`
- `partial`
- `planned`
- `not_implemented`
- `not_applicable`

Each assessment can reference evidence such as:

- architecture diagrams,
- test results,
- risk assessments,
- approval records,
- configuration exports,
- monitoring dashboards,
- supplier documentation.

The scoring model discounts controls without evidence.

### Decision output

The assurance engine returns one of:

- `APPROVE`
- `CONDITIONAL_APPROVAL`
- `REVIEW_REQUIRED`
- `BLOCK`

The report explains the decision and lists unresolved controls.

## Repository structure

```text
ai-governance-assurance-lab/
├── data/
│   ├── controls.csv
│   └── sample-evidence.csv
├── docs/
│   ├── assurance-model.md
│   ├── framework-mapping.md
│   └── threat-and-risk-model.md
├── examples/
│   ├── enterprise-rag-assistant.json
│   └── high-autonomy-agent.json
├── scripts/
│   ├── assess.py
│   └── generate_report.py
├── src/ai_governance_assurance/
│   ├── __init__.py
│   ├── models.py
│   ├── risk_engine.py
│   ├── control_engine.py
│   ├── assurance.py
│   └── reporting.py
├── tests/
│   ├── test_risk_engine.py
│   ├── test_control_engine.py
│   └── test_assurance.py
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
python scripts/assess.py examples/enterprise-rag-assistant.json
```

Generate a Markdown assurance report:

```bash
python scripts/generate_report.py \
  examples/enterprise-rag-assistant.json \
  --output assurance-report.md
```

## Example decision flow

```text
AI use case
    ↓
Inherent risk assessment
    ↓
Applicable control set
    ↓
Implementation status + evidence
    ↓
Control coverage
    ↓
Residual risk
    ↓
Assurance decision
```

## Example use case

The included `enterprise-rag-assistant.json` represents an internal enterprise assistant that retrieves controlled organizational documents and can summarize them for authenticated employees.

The assessment includes controls for:

- identity and authorization,
- data classification,
- RAG content validation,
- prompt injection,
- security logging,
- human oversight,
- supplier risk,
- evaluation and incident response.

## Design principles

### Evidence over assertion

A control marked "implemented" but supported by no evidence receives less assurance credit than an evidenced control.

### Governance should be executable

Risk and control decisions should be represented in structured data wherever practical, not only prose.

### Architecture is part of governance

AI governance cannot be separated from identity, data, APIs, cloud architecture, application security, observability, and operational controls.

### Human approval is not a universal mitigation

Human oversight can reduce risk, but it should not be used as a substitute for technical controls where automated systems can cause material impact before a person can intervene.

### Residual risk must remain visible

The objective is not to produce a green dashboard. The objective is to support an informed decision.

## Roadmap

### v0.2
- richer evidence quality scoring,
- policy-as-code control gates,
- JSON/CSV batch assessment,
- control ownership and due dates,
- exception register.

### v0.3
- AI agent assurance profile,
- secure RAG assurance profile,
- LLM security findings import,
- supplier/model risk assessment.

### v0.4
- web dashboard,
- audit trail,
- assurance history and comparison,
- machine-readable governance artefacts.

## Disclaimer

This project is educational and experimental. It does not constitute legal advice, certification guidance, or a complete AI governance programme.
