# Threat and risk model

The lab assumes that an enterprise AI system is not only a model. It is a system of:

```text
users
  ↓
application
  ↓
identity / authorization
  ↓
prompts + orchestration
  ↓
model
 ↙   ↘
RAG   tools/APIs
 ↓       ↓
data   enterprise systems
  \     /
 logging + monitoring
```

Important risk scenarios include:

- prompt injection,
- indirect prompt injection through retrieved content,
- unauthorized data retrieval,
- sensitive-data disclosure,
- tool abuse and excessive agency,
- privilege escalation through poorly designed orchestration,
- unsafe or incorrect automated actions,
- model/supplier changes,
- compromised dependencies,
- weak logging and non-repudiation,
- insufficient evaluation,
- failure to detect or respond to AI-specific incidents.

The governance model therefore treats architecture and technical security controls as part of assurance rather than as separate implementation details.
