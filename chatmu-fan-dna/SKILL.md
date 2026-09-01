---
name: chatmu-fan-dna
description: >
  Use to run psychographic + demographic audience analysis, build buyer personas,
  analyze engagement by location, and measure social→streaming conversion.
  Trigger phrases: "fan DNA", "audience analysis", "buyer persona",
  "audience conversion", "ADN de fans", "análisis de audiencia",
  "persona compradora".
compatibility: claude.ai
category: analytics
subcategory: audience
shortDesc: Psychographic + demographic fan analysis, personas, and conversion
version: "1.0"
tags: [audience, fans, persona, conversion, analytics]
---

# Chatmu — Fan DNA Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** managers, marketers and A&Rs profiling an artist's fanbase.

## What does this Skill do?

You produce a Fan DNA profile for an artist: who they are (demographic + psychographic), where they are (city-level engagement), how the funnel converts (social → streaming), and what markets have upside. Output includes buyer persona cards ready for briefs.

## Tone

Insight-first. Every number carries a decision it enables.

## RULES

1. Every metric traces to a MCP tool. No made-up affinities.
2. When Fan DNA has not been analyzed, request analysis before profiling.

## WORKFLOW

### 1. Check availability
- `list_analyzed_fans_dna` → is there a Fan DNA for the artist?
- If yes → `get_fans_dna_details` for the psychographic profile.

### 2. Demographics + geography
- `audience_demographics` (platforms: all, includeInterests: yes).
- `engagement_by_location` → real fans vs. casual.
- `artist_top_geographic_data` → top cities/countries.
- `geographic_growth_analysis` → where momentum is building.
- `search_specific_location` for a focus city.

### 3. Platform reach
- `get_platform_audience` per DSP/social.

### 4. Conversion
- `analyze_audience_conversion` → funnel top-to-bottom.
- `analyze_social_to_streaming_conversion` → paid + organic conversion lift.
- `analyze_niche_compatibility` → retention/loyalty.

### 5. Market upside
- `market_potential_analysis` (targetLocation: top 3 cities) → gap analysis.

### 6. Personas
- Build 2–3 personas: name, age band, top city, top platform, interests, listening moment, spend proxy, activation channels.

## Deliverables

- Fan DNA report (chat + `cm-docx` / `cm-pdf` for a full version).
- Persona cards (2–3).
- Priority markets list.
