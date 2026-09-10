#!/usr/bin/env python3
import argparse
import json

from ai_governance_assurance.models import AIUseCase
from ai_governance_assurance.assurance import assess
from ai_governance_assurance.reporting import markdown_report


def main():
    parser = argparse.ArgumentParser(description="Generate an AI assurance report.")
    parser.add_argument("use_case", help="Path to use-case JSON")
    parser.add_argument("--controls", default="data/controls.csv")
    parser.add_argument("--output", default="assurance-report.md")
    args = parser.parse_args()

    with open(args.use_case, encoding="utf-8") as fh:
        use_case = AIUseCase(**json.load(fh))

    result = assess(use_case, args.controls)
    report = markdown_report(use_case, result)

    with open(args.output, "w", encoding="utf-8") as fh:
        fh.write(report)

    print(f"Wrote {args.output} ({result.decision})")


if __name__ == "__main__":
    main()
