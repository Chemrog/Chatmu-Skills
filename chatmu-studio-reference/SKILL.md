---
name: chatmu-studio-reference
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) when the user gives a song
  they like and wants to know how their mix compares: both files measured with
  Chatmu Ears and compared at matched loudness — tonal balance by band (sub,
  lows, low-mids, mids, presence, air), stereo width, dynamics and loudness —
  then 3–5 differences in producer words ("tu mezcla tiene 4 dB menos de aire
  arriba de 10 kHz") and which track or bus to look at. The reference file
  never leaves the user's Mac. Also the tonal target for chatmu-mixing-progressive.
  Trigger phrases: "compárala con esta canción", "compara mi mezcla con",
  "quiero que suene como", "que suene como esta", "referencia", "canción de
  referencia", "track de referencia", "¿qué le falta comparada con…?", "¿por
  qué la mía suena más apagada?", "¿por qué suena más chica?", "A/B con
  referencia", "compare with this song", "reference track", "make it sound
  like", "mix reference", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Compare your mix with a reference song at matched loudness: bands, width, dynamics, 3-5 concrete fixes"
version: "1.0"
tags: ["studio", "ableton", "reference", "referencia", "mixing", "mezcla", "tonal-balance", "loudness", "co-producer"]
requiresTools: ["local_ears_analyze_file", "local_ears_render", "local_ears_listen", "local_ableton_export", "local_ableton_snapshot", "local_ableton_status", "local_list_access"]
---

# Chatmu Studio — Reference track comparison
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Ears (+ Ableton Live to export the user's mix).
**Used by:** `chatmu-mixing-progressive` (tonal target in phase 7), `chatmu-master-check`. **Export:** `chatmu-studio-export`.

## What does this Skill do?

"Quiero que suene como esta" → measure both songs the same way, **turn them to the same
loudness**, and say what really differs, in a few lines a producer would act on. Louder
always sounds "better", so comparing without matching loudness is lying.

Answer in the user's language (usually Spanish). Max 5 differences.

## HARD RULES

1. **Match loudness first (Ears rule 5).** Compare band levels, width and dynamics only
   after removing the integrated-LUFS difference. Report the loudness gap separately.
2. **Files, not the stream.** Both sides measured with `local_ears_analyze_file` on files.
   The user's mix: an export (`chatmu-studio-export`, 24/32-bit WAV). The reference: the
   file the user gives (wav, aiff, flac, mp3, m4a — mp3/m4a are converted locally).
3. **Equivalent material.** Chorus vs chorus beats whole song vs whole song. If you only
   have whole files, say the comparison includes intros/breaks and is approximate.
4. **The reference stays on the Mac.** Ears runs locally; never upload it anywhere, never
   ask for a streaming link to "download" it.
5. **Differences are not orders.** The reference is a direction, not a target to copy;
   genre and arrangement differences are legitimate. Say "si quieres acercarte…".
6. **3–5 differences, biggest first,** each with a number, a cause and where to act.

## Phase 0 — Get the two files

| Side | How |
|---|---|
| Reference | the file they attach / name (Descargas…). Ungranted folder → the app asks once ("acepta el permiso para leer esa carpeta"). If they only have a link to a streaming service, ask for the file (they own a copy, or a purchased download). |
| Their mix | a recent export of the same section, or export it now: `local_ableton_export` `plan` → OK → `start` → `status` (see `chatmu-studio-export`). Prefer the section that matches the reference's chorus/drop (`start_bar` / `end_bar`, from `local_ableton_snapshot` + the user). |

Ask once: "¿Qué parte de tu canción corresponde al coro de la referencia?" If the user
doesn't know, use the densest 8–16 bars of their song and the whole reference (rule 3).

## Phase 1 — Measure both (same tools, same order)

For each file:
1. `local_ears_analyze_file { path, tool: "loudness" }` → `integrated_lufs`,
   `true_peak_dbtp`, `loudness_range_lu`.
2. `local_ears_analyze_file { path, tool: "spectrum" }` → band levels (Ears bands: sub
   20–60 Hz, bass 60–120, low_mid 120–300, mid 300–800, high_mid 800–2.5k, presence
   2.5–5k, brilliance 5–10k, air 10–20k).
3. `local_ears_analyze_file { path, tool: "stereo" }` → width / correlation (and per band
   if present).
4. `local_ears_analyze_file { path, tool: "dynamics" }` → crest factor.
5. Optional picture: `local_ears_render { captureId, view: "spectrum_curve" }` for each.

## Phase 2 — Compare at matched loudness

1. `offset = LUFS_ref − LUFS_mix`. Report it alone: "la referencia está 3.2 dB más fuerte"
   (that is a mastering question, `chatmu-master-chain`).
2. For each band: `delta = band_mix − band_ref` (both already at −18 LUFS, see Phase 1).
   Only if a result does NOT carry that normalization, add the offset first
   (`band_mix + offset`) — never apply it twice.
3. Width: correlation / width difference, overall and in the low end (a wide low end in
   the mix vs a mono one in the reference is a real finding).
4. Dynamics: crest-factor difference (more than ~3 dB = audibly more/less punch).
5. Ignore deltas under ~1.5 dB in one band: that is noise between songs.

## Phase 3 — Report (producer words)

Table, then 3–5 lines:

| Banda | Tu mezcla vs referencia (a igual volumen) |
|---|---|
| sub 20–60 | +1.0 dB |
| low_mid 120–300 | **+3.5 dB** |
| presence 2.5–5k | −1.2 dB |
| air 10–20k | **−4.1 dB** |

1. "Tienes 3.5 dB de más entre 120 y 300 Hz: suena más turbia. Revisa el bus MELODIC
   (pads y guitarras) antes que la voz."
2. "Te faltan 4 dB de aire arriba de 10 kHz: un shelf suave en VOCALS y en el bus de
   platillos, no en el máster."
3. "Tu crest factor es 4 dB menor: la referencia respira más; menos limitador."

Where to act — map each band to the usual suspects (from the session's snapshot names):
sub/low → kick, bass/808 (BASE); low_mid → pads, guitars, piano, vocal body; mid/high_mid
→ snare, vocals, leads, guitars; presence → vocal, snare, hats; brilliance/air → hats,
cymbals, vocal air, reverbs. Name tracks/buses from the user's session, not generic ones.

Offer next steps: apply with `chatmu-mixing-progressive` (bus EQ, closed loop) or
`chatmu-master-chain` (loudness / overall tilt).

## Ears verification

Every number above comes from `local_ears_analyze_file`. After a change made because of
this comparison, export the same range again and repeat Phase 1–2 on the new file: report
"aire: −4.1 → −1.3 dB". If a file could not be analyzed, say **"no verificado"** for that
side and don't invent the comparison.

## Don'ts

- Don't compare without matching loudness.
- Don't compare a stream capture against a file.
- Don't upload or share the reference.
- Don't list ten differences; three good ones are better.
