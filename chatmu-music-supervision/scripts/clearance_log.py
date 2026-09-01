#!/usr/bin/env python3
"""Build a music clearance log (.xlsx) for a sync/supervision project.

Input: /workspace/in/clearance.json (or first argv) with:
  project, tracks: [{title, isrc, master_owner, publisher, sync_status,
                     master_status, notes, deadline}]
Output: /workspace/out/clearance_log.xlsx

Run only via the execute_python sandbox. pandas + openpyxl preinstalled.
"""
import json
import os
import sys

import pandas as pd


def load_input() -> dict:
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/in/clearance.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    data = load_input()
    tracks = data.get("tracks", [])
    rows = []
    for t in tracks:
        rows.append({
            "title": t.get("title", ""),
            "isrc": t.get("isrc", ""),
            "master_owner": t.get("master_owner", ""),
            "publisher": t.get("publisher", ""),
            "sync_status": t.get("sync_status", "pending"),
            "master_status": t.get("master_status", "pending"),
            "deadline": t.get("deadline", ""),
            "notes": t.get("notes", ""),
        })

    df = pd.DataFrame(rows)
    status_order = {"pending": 0, "in_progress": 1, "cleared": 2, "denied": 3}
    if not df.empty:
        df["_sort"] = df["sync_status"].map(status_order).fillna(4)
        df = df.sort_values("_sort").drop(columns="_sort")

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "clearance_log.xlsx")
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="clearances", index=False)

    done = int((df["sync_status"] == "cleared").sum()) if not df.empty else 0
    print(f"Saved {out_path} — {len(df)} tracks, {done} cleared")


if __name__ == "__main__":
    main()
