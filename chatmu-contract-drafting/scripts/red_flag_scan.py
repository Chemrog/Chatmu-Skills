#!/usr/bin/env python3
"""Scan a contract text/markdown for common music-industry red flags.

Input: /workspace/in/contract.txt|.md (or first argv, text content).
Output: /workspace/out/red_flags.md with matched flags + severity.

Run only via the execute_python sandbox.
"""
import os
import re
import sys

# (pattern, flag, severity, note)
RULES = [
    (r"in perpetuity|perpetual|forever|irrevocab\w*", "Perpetuity / irrevocable term", "HIGH",
     "Check for a term limit and a reversion date for masters & rights."),
    (r"\ball rights\b|entire copyright|exclusively and solely", "All-rights / exclusive grant", "MEDIUM",
     "Scope the grant: territory, term and exploitation channels must be defined."),
    (r"gross receipts|gross revenue", "Commission/base on gross", "MEDIUM",
     "Confirm whether commissions are on gross or modified gross (deductions matter)."),
    (r"admin fee|administrative fee", "Admin fee present", "LOW",
     "Typical 10-25%; watch for a double-dip: admin fee PLUS a % of gross."),
    (r"recoup\w*|recoupable", "Recoupable advance", "LOW",
     "Recoupable = recoverable against royalties; confirm what is recouped (recording costs?)."),
    (r"reversion|revert", "Reversion right mentioned", "GOOD",
     "Positive sign: masters/rights revert after a term — verify conditions."),
    (r"terminat\w*", "Termination clause present", "GOOD",
     "Ensure there is an exit (and a sunset schedule if management)."),
    (r"work for hire|work-for-hire", "Work-for-hire", "MEDIUM",
     "Who owns the work? WFH transfers authorship/ownership to the payer — get it in writing."),
    (r"draft|placeholder|TBD|to be determined", "Placeholders / TBD", "LOW",
     "Unfilled blanks are the #1 source of disputes; complete before signing."),
]


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/in/contract.txt"
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    results = []
    for pattern, flag, severity, note in RULES:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            results.append((severity, flag, len(matches), note))

    results.sort(key=lambda r: {"HIGH": 0, "MEDIUM": 1, "LOW": 2, "GOOD": 3}.get(r[0], 4))

    lines = ["# Red Flag Scan", ""]
    if not results:
        lines.append("No common red-flag patterns detected. Still have a lawyer review it.")
    for severity, flag, count, note in results:
        lines.append(f"- **[{severity}]** {flag} (x{count}) — {note}")

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "red_flags.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {out_path} — {len(results)} patterns matched")


if __name__ == "__main__":
    main()
