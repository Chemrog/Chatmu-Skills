---
name: chatmu-artist-report
description: >
  Generates artist performance reports for Chatmu — weekly, monthly, or release
  tracking (single, EP, or album) — in the Pro Indie Music / Chatmu format: half
  data diagnostic, half actionable content strategy. Use whenever a manager asks
  for a "weekly report", "monthly report", "release report", an "update on" a
  song or artist, "how's" a single doing, or a performance update for any artist
  they manage. Also use if they ask for a report in this format or any variant
  of that style. Trigger phrases: "weekly report", "monthly report", "release
  report", "update on", "how's", "performance update".
compatibility: claude.ai
category: analytics
subcategory: artist-report
shortDesc: Creates artist performance reports with data diagnostics and content strategy
---

# Chatmu — Artist Report Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP (100+ tools)
**For:** Managers preparing performance deliverables for labels (Pro Indie Music / Chatmu)
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

Produces artist performance reports in the Chatmu / Pro Indie Music style: half
data diagnostic, half actionable content strategy. The reference format is
documented in `references/report-template.md`.

Every report is a **deliverable** — plain text or simple Markdown, ready to
copy/paste or hand to a document. Not an interactive dashboard, not a chat
summary. This is what a manager sends to a label.

---

## RULE #1 — Never invent figures

All streaming, audience, playlist, and demographic numbers MUST come from the
Chatmu MCP tools. If a data point is not available in Chatmu, say so explicitly
in the report ("data not available on this platform") instead of filling it in.

Web search (see RULE #4) is for qualitative context only, never for numbers.

---

## RULE #2 — Pick the right variant

| Type | When | Focus |
|------|------|-------|
| **Weekly** | Ongoing tracking of an already-released single, or an artist in an active campaign | Day-over-day stream trends, changes in discovery sources, what content to publish this week |
| **Monthly** | Month-end cut, comparison against the previous month, reviewing several releases or the catalog | Cumulative growth, MoM comparison, overall artist health (all platforms), next month's priorities |
| **Per release** | First 7/14/30 days of a new single, EP, or album | Initial push vs. drop-off, own-audience conversion, "reinforce / let it run / pivot" decision |

If the manager doesn't specify, ask only if it's ambiguous between the three.
Rules of thumb:
- Mentions a date range or "this week" → **Weekly**
- Says "this month" or asks to compare months → **Monthly**
- The song came out ≤30 days ago → **Per release**

---

## RULE #3 — Gather the data from Chatmu MCP

Use Chatmu tools to get the numbers. Typical tools depending on what you need:

- `song_identity_resolver` / `search_chatmu_songs` — find the song's UUID
- `get_song_performance_and_charts` — streams, listeners, chart position
- `get_released_song_metadata` — metadata and "DNA" of the released track
- `artist_current_stats` / `get_platform_audience` — total audience, Active Listeners, Super Listeners per platform
- `get_artist_active_playlists` / `find_latest_editorial_placements` — editorial vs. algorithmic playlist breakdown
- `audience_demographics` — ideal listener profile (age, gender, location, behavior)
- `get_artist_retention` — audience conversion / retention rate
- `engagement_by_location` / `geographic_growth_analysis` — if the report needs a geographic cut
- `get_artist_briefing` — if an automated briefing already exists for that artist, use it as the base input

---

## RULE #4 — Web search is qualitative-only, and optional

Web search complements the MCP in exactly two sections of the report, and
nowhere else:

1. **Ideal listener profile (Section 9)** — to enrich "visual aesthetic they
   connect with", "main motivation", and "interests outside music" with current,
   concrete references for that demographic (brands, visual trends, platforms,
   cultural touchpoints). The MCP gives the demographic skeleton; web gives the
   cultural flesh.
2. **Recommended strategy (Section 7)** — to check which vertical formats, hooks,
   and narrative tones are currently performing on TikTok/Reels for that niche.
   This changes fast and web keeps it fresh.

**Hard limits:**
- NEVER use web search for streaming counts, listener counts, playlist counts,
  chart positions, retention rates, or any metric. Those are MCP-only.
- NEVER blend a web-sourced figure into the report as if it were Chatmu data.
- If web search is not available, fall back to Claude's reasoning over the MCP
  demographic data. The report still works without it.
- When you do use web context, keep it implicit in the recommendations — don't
  cite URLs or "according to the internet" in the deliverable. The report reads
  as one voice.

---

## STEP 1 — Gather the data

Follow RULE #3. Pull what you need for the chosen variant. Don't pull everything
if the variant doesn't require it (a weekly report doesn't need a full catalog
audit).

If a datum isn't available in Chatmu, say so in the report rather than filling
it in.

---

## STEP 2 — Calculate derived metrics

These almost always have to be computed by hand from the raw data:

- **Streams per listener** = streams / listeners. ~1.0 indicates drive-by
  listening, not recurring fans.
- **Save rate** = saves / streams (×100). Reference: >8% is a good affinity
  signal.
- **% of streams by source** = algorithmic / editorial / own catalog / other
  (should sum to ~100%).
- **% of audience that already heard the release** = track listeners / artist's
  Active Listeners (and the same against Super Listeners). This is the key
  indicator of own-audience conversion — the metric a label cares about most.
- **Daily trend** = streams/day at the start vs. streams/day now, to detect
  whether momentum is holding or falling.

---

## STEP 3 — Write the report

Follow this structure and tone (direct, no filler, figures first then a
one-sentence interpretation):

1. **Header:** "Report: [Weekly/Monthly/Release] – '[Song/Artist]' | [Artist]"
   + cutoff date.
2. **Streams / listeners summary:** total figure for the period + what the
   streams-per-listener ratio means.
3. **Saves:** figure + save rate + affinity interpretation.
4. **Stream sources:** % breakdown algorithmic / editorial / catalog / other,
   and how dependent it is on external discovery vs. own audience.
5. **Artist audience:** total Active Listeners and Super Listeners, and how
   many / what % of each already heard the release. This is the section the
   manager cares about most — always include it even if the report is general
   catalog; it's the metric a label cares about most.
6. **Trend:** streams/day at the start of the period vs. streams/day now (or
   MoM comparison if it's a monthly report).
7. **Recommended strategy:** 3-6 concrete, actionable organic content
   recommendations — not generic. They must be anchored to the ideal listener
   profile (see STEP 4): format, duration, frequency, who appears on camera,
   narrative tone. If something isn't working (e.g. third-party content, a
   specific format), say it directly. This is one of the two sections where web
   context may inform the recommendations (RULE #4).
8. **Conclusion:** 3-4 lines connecting data with strategy — what's working,
   what isn't, and the next step.
9. **Ideal listener profile:** age, socio-economic level, location, main
   motivation (self-expression, entertainment, etc.), visual aesthetic they
   connect with, platform/device of consumption, interests outside music. This
   section barely changes between reports for the same artist — reuse it if it
   already exists from a previous report, only update it when there's new
   demographic data. This is the other section where web context may enrich
   the qualitative profile (RULE #4).

---

## Differences by report type

**Weekly:**
- May omit or summarize the ideal listener profile section if it was sent
  recently; focus the report on "what to publish this week".

**Monthly:**
- Add a table or paragraph comparing the current month vs. the previous one
  (total streams, audience growth, new playlists gained/lost).
- If there were several releases in the month, summarize each in 2-3 lines
  before going into detail on the most relevant one.

**Per release:**
- Add a timeline of the initial push (day 1, day 7, day 14, day 30 if
  applicable).
- End with an explicit decision recommendation: reinforce with more content,
  let it run organically, or pivot the strategy because there's no traction.

---

## Delivery format

- Plain text or simple Markdown, ready to copy/paste or hand to a document.
- If the manager explicitly asks for a PDF or Word, use the corresponding docx
  or pdf skill after the final content is ready.
- Numbers always with thousands separator (33,860) and percentages with one
  decimal when it adds precision (8.5%).
- No emojis. Section headers in bold or as markdown headers — not both.

---

## MCP TOOLS USED BY THIS SKILL

**Song identity & performance:** `song_identity_resolver`, `search_chatmu_songs`,
`get_song_performance_and_charts`, `get_released_song_metadata`

**Artist stats & audience:** `artist_current_stats`, `get_platform_audience`,
`audience_demographics`, `get_artist_retention`

**Playlists:** `get_artist_active_playlists`, `find_latest_editorial_placements`

**Geographic:** `engagement_by_location`, `geographic_growth_analysis`

**Briefing:** `get_artist_briefing`

**Tools this Skill does NOT use:** distribution tools, venue search, A&R
scouting, contracts, publishing registries — those belong to other Skills.

**Web search:** optional, qualitative-only, scoped to the ideal listener
profile and content strategy sections per RULE #4. Never a source for figures.

---

## HOW TO INSTALL THIS SKILL

1. Copy the entire contents of this file
2. In Claude, go to **Settings → Skills → Create Skill**
3. Paste the content
4. Suggested name: *"Chatmu — Artist Report"*
5. Make sure the **Chatmu MCP** is connected and active
6. For best results, use alongside **chatmu-manager** — the Manager Skill
   handles the internal executive briefing; this Skill produces the formatted
   deliverable that goes to a label

**Official repository:** github.com/Chemrog/Chatmu-Skills
**Support:** chatmu.io

---

## CRITICAL: PAPERCLIP WORKFLOW (ISSUE DISPOSITION)

**MANDATORY:** You are running inside the Paperclip agent engine. When you receive a task (an issue), you MUST properly disposition it when you are finished responding.
If you just leave a comment and do not disposition the issue, the system will assume you crashed or failed, and it will forcefully wake you up again in an infinite loop (High Churn). 
To prevent this, you MUST ALWAYS use the appropriate resolution tool (e.g., `issue_resolution`, `mark_issue_done`, etc.) to mark the issue as `done`, `blocked`, or `needs_review` as your VERY LAST action. Never leave an issue in progress if you are done working on it.
