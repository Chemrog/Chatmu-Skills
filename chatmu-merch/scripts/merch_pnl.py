#!/usr/bin/env python3
"""Model merch line P&L: items, costs, prices, margins, tour venue splits.

Input: /workspace/in/merch.json (or first argv) with:
  items: [{name, cost, price, units_sold}]
  venue_share_pct: default 0.20 (20% of gross to venue), per-item optional
Output: /workspace/out/merch_pnl.xlsx (items sheet + summary) + printed summary.

Run only via the execute_python sandbox. pandas + openpyxl preinstalled.
"""
import json
import os
import sys

import pandas as pd


def load_input() -> dict:
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/in/merch.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    data = load_input()
    items = data.get("items", [])
    default_venue_share = float(data.get("venue_share_pct", 0.20))
    if not items:
        print("No items in input.", file=sys.stderr)
        sys.exit(1)

    rows = []
    for it in items:
        name = it.get("name", "Item")
        cost = float(it.get("cost", 0))
        price = float(it.get("price", 0))
        units = int(it.get("units_sold", 0))
        gross = price * units
        venue_share = float(it.get("venue_share_pct", default_venue_share))
        venue_take = gross * venue_share
        cogs = cost * units
        artist_net = gross - venue_take - cogs
        rows.append({
            "item": name,
            "cost": cost,
            "price": price,
            "units": units,
            "gross": round(gross, 2),
            "venue_share_pct": venue_share,
            "venue_take": round(venue_take, 2),
            "cogs": round(cogs, 2),
            "artist_net": round(artist_net, 2),
            "margin_pct": round((artist_net / gross * 100) if gross else 0, 1),
        })

    df = pd.DataFrame(rows)
    total_gross = df["gross"].sum()
    total_net = df["artist_net"].sum()
    summary = pd.DataFrame([{
        "metric": "total_gross", "value": total_gross,
    }, {
        "metric": "total_venue_take", "value": df["venue_take"].sum(),
    }, {
        "metric": "total_cogs", "value": df["cogs"].sum(),
    }, {
        "metric": "total_artist_net", "value": total_net,
    }, {
        "metric": "blended_margin_pct", "value": round(total_net / total_gross * 100, 1) if total_gross else 0,
    }])

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "merch_pnl.xlsx")
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="items", index=False)
        summary.to_excel(writer, sheet_name="summary", index=False)

    print(f"Saved {out_path}")
    print(f"Items: {len(df)} | Gross: {total_gross:.2f} | Artist net: {total_net:.2f} | Margin: {total_net/total_gross*100:.1f}%" if total_gross else "Saved")


if __name__ == "__main__":
    main()
