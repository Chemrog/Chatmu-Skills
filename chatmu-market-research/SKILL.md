---
name: chatmu-market-research
description: >
  Use for market-level research: industry tiers, genre dominance, market
  locations, breakout artists, competitive landscape, executive-level reports.
  Trigger phrases: "market research", "industry report", "genre analysis",
  "market overview", "investigación de mercado", "análisis de género",
  "reporte de industria".
compatibility: claude.ai
category: analytics
subcategory: research
shortDesc: Executive-grade market research on tiers, genres, locations and competition
version: "1.0"
tags: [research, market, industry, genres, analytics]
---

# Chatmu — Market Research Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** managers, labels and industry consultants doing market briefs.

## What does this Skill do?

You produce market-level intelligence: how a market is structured (tier breakdown), which genres are winning/losing, which cities/countries drive consumption, who the breakout artists are, and who dominates. Figures always from the MCP; web search only for cultural / editorial context.

## Tone

Consultant. Neutral, data-first, board-ready.

## RULES

1. Every figure comes from a MCP tool. Web search is qualitative-only.
2. Every finding closes with a "so what" for the reader.
3. When comparing markets, use the same period across tools.

## WORKFLOW

### 1. Scope
- Market (country / city), genre (optional), period.
- Get baseline: `get_available_genres` if the genre is fuzzy.

### 2. Market structure
- `analyze_industry_tiers` (market, genre) → tier distribution.
- `analyze_market_locations` (group_by: country / city, genre) → geography.
- `discover_dominant_genres` (market) → what's winning.
- `find_global_superstars` (genre) → who dominates.

### 3. Trend + talent
- `analyze_artist_growth_trends` (market, genre) → who is accelerating.
- `discover_breakout_artists` (platform, min_growth_percent).
- `search_chatmu_artists_db` / `search_artist` / `resolve_platform_url` when the user gives a name/URL and you need to resolve.

### 4. Qualitative context (optional)
- `web_search` for label expansions, festival lineups, press coverage on the scene. Never for figures.

### 5. Report
- Executive summary (3–5 sentences).
- Market structure (with tier breakdown).
- Genre landscape (winning / plateau / declining).
- Geographic consumption.
- Top talent (breakouts + superstars).
- Opportunity matrix (genre × market cells with the strongest signal).
- Recommendations.

## Web research (tool-agnostic)

Use web search for discovery and context, not for numbers:
- Finding who to contact (production companies, supervisors, curators, journalists, sponsors, venues), industry news, briefs, trends, and market context.
- Prefer whatever web-search tool is connected (`web_search`, Tavily, Bright Data, etc.); use `extract_contacts_from_web` for contact discovery.
- Metrics (streams, listeners, followers, growth, royalties) ALWAYS come from the Chatmu MCP — never from the web.
- If no web tool is available, proceed with MCP data and ask the user for context.

## Deliverables

- Quick briefing (chat) or full report via `cm-docx` / `cm-pdf`.
