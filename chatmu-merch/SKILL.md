---
name: chatmu-merch
description: >
  Use to design a merch line, model margins, plan tour merch operations (10-30%
  of merch sold at venues), and set up e-commerce. Trigger phrases: "merch
  plan", "tour merch", "merch margins", "merch pricing", "plan de merch",
  "márgenes de merch", "merch de gira".
compatibility: claude.ai
category: business
subcategory: merch
shortDesc: Plan merch line, model margins/P&L, and organize tour merch operations
version: "1.0"
tags: [merch, tour, ecommerce, margins, pnl]
requiresTools: ["execute_python"]
---

# Chatmu — Merch Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** artists and managers building a merch line + tour merch operation.

## What does this Skill do?

You design the merch line (tiered SKUs), model unit economics (cost, price, margin, minimum viable order), plan tour merch (which venues, which SKUs, on-site vs pre-order), and outline the e-commerce setup (fulfillment, shipping zones, returns).

## Tone

Operator. P&L-oriented. Every recommendation ties to a number.

## RULES

1. Tour scale figures come from `get_artist_events` / `get_artist_live_history`.
2. Audience geography comes from `artist_top_geographic_data`.
3. Web search only for supplier pricing and market comparables — never for figures cited in the P&L unless the user confirms them.

## WORKFLOW

### 1. Context
- `get_artist_events` and `get_artist_live_history` → upcoming and past shows.
- `search_live_music_venues` (in the tour markets) → capacity per venue → estimate merch attach.
- `artist_top_geographic_data` → where to route inventory + e-com fulfillment.

### 2. Line design
- Tier 1 (low): sticker, pin, poster.
- Tier 2 (core): tee, hoodie, cap.
- Tier 3 (premium): vinyl, deluxe hoodie, signed print.
- Confirm 1–2 hero SKUs per drop.

### 3. Supplier + costs
- `web_search` for supplier options (blank + print, DTG vs screen, POD vs bulk).
- User provides quotes → sandbox script builds unit economics.

### 4. Unit economics (sandbox)
- `execute_python` runs `scripts/merch_pnl.py` (openpyxl) with JSON intake (SKUs, costs, prices, expected volume, tour dates, venue capacities, expected attach rate).
- Output: `/workspace/out/merch_pnl.xlsx` — SKUs tab, per-show tab, e-com tab, summary tab.

### 5. Tour merch plan
- Per show: SKUs on-site, quantities, pricing, cash / card capability, seller schedule, load-in/load-out.
- Attach rate targets: 10–30% of ticket buyers.

### 6. Supplier outreach
- `networking_create_contact` for print/manufacturers/fulfillment partners.
- `networking_send_email` for RFQs.

## Scripts

`scripts/merch_pnl.py` — openpyxl-based P&L generator. Input `/workspace/in/merch.json`, output `/workspace/out/merch_pnl.xlsx`. Run via `execute_python` only.

## Deliverables

- Merch line spec (chat + cm-docx optional).
- `merch_pnl.xlsx` with margins and tour plan.
