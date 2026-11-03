---
name: chatmu-mix-effects
description: >
  Uses reverb, delay, modulation, saturation/distortion and filters with intention
  in the user's Ableton Live set: send vs insert, pre-delay and decay from tempo,
  dotted/triplet delay times, ducked effects, depth planes front-to-back, genre
  starting points, with Ableton stock devices (Reverb, Hybrid Reverb, Echo, Delay,
  Chorus-Ensemble, Saturator, Roar, Auto Filter) and real parameter names read
  from the device before setting them. Verifies by listening.
  Trigger phrases: "reverb", "delay", "echo", "add space", "make it wider",
  "saturation", "distortion", "warmth", "filter sweep", "too dry", "too washy",
  "depth", "reverb", "eco", "delay", "más espacio", "que suene lejos", "más
  ancho", "saturación", "distorsión", "calidez", "barrido de filtro", "suena muy
  seco", "suena lavado", "profundidad".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Reverb, delay, modulation, saturation and filters with intent: tempo-synced, ducked, depth planes"
version: "1.0"
tags: [mix, studio, ableton, reverb, delay, saturation, effects, space]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_song
  - local_ableton_devices
  - local_ableton_load_device
  - local_ableton_device_params
  - local_ableton_set_device_param
  - local_ableton_mixer
  - local_ableton_edit_track
  - local_ableton_undo
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Mix — Effects with intention

Every effect answers one question: **where does this sound sit (front/back, wide/narrow,
clean/dirty), and does it move?** If you cannot name the answer, don't load the device.
The AI-mix tell is the opposite: the same long reverb on everything, delays at random
times, a Saturator on every track "for warmth". The result is a flat, washy wall.

Related: EQ before/after effects `chatmu-mix-eq`; dynamics `chatmu-mix-compression`;
ducking pumps `chatmu-studio-sidechain`; panning `chatmu-studio-spatial-panning`;
genre balances `chatmu-mix-by-genre`; order of the whole mix `chatmu-mixing-progressive`.

## When to use
User asks for space, width, echo, warmth, grit, a sweep; says a sound is "too dry",
"too washy", "flat", "stuck to the speakers"; or it is the effects pass of a mix.

## Ask only what is missing
Read tempo and tracks from the set first (`local_ableton_snapshot`, `local_ableton_song`).
Ask at most: genre/reference, and which element should feel closest. Never more than two.

## Send vs insert
| Use a **send (Return track, 100% wet)** | Use an **insert (on the track)** |
|---|---|
| Shared space: reverb, most delays | Effect IS the sound: distortion, filter, chorus on a synth |
| Several tracks in one room = glue | Only this track, wet/dry via Dry/Wet |
| You want to EQ/compress/duck the wet | Parallel blend inside a rack is fine too |

Rule: reverbs and throw delays live on Returns with Dry/Wet = 100%; the track's send knob
sets the amount. On an insert reverb, Dry/Wet 10–25% max. Start every Return with Live's
EQ Eight after the reverb: HPF 200–400 Hz, LPF 8–12 kHz (dark returns sit behind, bright
returns jump forward and hiss).

Default return layout (create only what the song needs, max 4):
- A: **Short room/plate** 0.6–1.2 s — glue drums, keys, backing vox.
- B: **Long hall/plate** 1.8–3.5 s — lead vocal, pads, snare throws.
- C: **1/4 or 1/8 dotted delay** — lead vocal, leads.
- D: **Special** (throw delay, reverse, shimmer) — automated, mostly silent.

## Times from tempo (always compute, never guess)
Quarter note ms = 60000 / BPM.
| Note | Factor | 90 BPM | 120 BPM | 128 BPM | 140 BPM |
|---|---|---|---|---|---|
| 1/4 | 1 | 667 | 500 | 469 | 429 |
| 1/8 | 0.5 | 333 | 250 | 234 | 214 |
| 1/8 dotted | 0.75 | 500 | 375 | 352 | 321 |
| 1/8 triplet | 0.333 | 222 | 167 | 156 | 143 |
| 1/16 | 0.25 | 167 | 125 | 117 | 107 |
| 1/4 dotted | 1.5 | 1000 | 750 | 703 | 643 |

- **Pre-delay**: 1/64–1/32 of a bar territory, 10–40 ms. Short (0–10 ms) = sound melts
  into the room; 20–40 ms = dry consonants stay clear, verb blooms after (lead vocal).
  Tempo-locked option: 1/64 note = quarter ms / 16 (120 BPM → 31 ms).
- **Decay**: the tail should fade before the next important hit. At 120 BPM (bar = 2000
  ms) aim ≈ 1 bar for a hall, ≈ 1/2 bar (1000 ms) for a room, ≈ 1 beat (500 ms) for a
  snare that must stay tight. Faster tempos/denser genres → shorter decay.
- Delay feedback: 15–30% (2–4 audible repeats) for vocals, 40–60% only for throws/dub.
- In Echo/Delay use Sync mode and pick the division; use ms mode only for slap.
- **Slapback** (rockabilly, rap ad-libs, guitars): 80–140 ms, feedback 0–10%, single repeat.

## Depth planes (front → back)
| Plane | What lives there | Recipe |
|---|---|---|
| Front | Lead vocal, kick, snare body, bass | Mostly dry; pre-delay 25–40 ms; brighter; more transient |
| Middle | Keys, guitars, hook synth, backing vox | Room send −15 to −10 dB; slight LPF on the send |
| Back | Pads, atmos, FX, choirs | More hall, less direct, LPF 6–8 kHz on track, shorter pre-delay, lower level |
Rule: **one** thing in front per section. Bass and kick get **no reverb** (or a room with
HPF ≥ 250 Hz on the return). Low end stays mono and dry.

## Ducking (keep it big without mud)
- Delay/reverb ducked by the lead vocal: Compressor on the Return, sidechain from the vocal,
  ratio 4:1, attack 1–5 ms, release 150–300 ms (≈ 1/8 at tempo), 4–8 dB GR. Repeats bloom in
  the gaps between phrases.
- Echo has a built-in **Ducking** section (Duck amount + Release): use it first.
- Pads/reverb wash ducked by kick for EDM: see `chatmu-studio-sidechain`.

## Modulation
- **Chorus-Ensemble**: Chorus mode on Rhodes/pads/clean guitar, Rate 0.3–1 Hz, Amount low,
  Dry/Wet 20–40%. Ensemble mode = 80s string machines. Never on bass below ~150 Hz (use
  Width/Crossover so lows stay mono) and never on the lead vocal by default.
- **Phaser-Flanger** / Auto Pan: movement for one element, synced (1/4, 1 bar), not all.
- Doubler effect: Delay with L 10–15 ms / R 20–25 ms, no feedback, low wet, on a backing.

## Saturation and distortion (harmonics, not loudness)
- **Saturator**: Analog Clip or Soft Sine for gentle color; Drive 2–6 dB, Output = −Drive
  (gain-match before judging); Dry/Wet 30–60% for parallel. Warm Tube on bass to add
  harmonics at 200–1500 Hz so it reads on phones.
- **Roar**: modern multi-stage; Shaper/Tube/Fractal types, Single/Serial/Parallel/Multiband
  routing. Multiband to dirty the mids of a bass and keep the sub clean. Amount via Drive,
  blend via Dry/Wet; Roar also has a Compressor and Feedback section — keep Feedback off
  unless you want sound design.
- 808: Saturator or Roar so the note is heard on small speakers; check sub is still mono.
- Drums bus: 1–3 dB of saturation, more only for lo-fi, boom bap, rock.
- Gain-match every A/B. Louder always "sounds better" and fools you.

## Filters
- **Auto Filter**: HPF/LPF with Frequency and Resonance; LFO (synced) for movement;
  Envelope follower for wah. Builds: LPF 200 Hz → 20 kHz over 8–16 bars, or HPF 20 →
  400–800 Hz in the last 4 bars of a build, snap back on the drop downbeat.
- Telephone/radio: band-pass 400 Hz–3 kHz on a verse vocal line or intro.
- Low-pass the reverb return, not the dry source, to push things back without dulling them.

## Device parameters: always read, then set
Parameter names differ between devices and Live versions. Before any set:
1. `local_ableton_devices` on the track → device index.
2. `local_ableton_device_params` → exact names, current values, ranges.
3. `local_ableton_set_device_param` with those names. Never invent a name.
Typical names to look for: Reverb "Predelay", "Decay Time", "Dry/Wet", "Diffusion";
Hybrid Reverb "Predelay", "Decay", "Algorithm"/"Blend"; Echo "L Time"/"R Time", "Feedback",
"Duck"; Saturator "Drive", "Output", "Type"; Auto Filter "Frequency", "Resonance".
Confirm from the params call; if absent, report it and pick the closest real one.

## Genre starting points
| Genre | Space | Delay | Color |
|---|---|---|---|
| Pop | Plate 1.6–2.2 s on vox, room on drums | 1/8 dotted, ducked | Light Saturator on vox bus |
| Hip-hop / trap | Mostly dry lead, short room | Throws on the last word of lines, 1/4 | 808 saturation, hats dry |
| Reggaeton | Short plate vox, dry dembow | 1/8 or 1/4 ducked, low wet | Clean |
| House / techno | Short room on drums, long hall on stabs/pads | 1/8 dotted or 3/16 on stabs | Drum bus saturation, Auto Filter rides |
| Lo-fi | Room + filtered hall | 1/4 dub-ish | Heavy Saturator, LPF 8–10 kHz |
| Ballad / cinematic | Hall 2.5–4 s, more pre-delay | 1/4 low wet | Minimal |
| Rock | Room on drums, plate on vox | Slapback on vox | Amp/drive on guitars, bus saturation |
| Corridos / regional | Short room, natural | Little or none | Clean, acoustic |

## What ruins it
- Same reverb at the same amount on every track → no depth, mud at 200–500 Hz.
- Reverb on kick/bass/808 → low end blurs, loses punch in clubs.
- Delay at a non-synced time → flams and rhythmic chaos.
- Long tails at fast tempos → the groove smears.
- Saturating without gain-matching → you keep turning it up.
- Stereo width (chorus/wide verb) on low frequencies → phase issues in mono.
- Everything automated all the time → nothing feels special.

## Tool workflow
1. `local_ableton_snapshot` + `local_ableton_song` → tempo, tracks, existing returns.
2. Compute times (table above) and tell the user the numbers.
3. Create/reuse Returns (`local_ableton_edit_track`), load devices with
   `local_ableton_load_device`; read params (`local_ableton_device_params`) before setting.
4. Set sends with `local_ableton_mixer` (start at −15 dB, raise until audible, back off 2 dB).
5. `local_ears_track_levels` → check masking in 200–500 Hz and that returns don't overtake
   the dry. `local_ears_listen` → overall check (indicative, trust your ears more).
6. Each change is undoable: offer `local_ableton_undo` if the user dislikes it.

## Hard rules
- Read params before setting; never guess names.
- Reverb/delay on Returns at 100% wet unless there is a reason.
- HPF every reverb return ≥ 200 Hz; no reverb on sub-bass content.
- Delay times synced or computed from 60000/BPM.
- Gain-match saturation before judging it.
- Max 4 returns; one element in front per section.
- One change at a time, explain it, let the user hear it.

## Tell the user (example)
"At 96 BPM a quarter is 625 ms, so I set the vocal delay to a dotted 1/8 (469 ms),
feedback 22%, ducked so the echoes only appear between your lines. The plate has 30 ms
pre-delay so the words stay up front, and I cut its lows below 300 Hz so it doesn't muddy
the bass. Want it more distant or a bit drier?"
