---
name: chatmu-studio-sidechain
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to set up sidechain
  compression / pumping / ducking: a Compressor (or Glue Compressor) on the bass,
  pad, synth or bus with its "Audio From" set to the kick (Post FX), values per
  genre (house, EDM, techno, trap, reggaetón), alternatives without routing
  (Auto Pan / volume shaping, LFO 1/4 in Chatmu Synth), bass-under-kick
  ducking, and an Ears check that it really pumps (level drop on every hit).
  Trigger phrases: "ponle sidechain", "sidechain al bajo", "sidechain desde el
  kick", "que bombee", "bombeo", "que respire con el kick", "ducking", "que el
  bajo le deje espacio al kick", "compresor con sidechain", "Audio From",
  "sidechain from the kick", "pumping", "duck the bass", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Sidechain and pumping in Live: Compressor from the kick (Post FX), values by genre, verified with Ears"
version: "1.0"
tags: ["studio", "ableton", "sidechain", "pumping", "bombeo", "ducking", "compressor", "mixing", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_tracks", "local_ableton_devices", "local_ableton_load_devices", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_device_routing", "local_ableton_move_device", "local_ableton_lom", "local_ableton_apply", "local_ableton_undo", "local_ableton_transport", "local_ableton_song", "local_ableton_status", "local_ears_listen", "local_ears_render", "local_synth_list_params", "local_synth_modulate", "local_synth_unmodulate", "local_ableton_browser"]
---

# Chatmu Studio — Sidechain & pumping
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live 12 (AbletonMCP patched Remote Script 1.10.0-chatmu) + Chatmu Ears.
**Related:** `chatmu-mixing-progressive` (where it fits in the mix), `chatmu-studio-drop-buildup`, `chatmu-studio-synth`.

## What does this Skill do?

Makes one track duck when the kick hits — subtly (room for the kick) or as an effect (the
house/EDM "pump") — **without asking the user to click anything**, and proves with Ears
that it works.

Answer in the user's language (usually Spanish). Plan in one table, one OK.

## HARD RULES

1. **The sidechain IS controllable.** "Audio From" is Live 12's `Device.input_routings`:
   use `local_ableton_device_routing`. Never tell the user it "isn't exposed"; if something
   fails, `local_ableton_lom describe` the device and read the options first.
2. **Identity by name:** tracks and devices by their current names (`trackName`,
   `deviceName`, `expectTrackName`). Re-read after any structural change.
3. **Real units:** `local_ableton_device_params` first, then
   `local_ableton_set_device_param` with `display` ("-24 dB", "4:1", "1 ms", "150 ms").
   Report Live's `display_value`.
4. **Verify the routing by reading it back** (`verified: true` in the routing result, or a
   read-only `local_ableton_device_routing` call without `source`).
5. **Closed loop with Ears** (last phase): keep it only if it measurably ducks on the hits
   and the user likes it; otherwise `local_ableton_undo` the steps, say what was undone.

## Phase 0 — Recon

`local_ableton_snapshot` → the kick track (name, e.g. "Kick 909"), the target(s) (bass, pad,
stab, a bus), devices already on them (an existing Compressor can be reused), tempo.
Ask only what's missing: "¿bombeo marcado (efecto) o sutil (que el kick respire)?"

## Phase 1 — Values by genre (starting points)

One beat lasts `60000 / BPM` ms (124 BPM → 484 ms). The release decides the pump shape: the
level should come back just before the next kick.

| Genre / goal | Ratio | Attack | Release | Gain reduction on hits |
|---|---|---|---|---|
| House / deep house (pads, chords) | 4:1 – inf:1 | 0.1–1 ms | 30–45 % of a beat | 4–8 dB |
| EDM / big room / future bass (pump as effect) | inf:1 | 0.1 ms | ~50 % of a beat (≈ 1/8) | 8–15 dB |
| Techno (bass, rumble) | 4:1 – 10:1 | 0.1–1 ms | 80–150 ms | 2–5 dB (rumble: more) |
| Trap / hip-hop (808 under the kick) | 4:1 – 10:1 | 0.1 ms | 50–100 ms | 3–6 dB, ducking only |
| Reggaetón / pop (bass under the kick) | 3:1 – 4:1 | 1 ms | 60–120 ms | 2–4 dB, inaudible as pump |

Threshold: lower it until the gain reduction reaches the target on the hits (read it by ear
and Ears; Live's GR meter is not readable by the tools). Makeup: none for an effect pump;
match level for subtle ducking.

## Phase 2 — Set it up (one OK)

1. **Compressor:** reuse one on the target, or load it (`local_ableton_load_devices
   { loads: [{ trackIndex, name: "Compressor", expectTrackName }] }`, one approval for all
   targets). Put it where it belongs (usually after EQ, before reverb/delay) with
   `local_ableton_move_device` if needed. Glue Compressor works too (DRUMS/bus glue).
2. **Routing:** `local_ableton_device_routing { trackName: "<target>", deviceName:
   "Compressor", source: "<kick track>", tap: "Post FX" }` — it also switches "S/C On".
   Check `verified: true`. Post FX = the kick after its devices, before its fader, so the
   kick's fader/solo state doesn't change the trigger.
3. **Parameters:** `local_ableton_device_params` → set Ratio, Attack, Release, Threshold
   (and Makeup) with `local_ableton_set_device_param` `display`. Several at once on a track:
   `local_ableton_apply` with `device_param` changes.
4. **Several targets** (bass + pads + stabs): same compressor settings per role, or one
   sidechained bus (route them to a group and compress the group) — fewer devices.

### Ghost kick (trigger without hearing it)

If the trigger must keep going where the audible kick stops (breaks): a track with a kick
clip playing every beat, fader at −inf, and the sidechain source = that track with
`tap: "Post FX"` (taken before the fader).

## Phase 3 — Alternatives without routing

| Route | When | How |
|---|---|---|
| Auto Pan / tremolo shape | quick pump on one track, no trigger needed | load the device (find its exact name with `local_ableton_browser` — it varies by Live version), amount 100 %, synced to 1/4, phase 0°; read its params first |
| Volume shaper in Chatmu Synth | the sound comes from Chatmu Synth | `local_synth_list_params { filter: "lfo_1" }`, then `local_synth_modulate { source: "lfo_1", destination: <the synth's volume/level param from list_params>, amount: -0.3 }`, LFO synced to 1/4 with a ramp shape. Never guess the destination name. |
| Bass ducking under the kick only | 808/bass and kick play together | the Compressor route with the trap/reggaetón row (subtle) |

## Phase 4 — Ears verification (does it really pump?)

1. Loop 4–8 bars where kick and target play (`local_ableton_song` loopStart/loopLength/loop,
   note the old loop), solo the **target** only (`local_ableton_apply` solo — the Post FX
   trigger still works), play from the loop start.
2. **A/B on the same bars:** `local_ears_listen { seconds: 8 }` with the compressor ON, then
   `local_ableton_set_device_param { …, on: false }` and listen again OFF, then back ON.
3. It pumps if, with ON vs OFF: integrated level drops by roughly the intended average
   reduction, the crest factor/short-term variation goes up, and the waveform shows dips on
   every beat (`local_ears_render { captureId, view: "waveform" }`; the
   `"modulation_spectrum"` view shows a peak at BPM/60 Hz, e.g. 2.07 Hz at 124 BPM).
4. Restore solo, loop and playback. Report: "pide −8 dB en cada golpe → medido: el pad baja
   ~6 dB en cada kick (ON vs OFF −3.1 LU)".
5. No dips → check `verified`, S/C On, the kick actually plays in that range, threshold too
   high. Fix once and re-measure; otherwise undo and say what you found.

If you can't listen (nothing playing, Ears unavailable — `chatmu-studio-listen-troubleshooting`)
or can't see the render, say **"configurado, no verificado"** and give the settings Live read
back.

## Don'ts

- Don't ask the user to pick "Audio From" by hand before trying the routing tool.
- Don't use a compressor's GR meter you can't read as proof; use the Ears A/B.
- Don't leave tracks soloed or the loop changed.
