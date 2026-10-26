---
name: chatmu-master-chain
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to build or adjust the
  mastering chain on Live's Master track: gentle EQ, glue compression, optional
  width/bass mono, optional saturation and a limiter with a −1 dBTP ceiling,
  aiming at the genre's competitive loudness (or a reference song the user
  likes), not at −14 LUFS (that is the streaming playback level). Sets every
  parameter in real units (dB, ms, :1), keeps the Co-Producer Audio plugin
  last, and verifies each step on an exported WAV with chatmu-master-check.
  Trigger phrases: "masterízala", "masteriza mi canción", "hazme el máster",
  "cadena de máster", "pon un limitador en el master", "limitador", "súbele
  volumen al master", "que suene más fuerte", "que llegue a -14 LUFS", "glue",
  "compresor en el master", "master para Spotify", "master para el club",
  "mastering chain", "master my song", "limiter on the master", "make it
  louder", "LUFS target", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Mastering chain on Live's Master: EQ, glue, limiter to a LUFS target, verified on the exported WAV"
version: "1.1"
tags: ["studio", "ableton", "master", "mastering", "limiter", "limitador", "loudness", "lufs", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_status", "local_ableton_browser", "local_ableton_load_devices", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_move_device", "local_ableton_mixer", "local_ableton_lom", "local_ableton_undo", "local_ableton_export", "local_ears_analyze_file", "local_ears_listen", "local_ears_ensure_plugin"]
---

# Chatmu Studio — Master chain
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live (AbletonMCP patched Remote Script 1.10.0-chatmu for real units and Master devices) + Chatmu Ears.
**Pairs with:** `chatmu-master-check` (the chain does, the check verifies). **Before:** `chatmu-mixing-progressive` (a master can't fix a mix). **Export:** `chatmu-studio-export`.

## What does this Skill do?

Puts a short, honest mastering chain on Live's Master and reaches a loudness target
without wrecking the mix. Every move is in real units, read back from Live, and judged on
an **exported file**, never on the stream.

Answer in the user's language (usually Spanish). Plans as tables; one OK per batch.

## HARD RULES

1. **The Co-Producer Audio plugin stays LAST on the Master.** Ears and the realtime export
   hear the signal at the plugin's position. A limiter loaded after it is invisible to
   them. After every load on the Master, re-read the chain (`local_ableton_snapshot`) and,
   if needed, `local_ableton_move_device { action: "move", target: "master", deviceName:
   "Co-Producer Audio", expectName: "Co-Producer Audio" }` (no `position` = last).
2. **Master fader at 0 dB** while a master chain is on (school A leaves it at −10 dB:
   the fader comes after the limiter and would just turn the master down). Say it and set
   it with `local_ableton_mixer { target: "master", property: "volume", db: 0 }`.
3. **Read before you write.** `local_ableton_device_params { target: "master", deviceName }`
   first: exact names, ranges, `display_value`, `value_items`. Then
   `local_ableton_set_device_param { target: "master", deviceName, param, display }` in real
   units ("-1 dB", "2:1", "30 ms"). Answer with the `display_value` Live returned ("pedí
   −1 dB → quedó −1.0 dB"). Never guess a parameter name or an internal value.
4. **Closed loop:** measure → change one thing → measure the same range → keep it only if
   the number improved AND the user likes it; otherwise `local_ableton_undo` (one undo per
   write) and say what was undone.
5. **Delivery numbers only from a file:** export the reference range (or the whole song)
   with `local_ableton_export` `bit_depth: 32` and measure it with
   `local_ears_analyze_file`. The stream (`local_ears_listen`) is only for quick A/B.
6. **Gentle by default:** EQ moves ≤ 2 dB, glue 1–3 dB of gain reduction, limiter 2–6 dB
   of gain. If it needs more, the problem is in the mix: send it back to
   `chatmu-mixing-progressive` and say why.
7. **Never say a Live feature "is not exposed"** without `local_ableton_lom describe` on
   the object first (e.g. a Limiter option that isn't a parameter).
8. **Approvals:** loading devices needs an on-screen approval → load the whole chain in ONE
   `local_ableton_load_devices` call (≤ 8 loads, `target: "master"`).
9. **Compare at matched loudness.** Louder always sounds better. When you A/B the master vs
   the mix, or vs a reference, state both LUFS and judge after matching them (turn the louder
   one down by the difference); never present "it's louder" as "it's better".

---

## Phase 0 — Recon (read only)

1. `local_ableton_snapshot` → Master chain (devices and order), Master fader (dB), track
   faders, is the mix clipping anywhere obvious.
2. `local_ears_ensure_plugin { install: false }` → Co-Producer Audio on the Master?
3. **Pick the loudness target** (say it to the user in one line):
   - **−14 LUFS is NOT a mastering target.** It is the level Spotify/YouTube *play* at:
     louder masters are turned down, quieter ones (Spotify) up. A master at −14 sounds
     quiet next to commercial releases in playlists, DJ sets, SoundCloud, TikTok/IG and
     anywhere without normalization. Measured commercial masters: median about −10.6 LUFS,
     ~80 % louder than −14; Grammy 2026 nominees up to −6.5 (Bad Bunny "DtMF" −8.0).
   - **Default = competitive for the genre** (integrated LUFS of the whole song):

     | Genre | Target | Min crest factor |
     |---|---|---|
     | Lo-fi, jazz, acoustic, regional/bolero, ballad, cinematic | −13 .. −11 | 9 dB |
     | Pop, R&B, indie, rock | −10 .. −8 | 8 dB |
     | Hip-hop, trap, drill | −9 .. −7 | 7 dB |
     | Reggaetón, urbano latino, dembow, cumbia moderna | −8 .. −6 | 6 dB |
     | EDM, house, techno (club) | −8 .. −6 | 6 dB |
   - **Better than the table: a reference.** If the user names or gives a song they want to
     sound like (`local_ears_analyze_file` on it), target its integrated LUFS ±1 LU and its
     crest factor, and A/B at matched loudness (rule 9).
   - **Ceiling** −1.0 dBTP always for streaming (lossy encoders create overs); −0.5 for club
     masters only if the user asks.
   - The **crest factor floor** wins over the LUFS target: if the limiter would push the crest
     below the floor, stop there and say "llega a −9 LUFS sin aplastarse; más fuerte pierde
     golpe" (louder masters lose about 2 dB of crest on average).
4. **Before** numbers: if a recent export exists, `chatmu-master-check` on it; otherwise
   export the densest 8–16 bars (chorus/drop) at 32-bit and measure (rule 5).

## Phase 1 — Plan the chain (table, then OK)

| # | Device | Why | Starting point (adjust by ear and by numbers) |
|---|---|---|---|
| 1 | EQ Eight | only if the diagnosis shows it | high-pass 20–30 Hz ("Low Cut 48" at 25 Hz) if there is sub rumble; ±1–2 dB wide shelves for tilt |
| 2 | Glue Compressor | glue, not loudness | ratio 2, attack 10–30 ms, release Auto, threshold for 1–2 dB of reduction, makeup to match |
| 3 | Utility | optional | Bass Mono on (~120 Hz) if the low end is wide; width ≤ 110 % |
| 4 | Saturator | optional density | soft-clip / analog, drive 1–3 dB, output compensated, Dry/Wet 30–60 %: adds perceived loudness and eases the limiter |
| 5 | Limiter | loudness + ceiling | ceiling −1 dB true peak, gain up until the target, release auto / short; if it needs > 6 dB, split it: 2–3 dB on a clipper/saturator + the rest on the limiter |
| last | Co-Producer Audio | Ears + realtime export | must stay last (rule 1) |

- No problem in the diagnosis → skip that device. A master chain can be just the Limiter.
- If the user already has a mastering plugin/chain: read it (`local_ableton_device_params`
  or `local_ableton_lom describe`) and adjust that instead of stacking a second one.
- Device availability by Live edition: `local_ableton_browser { path: "audio_effects" }`.

## Phase 2 — Load and order

1. After OK: `local_ableton_load_devices { loads: [{ target: "master", name: "EQ Eight" },
   { target: "master", name: "Glue Compressor" }, { target: "master", name: "Limiter" }] }`
   (one approval).
2. `local_ableton_snapshot` → Master chain order. Fix it with `local_ableton_move_device`
   (`position` = index in the chain as it is before the move) and put Co-Producer Audio
   last (rule 1).
3. Master fader to 0 dB (rule 2).

## Phase 3 — Set it in real units (one device at a time)

For each device: `local_ableton_device_params` → set the few parameters you planned with
`local_ableton_set_device_param` (`display`), report what Live read back. Typical names
(always confirm with the read): EQ Eight `1 Filter Type A`, `1 Frequency A`, `1 Gain A`;
Glue Compressor `Threshold`, `Ratio`, `Attack`, `Release`, `Makeup`; Limiter `Gain`,
`Ceiling`, `Release` (newer Live versions add more options: use what the read shows).

## Phase 4 — Reach the target (closed loop)

1. Export the same reference range at 32-bit (`chatmu-studio-export` flow: plan → OK →
   start → status) and `local_ears_analyze_file { tool: "loudness" }` + `"dynamics"`.
2. Distance to target: `target − integrated_lufs`. Move the Limiter `Gain` by that amount
   (in ≤ 2 dB steps when the crest factor is already low).
3. Re-export the same range, measure. Keep or `local_ableton_undo`.
4. Stop when: within ±0.5 LU of the target (or of the reference), true peak ≤ −1 dBTP, and
   the crest factor is at or above the genre floor (Phase 0 table). If the target needs more than ~6 dB of
   limiter gain, stop and tell the user the mix needs work first (rule 6).
5. Quick A/B by ear (optional): play the same bars, `local_ears_listen` with the Limiter on
   and off (`local_ableton_set_device_param { target: "master", deviceName: "Limiter",
   on: false }`), matched by loudness in your report; ask the user which they prefer.

## Phase 5 — Ears verification and hand-off

1. Export the **whole song** (`chatmu-studio-export`, 24-bit for delivery or 32-bit to keep
   working) and run **`chatmu-master-check`** on it. Its verdict is the result of this
   skill.
2. Report: chain (device · key settings as Live shows them), before → after (LUFS, true
   peak, crest), and the check's verdict.
3. Change log (`device · param · old → new`) and how to undo (`local_ableton_undo`, one
   step per write, or set the old values).

If you could not export or Ears could not analyze the file: say **"no verificado"** and
give only the settings you applied, never a loudness claim.

## Don'ts

- Don't load the limiter after Co-Producer Audio and then trust the export.
- Don't chase loudness past the point where the crest factor collapses.
- Don't EQ the master to fix one instrument: fix the track.
- Don't claim LUFS from the stream.
