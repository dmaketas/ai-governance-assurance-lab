#!/usr/bin/env python3
import argparse
import json
from datetime import date

from ai_governance_assurance.models import AIUseCase
from ai_governance_assurance.assurance import assess


def main():
    parser = argparse.ArgumentParser(description="Assess an AI use case.")
    parser.add_argument("use_case", help="Path to use-case JSON")
    parser.add_argument("--controls", default="data/controls.csv")
    parser.add_argument("--as-of", help="Assessment date YYYY-MM-DD")
    args = parser.parse_args()

    with open(args.use_case, encoding="utf-8") as fh:
        payload = json.load(fh)

    as_of = date.fromisoformat(args.as_of) if args.as_of else None
    use_case = AIUseCase(**payload)
    result = assess(use_case, args.controls, as_of=as_of)

    print(f"Use case:           {use_case.name}")
    print(f"Inherent risk:      {result.inherent_risk}/100 ({result.risk_band})")
    print(f"Control coverage:   {result.control_coverage}%")
    print(f"Evidence assurance: {result.evidence_assurance}%")
    print(f"Residual risk:      {result.residual_risk}/100")
    print(f"Decision:           {result.decision}")
    print("Policy gates:")
    for gate in result.policy_gates:
        print(f"  [{'PASS' if gate.passed else 'FAIL'}] {gate.gate_id}: {gate.name}")
    for reason in result.reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()
