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

**Card:** `music-kb/50_rhythm/afro-cuban-clave.md` (clave grids, roles, errors).
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-humanize`.

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
