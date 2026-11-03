---
name: chatmu-studio-afro-cuban-rhythms
description: >
  Programs Afro-Cuban grooves in Ableton Live from the clave: son and rumba
  clave, 3-2 vs 2-3, cascara, mambo bell, tumbao, songo, mozambique and merengue,
  translated to a drum kit. Trigger phrases: "clave", "son clave", "rumba clave",
  "salsa", "songo", "tumbao", "cascara", "mambo bell", "afro-cuban", "cuban groove",
  "3-2", "2-3", "merengue", "mozambique".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Afro-Cuban grooves built on a correct clave timeline"
version: "1.0"
tags: [studio, ableton, rhythm, clave, afro-cuban, salsa, songo, drums]
requiresTools:
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_set_tempo
  - local_ableton_snapshot
---

# Chatmu Studio — Afro-Cuban rhythms

**Reference:** the tables and decision tree are at the end of this skill.
**Related:** the genre skill (`chatmu-studio-genre-*`), `chatmu-studio-humanize`.

## When to use
When the user asks for salsa, son, rumba, songo, merengue, mozambique, a Cuban feel, or a
groove that "sounds Latin" without being a generic 4/4 loop.

## Workflow

1. **Pick the style and tempo.** Typical starting ranges: son 90–120 BPM, salsa 160–220,
   songo 90–110, merengue 120–160. Ask if unsure.
2. **Write the clave first**, on its own track, 2 bars:
   - Son 3-2: bar 1 = 1, & of 2, 4; bar 2 = 2, 3.
   - Rumba 3-2: bar 1 = 1, & of 2, 4; bar 2 = 2, & of 3.
   - 2-3 is the same pattern starting on the 2-side.
3. **Build the groove against the clave:**
   - verse/soft → cascara on the shell
   - chorus/peak → mambo bell
   - bass → tumbao, sparse, silent downbeat
   - modern Cuban → songo, usually 2-3, hi-hat on 1 and 3
4. **Write it** with `local_ableton_write_notes`; keep one note per hit (no rolls unless the
   style asks for them).
5. **Play it** with `local_ableton_fire` and count the clave out loud with the user.
6. **Only then** humanize: micro-timing and velocity, never before the clave is right.

## Hard rules
- The clave goes on its own reference track; do not bury it inside another pattern.
- Never double the clave: if another part already contains it, remove one.
- State clearly whether the pattern is 3-2 or 2-3.
- Do not mix 6/8 and 4/4 claves in the same section.
- In songo, hi-hat on 1 and 3; quarter notes are too busy, 2 and 4 clash.
- Cascara must leave the clave accents audible.
- At fast tempos, simplify the left hand before touching the clave.

## Output
State style, tempo, clave direction and the pattern map (which instrument plays what).
Then the MIDI written and a one-line listening instruction.

## Reference


### What it solves
Build grooves that feel Cuban instead of generic: clave as the reference timeline, 3-2 vs
2-3, son vs rumba, and how to translate cascara, tumbao and songo to a drum kit.

### Numbers

### Clave in 4/4 (16th grid, 2 bars)
| Pattern | Bar 1 (3-side) | Bar 2 (2-side) |
|---|---|---|
| Son 3-2 | 1, & of 2, 4 | 2, 3 |
| Rumba 3-2 | 1, & of 2, 4 | 2, & of 3 |
| Son 2-3 | 2, 3 | 1, & of 2, 4 |
| Rumba 2-3 | 2, & of 3 | 1, & of 2, 4 |

- **Son clave** feels 4/4; **rumba clave** feels 6/8 because the last note moves later.
- The difference between son and rumba is **one note**: the last note of the 2-side.
- 3-2 and 2-3 are the same pattern heard from a different "1". Most Afro-Cuban music
  moves between both; what matters is knowing where you are.

### 6/8
The 6/8 clave is the same figure phrased in 6/8; it is the base of bembe and Abakwa.
Do not mix 6/8 and 4/4 claves inside the same section.

### Roles in the arrangement
| Element | What it plays | When |
|---|---|---|
| Clave | the timeline (2 bars) | always, as reference |
| Cascara | continuous pattern on the shell | verses, soft sections |
| Mambo bell | denser bell pattern | coros, peaks |
| Bongo bell | complementary bell | with mambo bell |
| Tumbao | bass/conga pattern | groove base |
| Abanico | 4–5 stroke ruff | opens a 2-3 pattern |

### Principles
1. **Clave is the ruler**, not another percussion layer. Everything either aligns with it or
   deliberately contradicts it.
2. 3-2 and 2-3 are the same music; do not treat them as different grooves.
3. The 2-side is where the groove "answers"; the 3-side is where it states.
4. Cascara fills the space between clave notes; it must not mask them.
5. Tumbao is sparse: the bass often implies the clave with a silent downbeat.
6. In songo, the hi-hat goes on 1 and 3. Quarter notes are too busy; 2 and 4 clash with
   the downbeat feel.
7. At fast tempos, remove notes from the left hand before removing the clave.

### Decision tree
```
Need a Cuban feel?          → start from son clave 3-2 at the tempo
Want more tension?          → rumba clave (6/8 feel)
Verse or soft section?      → cascara on the shell
Chorus or peak?             → mambo bell
Need a modern Cuban groove? → songo, usually 2-3
Two percussion parts?       → mambo bell + bongo bell (complementary)
Fast tempo?                 → simplify the left hand, keep clave and bell
```

### By style
| Style | Clave | Signature |
|---|---|---|
| Son | son 3-2 / 2-3 | tumbao bass, cascara in verses |
| Rumba | rumba | palito patterns, guaguancó |
| Salsa | son | cascara verse, mambo bell coro |
| Songo | mostly 2-3 | hi-hat 1 and 3, syncopated toms |
| Mozambique | — | bell-driven, timbales |
| Merengue | — | 2-feel, jaleo and apanpicho sections |

### Common errors
- Layering clave on top of a pattern that already contains it (double clave).
- Mixing 3-2 and 2-3 without a clear "1".
- Quantizing everything to a straight grid and losing the 6/8 feel of rumba.
- Putting the hi-hat on every quarter in songo.
- Writing cascara that covers the clave accents.
- Treating Afro-Cuban rhythms as "just another 4/4 loop".

### How it is validated
- **Ableton**: write the clave on a separate track, loop 2 bars, program the groove against it.
- **Count**: say "1" at the start of the 3-side and check that the 2-side answers.
- **Ears**: `listen_dynamics` and `listen_spectrum` to confirm the clave is audible and not masked.
- **Reference**: A/B against a son/salsa/songo track at the same tempo.

### Checklist
- [ ] Is the clave written on its own reference track?
- [ ] Is it clearly 3-2 or 2-3?
- [ ] Does every other pattern align to the clave?
- [ ] Is the cascara leaving room for the clave?
- [ ] In songo, is the hi-hat on 1 and 3?
- [ ] At fast tempo, did you simplify without losing the clave?
