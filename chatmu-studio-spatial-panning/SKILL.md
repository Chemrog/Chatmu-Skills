---
name: chatmu-studio-spatial-panning
description: >
  Places every element in the stereo field and in depth (front-to-back) in
  Ableton Live: panning, LCR/opposition, reverb sends, pre-delay and 5 depth
  planes, with mono compatibility. Trigger phrases: "panning", "pan", "stereo
  image", "width", "depth", "space", "reverb", "planes", "mono", "mix sounds flat".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Panning, depth planes and reverb sends that survive mono"
version: "1.0"
tags: [studio, ableton, mixing, panning, stereo, depth, reverb]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_load_device
  - local_ears_listen
  - local_ableton_mixer
  - local_ableton_apply
  - local_ableton_devices
  - local_ableton_set_device_param
  - local_ableton_fire
---

# Chatmu Studio — Space & panning

**Reference:** the tables and decision tree are at the end of this skill.
**Related:** `chatmu-mixing-progressive`, `chatmu-studio-listen-troubleshooting`.

## When to use
When a mix sounds flat, crowded, too wide, too narrow, or an element disappears in mono.
Not for EQ/compression problems; those go to `chatmu-mix-eq` / `chatmu-mix-compression`.

## Workflow

1. **Read the session:** `local_ableton_snapshot` and `local_ableton_tracks` (indexes, names,
   current pan/volume/sends).
2. **Classify into planes** (Reference table): 1 lead/kick/snare/bass, 2 main instruments,
   3 rhythmic/harmonic bed, 4 pads/ambience, 5 FX.
3. **Center the core:** kick, snare, bass, lead vocal at pan 0. Do not move them to fix
   a frequency problem.
4. **Pan the rest by opposition:** if a main element goes left, put a comparable one right.
   Prefer discrete positions (L/C/R or 40/40, 70/70) over random soft pans.
5. **Set depth:** more reverb and less top-end for farther planes; less reverb and sharper
   transients for closer ones. Reverb as send, 100% wet, post-fader.
6. **Write the moves** with `local_ableton_apply` in one batch (`type: "mixer"`,
   `property: "panning" | "volume" | "send"`).
7. **Mono check:** load Utility on the Master (`local_ableton_load_device`), set its Width to 0 with `local_ableton_set_device_param`, listen with `local_ears_listen` (stereo correlation too), then set Width back to 100%. Confirm nothing important disappears.
8. **Report** the plane map and what changed, then let the user listen.

## Hard rules
- Kick, snare, bass and lead vocal stay centered.
- Never hard-pan an element that must survive one-sided playback unless it has an opposite.
- Reverb must be a send, 100% wet, post-fader. No dry/wet insert for shared reverb.
- High-pass the reverb return (200–400 Hz) unless the genre wants wash.
- Depth is contrast: if everything has reverb, nothing is in front.
- Check mono before declaring the panning done.
- Do not use a stereo widener to fake width that the arrangement does not have.

## Output
A short map: element → plane → pan → send. Then the list of mixer changes applied.
If something cannot be verified (no Ableton control), say so and give the exact values
for the user to set manually.

## Reference


### What it solves
Place every element in space: left-right (panning), front-back (depth) and size (width).
Prevents flat, muddy mixes that fall apart in mono.

### Numbers

### The 4 dimensions (iZotope)
| Dimension | Control | Axis |
|---|---|---|
| Level | fader | up/down |
| Tone | EQ | up/down |
| Width | pan | left/right |
| Depth | reverb/delay | front/back |

### Panning
| Rule | Value |
|---|---|
| Mandatory center | kick, snare, bass, lead vocal |
| Hard pan | −3 dB in mono; may disappear in one earbud |
| Opposition | if something important goes left, something comparable goes right |
| Layered vocals | pairs 40/40, 50/50, 70/70, 80/80, 90/90, 100/100 |
| Pan law | 6 dB (mono), 3 dB (stereo), 4.5 dB (compromise) |

### Reverb
| Rule | Value |
|---|---|
| Setup | send–return, 100% wet, post-fader send |
| Blend | the first ~0.5 s does the blending work |
| High-pass | 200–400 Hz to avoid mud (common practice) |
| Pre-delay | separates source from tail; more pre-delay = closer |
| Uses | blend, size, tone, spread |

### Depth-plane model (working model, medium confidence)
| Plane | Elements | Level | Reverb | Tone | Width |
|---|---|---|---|---|---|
| 1 (front) | lead vocal, kick, snare, bass | high | almost none | bright | center |
| 2 | main instruments | medium | little | neutral | 30–60% |
| 3 | rhythmic/harmonic bed | medium-low | medium | darker | opposite to plane 2 |
| 4 | pads/ambience | low | long | dark | wide |
| 5 (back) | FX, textures | very low | very wet | filtered | extremes |

Depth cues, strongest first: **level → attack/transient → air (highs) → reverb amount →
pre-delay → width**. If two elements compete, separate them first by level and frequency;
panning is the last resort.

### Principles
1. The center is for what must survive mono and one-sided listening.
2. Width comes from opposition, not from piling everything at the extremes.
3. Depth comes from contrast: if everything has reverb, nothing is behind.
4. A short reverb blends; a long reverb creates ambience. They are not the same tool.
5. Pre-delay moves a source closer or farther more than decay does.
6. Always check mono: if an element disappears, the panning is wrong.
7. Fewer wide elements = more perceived width.

### Decision tree
```
Mix sounds flat?          → contrast levels + short reverb on planes 2–4
Muddy?                    → high-pass the reverb, shorten decay, lower sends
Vocal unclear?            → center, dry, compression, reverb ducking
Wide but weak?            → check opposition and correlation; mono the bass
Two elements compete?     → oppose panning or separate in frequency/time
Everything sounds far?    → lower global reverb and bring planes 1–2 forward
Everything sounds close?  → raise pre-delay and sends on planes 3–5
```

### By genre
| Genre | Panning | Depth |
|---|---|---|
| Pop | vocal/kick/snare center; doubles at extremes | short reverb, occasional delay |
| Reggaetón/trap | voice center; wide ad-libs; 808 center | little reverb, more delay |
| House/techno | kick/bass center; hats and percussion wide | short reverb, rhythmic delays |
| Lo-fi | everything closer and warmer | medium reverb, filtered |
| Rock | wide drums; opposing guitars | room reverb, short tail |
| R&B | vocal center, wide backing vocals | medium-long reverb, delay |

### Common errors
- Hard-panning important elements: they disappear in mono.
- Reverb on an insert with dry/wet: it changes the track level.
- Reverb without a high-pass: mud in the low mids.
- Everything centered (flat) or everything wide (diffuse).
- Confusing width with depth.
- Not checking mono.
- Using the same reverb to blend and to create ambience.

### How it is validated
- **Ears `listen_stereo`**: correlation, width, balance. Very low correlation = check phase.
- **Mono check**: sum to mono; nothing important should disappear.
- **A/B against a genre reference.**
- **Panning widget** (pending): show the 5 planes and each track's position.

### Checklist
- [ ] Are kick, snare, bass and lead centered?
- [ ] Does every element on one side have opposition?
- [ ] Is the reverb a 100% wet, post-fader send?
- [ ] Does the reverb have a high-pass?
- [ ] Is there real depth contrast between planes?
- [ ] Does it work in mono?
- [ ] Does the width come from opposition rather than a widener?
