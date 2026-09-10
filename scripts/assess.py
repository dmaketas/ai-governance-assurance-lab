#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from ai_governance_assurance.models import AIUseCase
from ai_governance_assurance.assurance import assess


def main():
    parser = argparse.ArgumentParser(description="Assess an AI use case.")
    parser.add_argument("use_case", help="Path to use-case JSON")
    parser.add_argument("--controls", default="data/controls.csv")
    args = parser.parse_args()

    with open(args.use_case, encoding="utf-8") as fh:
        payload = json.load(fh)

    use_case = AIUseCase(**payload)
    result = assess(use_case, args.controls)

    print(f"Use case:         {use_case.name}")
    print(f"Inherent risk:    {result.inherent_risk}/100 ({result.risk_band})")
    print(f"Control coverage: {result.control_coverage}%")
    print(f"Residual risk:    {result.residual_risk}/100")
    print(f"Decision:         {result.decision}")
    for reason in result.reasons:
        print(f"- {reason}")


if __name__ == "__main__":
    main()
