---
name: chatmu-artist-report
description: >
  Genera reportes de artista para Chatmu — semanales, mensuales o de seguimiento
  de lanzamiento (single, EP o álbum) — con el formato Pro Indie Music / Chatmu:
  mitad diagnóstico de datos, mitad estrategia de contenido accionable.
  Úsala siempre que el manager pida "reporte semanal", "reporte mensual",
  "reporte de lanzamiento", "actualización de" una canción o artista, "cómo va"
  un single, o un update de performance para cualquier artista que gestiona.
  También úsala si pide un reporte con este formato o cualquier variante de ese
  estilo.
  Trigger phrases: "reporte semanal", "reporte mensual", "reporte de lanzamiento",
  "actualización de", "cómo va", "update de".
compatibility: claude.ai
---

# Chatmu — Artist Report Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP (100+ tools)
**For:** Managers que preparan entregables de performance para disqueras (Pro Indie Music / Chatmu)
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

Produces artist performance reports in the Chatmu / Pro Indie Music style: half
data diagnostic, half actionable content strategy. The reference format is
documented in `references/report-template.md`.

Every report is a **deliverable** — plain text or simple Markdown, in Spanish, ready
to copy/paste or hand to a document. Not an interactive dashboard, not a chat
summary. This is what a manager sends to a label.

---

## RULE #1 — Never invent figures

All streaming, audience, playlist, and demographic numbers MUST come from the
Chatmu MCP tools. If a data point is not available in Chatmu, say so explicitly
in the report ("dato no disponible en esta plataforma") instead of filling it in.

Web search (see RULE #4) is for qualitative context only, never for numbers.

---

## RULE #2 — Pick the right variant

| Tipo | Cuándo | Foco |
|------|--------|------|
| **Semanal** | Seguimiento continuo de un single ya lanzado, o de un artista en campaña activa | Tendencia de streams día a día, cambios en fuentes de descubrimiento, qué contenido publicar esta semana |
| **Mensual** | Corte de mes, comparación contra el mes anterior, revisión de varios lanzamientos o del catálogo | Crecimiento acumulado, comparación MoM, salud general del artista (todas las plataformas), prioridades del próximo mes |
| **Por lanzamiento** | Primeros 7/14/30 días de un single, EP o álbum nuevo | Impulso inicial vs. caída, conversión de audiencia propia, decisión de "reforzar / dejar correr / pivotar" |

If the manager doesn't specify, ask only if it's ambiguous between the three. Rules of
thumb:
- Mentions a date range or "esta semana" → **Semanal**
- Says "el mes" or asks to compare months → **Mensual**
- The song came out ≤30 days ago → **Por lanzamiento**

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

Web search complements the MCP in exactly two sections of the report, and nowhere
else:

1. **Perfil del oyente ideal (Section 9)** — to enrich "estética visual con la que
   conecta", "motivación principal", and "intereses fuera de la música" with current,
   concrete references for that demographic (brands, visual trends, platforms,
   cultural touchpoints). The MCP gives the demographic skeleton; web gives the
   cultural flesh.
2. **Estrategia recomendada (Section 7)** — to check which vertical formats, hooks,
   and narrative tones are currently performing on TikTok/Reels for that niche. This
   changes fast and web keeps it fresh.

**Hard limits:**
- NEVER use web search for streaming counts, listener counts, playlist counts,
  chart positions, retention rates, or any metric. Those are MCP-only.
- NEVER blend a web-sourced figure into the report as if it were Chatmu data.
- If web search is not available, fall back to Claude's reasoning over the MCP
  demographic data. The report still works without it.
- When you do use web context, keep it implicit in the recommendations — don't
  cite URLs or "según internet" in the deliverable. The report reads as one voice.

---

## STEP 1 — Gather the data

Follow RULE #3. Pull what you need for the chosen variant. Don't pull everything
if the variant doesn't require it (a weekly report doesn't need a full catalog
audit).

If a datum isn't available in Chatmu, say so in the report rather than filling it.

---

## STEP 2 — Calculate derived metrics

These almost always have to be computed by hand from the raw data:

- **Reproducciones por oyente** = streams / listeners. ~1.0 indicates drive-by
  listening, not recurring fans.
- **Tasa de guardado** = guardados / streams (×100). Reference: >8% is a good
  affinity signal.
- **% de streams por fuente** = algorithmic / editorial / own catalog / other
  (should sum to ~100%).
- **% de audiencia que ya escuchó el lanzamiento** = track listeners / artist's
  Active Listeners (and the same against Super Listeners). This is the key
  indicator of own-audience conversion — the metric a label cares about most.
- **Tendencia diaria** = streams/day at the start vs. streams/day now, to detect
  whether momentum is holding or falling.

---

## STEP 3 — Write the report

Follow this structure and tone (direct, Spanish, no filler, figures first then a
one-sentence interpretation):

1. **Encabezado:** "Reporte de [Semanal/Mensual/Lanzamiento] – '[Canción/Artista]'
   | [Artista]" + fecha de corte.
2. **Resumen de streams/oyentes:** total figure for the period + what the
   reproducciones/oyente ratio means.
3. **Guardados:** figure + save rate + affinity interpretation.
4. **Fuentes de reproducción:** % breakdown algorithmic / editorial / catalog /
   other, and how dependent it is on external discovery vs. own audience.
5. **Audiencia del artista:** total Active Listeners and Super Listeners, and
   how many / what % of each already heard the release. This is the section
   This is the section the manager cares about most — always include it
   even if the report is general catalog; it's the metric a label cares
   about most.
6. **Tendencia:** streams/day at the start of the period vs. streams/day now (or
   MoM comparison if it's a monthly report).
7. **Estrategia recomendada:** 3-6 concrete, actionable organic content
   recommendations — not generic. They must be anchored to the ideal listener
   profile (see STEP 4): format, duration, frequency, who appears on camera,
   narrative tone. If something isn't working (e.g. third-party content, a
   specific format), say it directly. This is one of the two sections where web
   context may inform the recommendations (RULE #4).
8. **Conclusión:** 3-4 lines connecting data with strategy — what's working,
   what isn't, and the next step.
9. **Perfil del oyente ideal:** age, NSE, location, main motivation
   (self-expression, entertainment, etc.), visual aesthetic they connect with,
   platform/device of consumption, interests outside music. This section barely
   changes between reports for the same artist — reuse it if it already exists
   from a previous report, only update it when there's new demographic data.
   This is the other section where web context may enrich the qualitative
   profile (RULE #4).

---

## Differences by report type

**Semanal:**
- May omit or summarize the ideal listener profile section if it was sent
  recently; focus the report on "what to publish this week".

**Mensual:**
- Add a table or paragraph comparing the current month vs. the previous one
  (total streams, audience growth, new playlists gained/lost).
- If there were several releases in the month, summarize each in 2-3 lines
  before going into detail on the most relevant one.

**Por lanzamiento:**
- Add a timeline of the initial push (day 1, day 7, day 14, day 30 if applicable).
- End with an explicit decision recommendation: reinforce with more content,
  let it run organically, or pivot the strategy because there's no traction.

---

## Delivery format

- Plain text or simple Markdown, in Spanish, ready to copy/paste or hand to a
  document.
- If the manager explicitly asks for a PDF or Word, use the corresponding docx or pdf
  skill after the final content is ready.
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

**Tools this Skill does NOT use:** distribution tools, venue search, A&R scouting,
contracts, publishing registries — those belong to other Skills.

**Web search:** optional, qualitative-only, scoped to the ideal listener profile
and content strategy sections per RULE #4. Never a source for figures.

---

## HOW TO INSTALL THIS SKILL

1. Copy the entire contents of this file
2. In Claude, go to **Settings → Skills → Create Skill**
3. Paste the content
4. Suggested name: *"Chatmu — Artist Report"*
5. Make sure the **Chatmu MCP** is connected and active
6. For best results, use alongside **chatmu-manager** — the Manager Skill handles
   the internal executive briefing; this Skill produces the formatted deliverable
   that goes to a label

**Official repository:** github.com/Chemrog/Chatmu-Skills
**Support:** chatmu.io
