#!/usr/bin/env python3
"""Reconcile royalty statements against expected earnings.

Reads one or more CSV statements (pandas) plus an optional expected-splits
JSON, and produces:
  - /workspace/out/reconciled.xlsx — sheet "reconciled" + sheet "blackbox".

Convention: inputs at /workspace/in/*.csv and /workspace/in/expected.json.
Run only via the execute_python sandbox. pandas + openpyxl preinstalled.
"""
import glob
import json
import os
import sys

import pandas as pd


def guess_columns(df: pd.DataFrame) -> dict:
    cols = {c.lower().strip(): c for c in df.columns}
    def pick(*names):
        for n in names:
            if n in cols:
                return cols[n]
        return None
    return {
        "track": pick("track", "song", "title", "isrc"),
        "earned": pick("earned", "net", "net earnings", "royalty", "amount", "gross"),
        "plays": pick("plays", "streams", "units", "count"),
    }


def main() -> None:
    in_dir = "/workspace/in"
    expected = {}
    expected_path = os.path.join(in_dir, "expected.json")
    if os.path.exists(expected_path):
        with open(expected_path, "r", encoding="utf-8") as f:
            expected = json.load(f)  # {isrc_or_title: amount_expected}

    files = glob.glob(os.path.join(in_dir, "*.csv"))
    if not files:
        print("No CSV files found under /workspace/in/", file=sys.stderr)
        sys.exit(1)

    frames = []
    for f in files:
        df = pd.read_csv(f)
        frames.append(df)
    df = pd.concat(frames, ignore_index=True) if len(frames) > 1 else frames[0]

    m = guess_columns(df)
    track_col = m["track"]
    earned_col = m["earned"]
    plays_col = m["plays"]

    if not track_col or not earned_col:
        print(f"Could not map columns. Columns: {list(df.columns)}", file=sys.stderr)
        sys.exit(1)

    grouped = df.groupby(track_col)[earned_col].sum().reset_index()
    if plays_col:
        grouped["plays"] = df.groupby(track_col)[plays_col].sum().reset_index()[plays_col]

    grouped.columns = ["track", "reported_earned"] + (["plays"] if plays_col else [])
    grouped["expected_earned"] = grouped["track"].map(
        lambda k: float(expected.get(str(k), expected.get(str(k).upper(), float("nan"))))
    )
    grouped["delta"] = grouped["reported_earned"] - grouped["expected_earned"]
    grouped["status"] = grouped["delta"].apply(
        lambda d: "MATCH" if pd.isna(d) else ("UNDERPAID" if d > 0.005 else "OVERPAID" if d < -0.005 else "MATCH")
    )

    # Black box: reported lines with no ISRC/title match in expected → likely unregistered
    blackbox = grouped[grouped["expected_earned"].isna()].copy()

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "reconciled.xlsx")
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        grouped.to_excel(writer, sheet_name="reconciled", index=False)
        blackbox.to_excel(writer, sheet_name="blackbox", index=False)

    total_underpaid = grouped[grouped["status"] == "UNDERPAID"]["delta"].sum()
    print(f"Saved {out_path}")
    print(f"Rows: {len(grouped)} | Black-box candidates: {len(blackbox)} | Underpaid delta: {total_underpaid:.2f}")


if __name__ == "__main__":
    main()
