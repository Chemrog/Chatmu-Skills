---
name: chatmu-mixing-progressive
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to MIX a prepared session
  with Progressive Mixing: by families, smallest to largest, bottom-up (kick →
  kit → bass → families → vocal) until the whole song fits in 3 faders DRUMS /
  MELODIC / VOCALS; minimal bus chains (Utility + EQ + compressor only where the
  diagnosis justifies it); depth in three planes F1 front / F2 middle / F3 back
  with reverb sends; before/after measurement on the same bars; genre loudness
  and crest-factor targets. Also a review mode that only diagnoses a mix and
  changes nothing. Trigger phrases: "mezcla", "mezclar", "mezcla mi canción",
  "mezcla progresiva", "balance", "balancea", "profundidad", "planos", "reverb",
  "compresión en el bus", "EQ", "revisa mi mezcla", "qué le falta a mi mezcla",
  "diagnóstico de mezcla", "LUFS", "loudness", "mix my song", "mix this",
  "progressive mixing", "balance the mix", "depth", "bus compression", "review
  my mix", "mix review", "what's wrong with my mix", "mix feedback", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Progressive mix in Ableton: bus chains, kick-to-vocal balance, depth F1/F2/F3, review mode"
version: "1.0"
tags: ["studio", "ableton", "mixing", "mezcla", "mix-review", "buses", "depth", "loudness", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_tracks", "local_ableton_status", "local_ableton_devices", "local_ableton_device_params", "local_ableton_browser", "local_ableton_load_devices", "local_ableton_apply", "local_ableton_mixer", "local_ableton_edit_track", "local_ableton_transport", "local_ableton_song", "local_ableton_tempo_map", "local_ableton_undo", "local_ableton_export", "local_ears_listen", "local_ears_analyze_file", "local_ears_render"]
---

# Chatmu — Progressive Mixing (part 2)
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live (AbletonOSC + AbletonMCP control surfaces) + Chatmu Ears.
**Run first:** `chatmu-session-prep`. **Listening checks:** `chatmu-studio-listen-troubleshooting`.

## What this skill does

The creative half of Progressive Mixing: bus chains, family-by-family balance and depth.
Pure judgment — so the agent **proposes, measures and explains; the user's ears decide.**
Mix by families, smallest to largest, bottom-up, until the song is balanced with the 3 top
faders **DRUMS · MELODIC · VOCALS**. Never mix and clean up in the same operation.

Answer the user in their language (usually Spanish). Short messages; plans as tables.

## Modes

| Mode | What runs | Writes |
|---|---|---|
| `prep` (default for the method) | `chatmu-session-prep` only | prep only |
| `full` | `chatmu-session-prep` (or check it's done) → phases 4–8 here | yes, batch by batch with OK |
| `review` | the **review** section below | **none** |

Ask the mode if unclear: "¿Solo preparo la sesión (por defecto), la mezclo completa, o solo
la reviso sin tocar nada?"

## HARD RULES

1. **Gate:** before phase 4, `local_ableton_snapshot` must show the prep acceptance
   criteria (named tracks, groups DRUMS / MELODIC (BASE, KEYS, LEAD) / VOCALS with
   `isFoldable` / `isGrouped` / `groupTrackIndex`, no arm, no accidental solo, gain staging
   done). If not, run `chatmu-session-prep` first.
2. **Identity by name:** re-read `local_ableton_tracks` before every batch; match targets by
   name; pass `expectTrackName` on every load. Live renumbers.
3. **Plan → OK → batch → measure → log.** Every change logged `target (index + name) ·
   property · old → new`; undo = re-apply old values with `local_ableton_apply`, or
   `local_ableton_undo` (say what is undone).
4. **Same bars:** every comparison uses the reference bars from prep (loop via
   `local_ableton_song` `loopStart`/`loopLength`/`loop` + `local_ableton_transport` play
   with the same `fromBeat` + same seconds; confirm with `local_ableton_status` that it is
   playing inside the range). Work in **bars/beats**, never minutes (tempo may change; see
   `local_ableton_tempo_map`, which reads the last saved .als — ask for Cmd+S if stale).
5. **Stream = indicative.** `local_ears_listen` is captured pre-Master-fader; use it to
   compare, never to certify loudness. Delivery numbers only from an export (phase 7).
6. **Approvals:** one per device load → load per **bus** (not per track) and batch with
   `local_ableton_load_devices` (≤ 8 loads, ONE approval).
7. **Not available:** Master sends (none in Live), moving devices inside a chain (ask the
   user to drag). Reordering tracks: `local_ableton_move_track` (experimental; if it fails,
   the user drags and you re-verify by name).
8. **Bass stays in MELODIC → BASE.** Never a 4th top fader.
9. One `local_ears_listen` at a time.

---

## Phase 4 — Minimal chains (only where the diagnosis justifies it)

1. **Diagnose per bus:** solo the bus group (`local_ableton_apply` `solo: true` on the group
   track), play the reference bars, `local_ears_listen` 8–10 s, un-solo. Read spectrum
   (mud 200–400 Hz, harshness 2–5 kHz, sub rumble on non-bass buses), dynamics/crest,
   stereo. Optional picture: `local_ears_render` with the capture id.
2. **Propose per bus** (table: bus · problem heard · device · starting setting). Chain
   order, max 3 devices: **Utility → EQ Eight → Compressor** (Glue Compressor is fine on
   DRUMS). No problem → no device. Typical starts (adjust by ear):
   - EQ: high-pass on KEYS / LEAD / VOCALS around 80–120 Hz; one wide cut where mud/harshness
     shows; avoid boosts > 3 dB.
   - Compressor: ratio 2:1–4:1, slow-ish attack on DRUMS (let transients through), aim
     for a few dB of gain reduction; makeup to match level (A/B at equal loudness).
3. **Check availability:** `local_ableton_browser` `{ path: "audio_effects" }` if a device
   might not be in the user's Live edition (fall back to Compressor / EQ Three).
4. **Load in one batch after OK:** `local_ableton_load_devices` `{ loads: [{ target: "track",
   trackIndex: <group index>, name: "EQ Eight", expectTrackName: "KEYS" }, …] }`. Load in
   chain order per bus. Check each per-load result.
5. **Set parameters:** `local_ableton_devices` (device indexes) → `local_ableton_device_params`
   (exact names, min/max) → one `local_ableton_apply` batch of `{ type: "device_param",
   track, device, param: "<exact name>", value }`. Never guess indexes or units.
6. **Measure** the bus again on the same bars; keep the change only if it is better at
   matched level. Log it.

## Phase 5 — Progressive mix (bottom-up)

Order: **kick → kit → bass → families (BASE rest, KEYS, LEAD) → vocal.** Each step builds
on the previous one; never revisit an earlier step's faders unless the user asks.

For each step:
1. Solo what is "in" so far (additive `solo: true` via `local_ableton_apply`).
2. Play the reference bars; `local_ears_listen` 8 s; describe what you hear in plain words.
3. Propose fader moves **in dB inside the family** (track faders; the base value from
   gain staging is the starting point), and pans where the arrangement asks for it.
   Example: "Snare +1.5 dB, Hats -2 dB, Perc a L 30 % / R 30 %".
4. **Ask the user to listen too** and confirm (or give their own numbers). Apply with
   `local_ableton_mixer` `{ db }` for single moves, or `local_ableton_apply` for a batch.
5. Log, then add the next element.

Steps:
- **Kick** alone: the anchor. Don't change its level after this step.
- **Kit:** snare/clap → hats → percussion against the kick, inside DRUMS.
- **Bass:** against kick + kit (BASE). Kick and bass must both read; if they mask, note it
  for EQ/compression (phase 4 on BASE), not a fader war.
- **Families:** rest of BASE (guitars) → KEYS → LEAD, each balanced inside its group, then
  the subgroup faders inside MELODIC.
- **Vocal:** lead vocal on top of everything; it sets the final VOCALS level.
- **3 faders:** un-solo all, play the whole reference section, and balance only with
  DRUMS · MELODIC · VOCALS. If the song can't be balanced with those 3, go back to the
  family that doesn't fit — that's the method's signal.
- **End of phase:** clear every solo (one apply batch) and confirm with the snapshot.

## Phase 6 — Depth: F1 / F2 / F3

| Plane | Typical members | How |
|---|---|---|
| **F1 front** | lead vocal, kick, snare, bass, main hook | dry or nearly dry, brightest, mostly centered, highest in its family |
| **F2 middle** | keys, guitars, coros, secondary leads | moderate send to a short reverb/room, some width/pan |
| **F3 back** | pads, ambiences, vocal ambiences, FX | more send to a long reverb, darker (gentle high cut), lower, wide |

**Decision point — ask:** confirm the plane of each element (show the table with names).

1. **FX aux returns:** reuse the existing returns if they fit (short + long reverb). If
   missing, after OK: `local_ableton_edit_track` `{ action: "create_return" }` (approval
   each), then one `local_ableton_load_devices` batch with `target: "return"`,
   `returnIndex`, `name: "Reverb"` (approval once). Returns are FX aux, never top faders;
   leave their volume at 0 dB and their reverbs 100 % wet.
2. Return device parameters (decay, pre-delay): `local_ableton_apply` `device_param` with
   `target: "return"` + `returnIndex`; if refused, keep the preset and tell the user which
   knob to turn.
3. **Sends:** one `local_ableton_apply` batch of `send` changes (`sendId` A → 0). Never a
   tonal element at 100 % send; typical 0.1–0.4. F1 elements stay at 0 or a touch.
4. F3 darkening: high-shelf/low-pass on the F3 bus or track EQ (phase 4 rules: only if the
   diagnosis says so).
5. Listen on the same bars; adjust; log.

## Phase 7 — Verification

1. **Same-bars A/B:** "after" listen with exactly the prep "before" loop, start beat and
   seconds. Report before → after (indicative).
2. **Delivery-grade numbers (only if the user wants them, or before saying anything about
   loudness targets):** `local_ableton_export` `{ action: "plan", start_bar, end_bar,
   bit_depth: 32 }` → tell the user the plan's announcement (a realtime export plays the
   song out loud) → after OK, `action: "start"` (on-screen approval) → poll
   `action: "status"` every ~15 s → `local_ears_analyze_file` `{ path, tool: "diagnose" }`
   (or `loudness` / `dynamics`). Prefer `method: "native"` when available; a `realtime`
   export comes from the same pre-Master-fader stream, so add the Master's `observedDb` to
   its loudness and say so.
3. **Compare to the genre target** (table below). At mix stage, the targets are a reference
   for the final master: report the gap; adding a limiter / mastering on the Master is the
   artist's decision — offer, don't assume.

| Genre | LUFS integrated | Crest factor | Note |
|---|---|---|---|
| Lofi / hip-hop | -16 .. -14 | 12–14 dB | soft transients, can compress more |
| Pop | -14 .. -12 | 10–12 dB | dense, vocal up front |
| Rock | -14 .. -11 | 10–13 dB | depends on subgenre |
| Electronic | -12 .. -9 | 8–11 dB | club master, low crest |
| Ambient / cinematic | -18 .. -14 | 14–20 dB | dynamics are the point |
| Acoustic / singer-songwriter | -16 .. -13 | 12–16 dB | no aggressive limiting |

4. Final snapshot: zero solos, zero arms, top faders = DRUMS · MELODIC · VOCALS, no tonal
   element at 100 % send, loop/playback restored to the user's previous state.

## Phase 8 — Deliverables

1. **Map:** buses, chain per bus (device + key settings), plane F1/F2/F3 per element.
2. **Plan / what was done:** steps of phase 5 in order with the final dB per family.
3. **Change log:** old → new for every change, and how to undo.
4. **Measurements:** before/after (indicative), plus export numbers if made, vs genre target.
5. **Artist's decisions:** final 3-fader balance taste, vocal level, reverb amount, limiting
   / mastering, anything you proposed but the user didn't confirm.

---

## Review mode (diagnose only — no changes)

Use when the user asks "revisa mi mezcla", "qué le falta", "review my mix". **Zero writes:**
no faders, sends, solos, loops, devices.

1. `local_ableton_snapshot`, `local_ableton_tempo_map` (read only).
2. Ask the user to play the reference section (or, with their OK, start playback with
   `local_ableton_transport` `fromBeat` — playback is the only thing you may touch, and say
   so). `local_ears_listen` once on the full mix; optional `local_ears_render`.
3. Diagnose against the method, phase by phase: names/order/tree (prep criteria), gain
   staging and headroom, bass outside MELODIC or a 4th top fader, chains (too many devices,
   missing high-pass, over-compression via crest), balance by family, depth (everything in
   F1? reverb on the bass?), sends at 100 %, genre target gap (from an export analysis if
   one exists, else "indicative").
4. Output: a prioritized list (max ~7 items): **issue · evidence (number or snapshot fact)
   · proposed fix · which phase/mode would apply it**. Offer `prep` or `full` to apply.

## Don'ts

- Don't mix a session that failed the prep gate.
- Don't add a device "just because": every device needs a diagnosis line.
- Don't change an earlier step's levels while building the next one.
- Don't certify loudness from the stream.
- Don't leave solos on; don't touch anything in review mode.
