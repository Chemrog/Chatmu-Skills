---
name: chatmu-studio-breakbeats
description: >
  Programs breakbeats in Ableton Live using the 13 elements of funk drumming:
  ghost notes, kick doubles, open hi-hats, syncopated snare accents, rolls,
  hi-hat subdivision, triplets and 3-over-2 polyrhythm. For boom bap, lo-fi,
  hip-hop, DnB and dubstep. Trigger phrases: "breakbeat", "boom bap drums",
  "funk drums", "ghost notes", "break", "drum break", "hip-hop drums",
  "dnb drums", "jungle", "half-time", "make the drums groove".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Breakbeats built from the 13 elements of funk drumming"
version: "1.0"
tags: [studio, ableton, rhythm, breakbeat, drums, hip-hop, funk, boom-bap]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_set_tempo
---

# Chatmu Studio — Breakbeats

**Reference:** the tables and decision tree are at the end of this skill.
**Related:** the genre skill (`chatmu-studio-genre-*`), `chatmu-studio-humanize`, `chatmu-studio-sampling`.

## When to use
When the user wants boom bap, lo-fi, hip-hop, funk, DnB, jungle or dubstep drums, or says
the drums "don't groove".

## Workflow

1. **Set tempo and feel.** Boom bap 80–95, DnB/jungle 160–180, dubstep ~140 half-time.
2. **Program the framework:** kick on 1 and 3, snare on 2 and 4, steady 8th or 16th hats.
3. **Add element 8** (steady 16th hi-hat) so the kick and snare lock.
4. **Add elements one at a time**, in this order: 4 (kick doubles), 1 (ghost snares),
   6 (syncopated accents), 5 (open hats sparingly), 9 (hat variation).
5. **Set velocities:** ghost notes 20–40, main snare 90–110, hats lower than snare.
6. **Add 11 or 13 only for a fill or a special bar.**
7. **Play it** with `local_ableton_fire`; if it does not make you nod, remove an element.
8. **Humanize only after** the quantized groove works.

## Hard rules
- One element per pass; never add three at once.
- Do not overuse the open hi-hat: it turns the break into disco.
- Do not quantize ghost notes so hard that the pocket disappears.
- Keep a steady hi-hat layer; it is the floor of the groove.
- Element 11 (triplets) and 13 (3-over-2) are spice, not the main pattern.
- Match the tempo to the genre before programming.

## Output
State tempo, feel, elements used and velocities. Then the MIDI written and a one-line
listening instruction. If it still does not groove, remove the last element added.

## Reference


### What it solves
Program or play a breakbeat that actually grooves instead of a generic 4/4 loop. The book
breaks funk drumming into 13 elements that can be added one at a time.

### Numbers
| Parameter | Value |
|---|---|
| Grid | 16th notes: `1 e & a 2 e & a 3 e & a 4 e & a` |
| Boom bap tempo | 80–95 BPM |
| DnB / jungle | 160–180 BPM |
| Dubstep | ~140 BPM, half-time feel |
| Ghost-note velocity | 20–40 |
| Main snare velocity | 90–110 |
| Swing | 54–62% as a starting point |

### The 13 elements (Adamo)
| # | Element | What it adds |
|---|---|---|
| 1 | Snare single 16th on the “e” and/or “ah” (ghosted) | texture, depth, swing |
| 2 | Kick single 16th on the “e” and/or “ah” | flow, variety |
| 3 | Snare two 16ths in a row with one hand | colour, depth |
| 4 | Kick two 16ths in a row | power, strength |
| 5 | Open hi-hat | flavour; overuse sounds disco |
| 6 | Syncopated snare accents away from 2 and 4 | changes the feel |
| 7 | Buzz strokes and rolls on the snare | style, texture |
| 8 | Steady 16th-note hi-hat with one hand | solid layer, pocket |
| 9 | Hi-hat mix of 8ths, 16ths and rests | pushes or breaks the flow |
| 10 | Kick three or more 16ths in a row | drive |
| 11 | Broken 16th-note triplets on kick/snare | bounce; use sparingly |
| 12 | Unison (chordal) drumming | weight, colour |
| 13 | Three-16th-note phrase over 4/4 (3-over-2) | polyrhythm, tension |

### Principles
1. **Framework first:** kick on 1 and 3, snare on 2 and 4, steady 8th or 16th hats.
2. **Add one element at a time.** If you add three at once, you cannot hear what works.
3. **Ghost notes are the funk.** They sit low in velocity and fill the 16th grid.
4. **Element 8 is the floor.** A steady 16th hat makes the kick and snare lock.
5. **Element 6 is the twist.** Moving the snare accent off 2 and 4 changes the whole feel.
6. **Element 5 is salt.** A little open hi-hat = breakbeat; too much = disco.
7. **Element 11 and 13 are spice.** Use them once or twice, not every bar.
8. **Straight or swung, not accidental.** Decide the 16th-note feel and keep it.

### Decision tree
```
Need a basic funk break?     → framework + element 8 + element 1
Need more drive?             → element 4, then 10
Need more swing?             → element 1 ghosted on e/a, swing 54–60
Need a feel change?          → element 6 (move the snare accent)
Need a fill or turnaround?   → element 7 or 11
Need tension?                → element 13 (3-over-2)
Want DnB/jungle?             → 160–180 BPM, chop the break, add sub
Want dubstep?                → 140 BPM half-time, snare on 3
```

### Build order (safe)
```
1. Framework (kick 1/3, snare 2/4, hats)
2. Element 8 (steady 16th hats)
3. Element 4 (kick doubles)
4. Element 1 (ghosted snares)
5. Element 6 (syncopated accents)
6. Element 5 (open hats, sparingly)
7. Element 9 (hat variation)
8. Elements 11/13 only for a fill or a special bar
```

### Common errors
- Overusing the open hi-hat: turns the break into disco.
- Quantizing ghost notes to the grid and killing the pocket.
- Adding elements 11 and 13 everywhere: no contrast.
- No steady hi-hat layer: the kick and snare never lock.
- Accenting every snare on 2 and 4 only: no surprise.
- Programming at the wrong tempo for the genre.

### How it is validated
- **Ableton**: program the framework, then add one element per pass and listen.
- **Ears `listen_dynamics`**: ghost notes must be visibly lower than main hits.
- **Ears `listen_spectrum`**: hats and snare must not mask each other.
- **A/B**: compare against a classic break at the same tempo.
- **Dance test**: the loop must make you nod without the melody.

### Checklist
- [ ] Is the framework clear (kick 1/3, snare 2/4)?
- [ ] Is there a steady hi-hat layer?
- [ ] Are ghost notes low in velocity?
- [ ] Is the snare accent moved off 2/4 at least once?
- [ ] Is the open hi-hat used sparingly?
- [ ] Are triplets/polyrhythm used only as spice?
- [ ] Does it groove without melody?
- [ ] Is the tempo right for the genre?
