#!/usr/bin/env python3
"""Build a show budget / P&L / breakeven / door sheet (.xlsx).

Input: /workspace/in/show_budget.json (or first argv) with:
  show_name, capacity, expected_sell_through_pct,
  ticket_tiers: [{name, price, units}],
  merch_revenue_est, sponsor_contributions: [{name, amount}], bar_aux_net_est,
  venue_rent, production_cost, promo_cost, artist_guarantee,
  opening_acts_fees, fees_other, venue_door_split_pct
Output: /workspace/out/show_budget.xlsx with Revenue, Costs, P&L, Breakeven,
Door sheets. Run only via the execute_python sandbox.
"""
import json
import os
import sys

import pandas as pd


def load_input() -> dict:
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/in/show_budget.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    d = load_input()
    capacity = int(d.get("capacity", 0))
    sell = float(d.get("expected_sell_through_pct", 0.7))
    door_split = float(d.get("venue_door_split_pct", 0.0))

    tiers = d.get("ticket_tiers", [])
    revenue_rows = []
    ticket_gross = 0.0
    for t in tiers:
        units = int(t.get("units", 0))
        price = float(t.get("price", 0))
        gross = units * price
        ticket_gross += gross
        revenue_rows.append({
            "source": f"Tickets · {t.get('name', 'Tier')}",
            "units": units,
            "price": price,
            "gross": round(gross, 2),
        })

    expected_units = round(capacity * sell)
    expected_ticket_gross = 0.0
    for t in tiers:
        units = int(t.get("units", 0))
        expected_units_this = round(units * sell)
        expected_ticket_gross += expected_units_this * float(t.get("price", 0))

    sponsors = d.get("sponsor_contributions", [])
    sponsor_total = sum(float(s.get("amount", 0)) for s in sponsors)

    merch = float(d.get("merch_revenue_est", 0))
    bar = float(d.get("bar_aux_net_est", 0))

    revenue_rows += [
        {"source": "Merch", "units": "", "price": "", "gross": round(merch, 2)},
        {"source": "Sponsors", "units": "", "price": "", "gross": round(sponsor_total, 2)},
        {"source": "Bar / aux (net)", "units": "", "price": "", "gross": round(bar, 2)},
    ]
    revenue_df = pd.DataFrame(revenue_rows)
    total_revenue = ticket_gross + merch + sponsor_total + bar
    venue_take = ticket_gross * door_split

    cost_rows = [
        {"cost": "Venue rent", "amount": float(d.get("venue_rent", 0))},
        {"cost": f"Venue door split ({int(door_split*100)}% of tickets)", "amount": round(venue_take, 2)},
        {"cost": "Production", "amount": float(d.get("production_cost", 0))},
        {"cost": "Promotion", "amount": float(d.get("promo_cost", 0))},
        {"cost": "Artist guarantee", "amount": float(d.get("artist_guarantee", 0))},
        {"cost": "Opening acts fees", "amount": float(d.get("opening_acts_fees", 0))},
        {"cost": "Other fees", "amount": float(d.get("fees_other", 0))},
    ]
    cost_df = pd.DataFrame(cost_rows)
    total_costs = cost_df["amount"].sum()
    net = total_revenue - total_costs

    # Breakeven: gross tickets needed so that net >= 0 (holding other lines).
    other_rev = merch + sponsor_total + bar
    net_ticket_rev_needed = total_costs - other_rev
    avg_price = (ticket_gross / capacity) if capacity else 0
    breakeven_sell = (net_ticket_rev_needed / avg_price / capacity) if (avg_price and capacity) else float("nan")
    breakeven_rows = pd.DataFrame([
        {"metric": "capacity", "value": capacity},
        {"metric": "expected_sell_through_pct", "value": sell},
        {"metric": "expected_units", "value": expected_units},
        {"metric": "expected_ticket_gross", "value": round(expected_ticket_gross, 2)},
        {"metric": "avg_ticket_price", "value": round(avg_price, 2)},
        {"metric": "breakeven_sell_through_pct", "value": round(breakeven_sell * 100, 1) if breakeven_sell == breakeven_sell else None},
    ])

    door_rows = pd.DataFrame([
        {"item": "Ticket gross", "amount": round(ticket_gross, 2)},
        {"item": "Venue share (door split)", "amount": round(venue_take, 2)},
        {"item": "Artist net from door", "amount": round(ticket_gross - venue_take, 2)},
        {"item": "Merch gross", "amount": round(merch, 2)},
        {"item": "Sponsor cash in hand", "amount": round(sponsor_total, 2)},
    ])

    pnl = pd.DataFrame([
        {"line": "Total revenue", "amount": round(total_revenue, 2)},
        {"line": "Total costs", "amount": round(total_costs, 2)},
        {"line": "NET (pre-artist split)", "amount": round(net, 2)},
    ])

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "show_budget.xlsx")
    with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
        revenue_df.to_excel(writer, sheet_name="Revenue", index=False)
        cost_df.to_excel(writer, sheet_name="Costs", index=False)
        pnl.to_excel(writer, sheet_name="P&L", index=False)
        breakeven_rows.to_excel(writer, sheet_name="Breakeven", index=False)
        door_rows.to_excel(writer, sheet_name="Door", index=False)

    print(f"Saved {out_path}")
    print(f"Revenue: {total_revenue:.2f} | Costs: {total_costs:.2f} | Net: {net:.2f} | Breakeven sell-through: {breakeven_sell*100:.1f}%" if breakeven_sell == breakeven_sell else f"Saved {out_path}")


if __name__ == "__main__":
    main()
