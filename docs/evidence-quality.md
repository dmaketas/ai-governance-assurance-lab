# Evidence quality model

Version 0.2 replaces binary "evidence attached / not attached" logic with a transparent evidence-quality score.

Each evidence item carries:

- evidence type,
- quality level,
- verification status,
- optional freshness in days,
- a reference and description.

The score combines four dimensions:

1. **intrinsic quality** — low, medium, high or authoritative;
2. **evidence type** — e.g. self-attestation, architecture, configuration, test result, audit record;
3. **verification** — independently verified evidence receives more weight;
4. **freshness** — older evidence is discounted.

Where multiple artefacts exist, the strongest evidence receives the greatest weight and corroborating evidence adds confidence.

The model deliberately does not treat the mere presence of a document as proof that a control is effective.
