---
name: chatmu-studio-club-grooves
description: >
  Builds club grooves in Ableton Live for house, techno, trance, drum & bass,
  dubstep and chill-out: correct tempo, kick/snare/hat grid, bass placement and
  8/16/32-bar structure. Trigger phrases: "house groove", "techno", "trance",
  "drum and bass", "dnb", "jungle", "dubstep", "chill-out", "four on the floor",
  "club beat", "edm drums".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Club grooves: tempo, drum grid, bass and structure by genre"
version: "1.0"
tags: [studio, ableton, genres, house, techno, trance, dnb, dubstep, groove]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_set_tempo
---

# Chatmu Studio — Club grooves

**Reference:** the tables and decision tree are at the end of this skill.
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-sidechain`, `chatmu-studio-drop-buildup`.

## When to use
When the user asks for house, techno, trance, drum & bass, jungle, dubstep or chill-out,
or says a club track "doesn't feel like the genre".

## Workflow

1. **Set the genre and tempo**.
2. **Program the grid:**
   - House/techno/trance: kick on 1, 2, 3, 4; clap on 2 and 4.
   - House: open hat on the offbeats (3, 7, 11, 15 in 16ths), closed hat on all 16.
   - DnB: 2-step, snare on 2 and 4 plus ghost snares; kick syncopated.
   - Dubstep: half-time, kick on 1, snare on 3.
3. **Place the bass in the holes** left by the kick; sidechain if it fights.
4. **Add structure** in 8/16/32-bar blocks: intro, build, drop, breakdown.
5. **Play it** with `local_ableton_fire`; A/B against a reference at the same BPM.
6. **Only then** add texture and automation.

## Hard rules
- One genre at a time: do not mix DnB tempo with a house kick.
- Dubstep snare goes on 3, not 2 and 4.
- DnB is 2-step: ghost snares matter more than the main snare.
- Keep the offbeat open hat in house; it is the signature.
- One polyrhythm at a time.
- Leave room for the kick in the bass.
- Do not change chords every bar in techno; manage energy, not song form.

## Output
State genre, BPM, grid (kick/snare/hat), bass placement and structure. Then the MIDI
written and one reference to compare against.

## Reference


### What it solves
Pick the right tempo, kick/snare/hat pattern and structure for house, techno, trance,
drum & bass, dubstep and chill-out, instead of applying one generic 4/4 loop.

### Numbers

### Tempo and core pattern
| Genre | BPM | Kick | Snare/clap | Hats | Bass |
|---|---|---|---|---|---|
| House | 118–128 | 1, 2, 3, 4 | 2 and 4 | open on offbeats; closed 16ths | offbeat, short |
| Techno | 124–150 | 1, 2, 3, 4 | 2 and 4 or sparse | 16ths or offbeat | rolling, repetitive |
| Trance | 134–140 (138 standard) | 1, 2, 3, 4 | 2 and 4 | 1/8 offbeat open | rolling 16ths |
| Drum & bass | 165–185 (172/175) | 1 and 3, varied | 2 and 4 + ghost snares | 16ths, broken | sub, long |
| Dubstep | ~140, half-time | 1 | 3 | sparse, 16th details | sub + wobble |
| Chill-out | 80–126 | sparse / 2 and 4 | 2 and 4 | soft | long, simple |

### The basic house/club grid (16 pulses)
- Kick: **1, 5, 9, 13** (every beat).
- Snare/clap: **5 and 13** (beats 2 and 4).
- Open hat: **3, 7, 11, 15** (offbeats).
- Closed hat: all 16 pulses, lower velocity.

### Structure
| Genre | Phrase | Signature |
|---|---|---|
| House | 8/16 bars | groove first, drop, breakdown |
| Techno | 16/32 bars | linear, few changes, texture |
| Trance | 32 bars | build, breakdown, reprise |
| DnB | 8/16 bars | 2-step, switch-ups, sub |
| Dubstep | 8/16 bars | half-time, drop, wobble |

### Principles
1. **Tempo first.** The same pattern at the wrong BPM is a different genre.
2. **Four-on-the-floor is a family, not a genre.** House, techno and trance share the kick
   and differ in hats, bass and structure.
3. **DnB is not fast house.** It is 2-step: snare on 2 and 4 with ghost snares around it.
4. **Dubstep is half-time.** The snare lands on 3, not 2 and 4.
5. **The offbeat open hat is the house signature.** Remove it and the groove changes.
6. **Bass follows the kick's holes**, not the kick itself.
7. **One polyrhythm at a time.** Stacking 3:2 and 4:3 sounds confused (Snoman).
8. **Structure is energy management:** what enters and leaves every 8/16/32 bars.

### Decision tree
```
Want house?        → 118–128, kick 4/4, clap 2/4, open hat offbeats
Want techno?       → 124–150, kick 4/4, sparse clap, 16th hats, rolling bass
Want trance?       → 134–140, kick 4/4, offbeat open hat, 32-bar build
Want DnB?          → 165–185, 2-step, snare 2/4 + ghosts, sub
Want dubstep?      → ~140 half-time, kick 1, snare 3, sub + wobble
Want chill-out?    → 80–126, sparse kick, soft hats, long bass
```

### Common errors
- Playing DnB at 140 BPM and calling it DnB.
- Putting the dubstep snare on 2 and 4 instead of 3.
- Using the house offbeat hat in techno and losing the hypnotic feel.
- Overloading the groove: every element playing every 16th.
- Changing chords every bar in techno: it is texture, not song form.
- No contrast between build and drop.

### How it is validated
- **Ableton**: program the grid, then A/B against a reference at the same BPM.
- **Ears `listen_spectrum`**: kick and bass must not fight.
- **Ears `listen_dynamics`**: the drop must be louder/denser than the build.
- **Dance test**: the groove must work with no melody.

### Checklist
- [ ] Is the BPM right for the genre?
- [ ] Is the kick pattern correct (4/4 vs 2-step vs half-time)?
- [ ] Is the snare on the right beats?
- [ ] Does the hat pattern match the genre?
- [ ] Does the bass leave room for the kick?
- [ ] Is there a real build/drop contrast?
- [ ] Does it work with no melody?
