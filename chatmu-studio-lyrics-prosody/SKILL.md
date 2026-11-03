---
name: chatmu-studio-lyrics-prosody
description: >
  Writes and fits lyrics WITH the user so they sit naturally on a melody, in
  Spanish and English: stressed syllables on strong beats, open vowels on long and
  high notes, line length matched to the phrase, rhyme types and placement, title
  placement, verse vs chorus density. Never replaces the user's words silently;
  proposes options and explains why. Ties in with local_sing for a guide vocal.
  Trigger phrases: "lyrics", "write the lyrics", "fit the words", "the words
  don't fit", "prosody", "rhyme", "chorus lyrics", "hook line", "letra",
  "escribe la letra", "acomoda la letra", "no cuadra la letra", "prosodia",
  "rima", "letra del coro", "las sílabas no caben", "suena forzado".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Lyrics that sing: stress on strong beats, open vowels on long notes, rhyme and title placement, ES/EN"
version: "1.0"
tags: [studio, lyrics, prosody, songwriting, spanish, english, topline]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_get_notes
  - local_ableton_write_notes
  - local_ableton_create_clip
  - local_harmony_map
  - local_sing
---

# Chatmu Studio — Lyrics & prosody

Prosody = the words and the music saying the same thing at the same time. A line is
"wrong" when the natural stress of the word falls on a weak beat (es-pe-RAR sung as
ES-pe-rar), when a closed vowel is held on a high note, or when the line is one syllable
too long and gets crammed. These are measurable; this skill measures them.

**Collaboration rule:** the lyrics belong to the user. Never rewrite their words without
showing the original next to your proposal and the reason ("'corazón' stresses -ZÓN, but
your melody puts the long note on CO-; option A moves the word, option B moves the note").
They choose. If they wrote nothing, offer 2–3 options per line, not a finished song.

Related: melody first `chatmu-studio-hook-melody`; guide vocal `chatmu-studio-guide-vocal`;
section shapes `chatmu-studio-arrangement`.

## When to use
Writing lyrics for a melody, fitting existing lyrics to a melody (or a melody to lyrics),
the user says the words feel forced, rhymes are weak, the chorus "doesn't land", or before
rendering a guide vocal with `local_sing`.

## Ask only what is missing
Language (ES, EN or mixed), what the song is about in one sentence, the title/hook phrase
if they have one, and whether the melody exists. Max two questions at once.

## 1. Map the melody's stress grid
Read the clip (`local_ableton_get_notes`). For each note mark: beat position, length,
pitch, and **weight**:
- Strong: beat 1 (strongest), beat 3; any note ≥ 1 beat long; the highest note of the
  phrase; a note landing after a rest.
- Medium: beats 2 and 4.
- Weak: off-beat 8ths/16ths, short pickups (≤ 1/8), notes inside a run.
Syncopated anticipations (a note on the "and" of 4 tied over the bar) count as **strong** —
they take the stress of the downbeat they anticipate. This is how reggaeton, pop and R&B
hooks place stress.

## 2. Map the lyric's stress
- **Spanish**: count sung syllables with synalepha (vowels across word boundaries merge:
  "que_es-ta", "mi_a-mor" = fewer syllables). Stress rules: words ending in vowel/n/s
  stress the penultimate (CA-sa, CAN-tan); others the last (a-MOR, ciu-DAD); accent marks
  override (co-ra-ZÓN, MÚ-si-ca). Agudas (last-syllable stress) end lines on a strong beat
  with a "masculine" landing; llanas give a falling "feminine" ending (strong-weak);
  esdrújulas (MÚ-si-ca) need strong-weak-weak — rare at line ends, great for rhythm hooks.
- **English**: stress by dictionary (to-NIGHT, BEAU-ti-ful, re-MEM-ber); function words
  (the, a, of, to, and, in) are weak and must sit on weak positions; one-syllable content
  words (love, gone, know) can take strong beats. English packs more consonant clusters —
  fewer syllables per note than Spanish at the same tempo.

## 3. Align: the rules that make it sing
1. **Stressed syllable on a strong/medium position**, unstressed on weak. Every mismatch
   on a long or high note is a must-fix; mismatch on a fast pickup is tolerable.
2. **One syllable per note** by default. Melisma (one syllable over 2–4 notes) only on an
   open vowel and only at the peak or line end — R&B/gospel more, corridos/rap almost never.
3. **Open vowels on long and high notes**: ES /a/, /o/, /e/; EN "ah", "oh", "ay", "I" (as in
   "fly"). Avoid holding /i/ ("sí", "free") or /u/ above about A4 (female) / E4 (male) —
   they close and thin out. Avoid holding nasal/consonant endings: sustain the vowel and
   place the final consonant on the release.
4. **Line length = phrase length**. Count notes in the phrase vs syllables after
   synalepha. ±1 syllable: split or merge a note (same rhythm cell, keep the motif).
   ±2 or more: rewrite the line, don't cram.
5. **Breaths**: a rest ≥ 1/8 note at least every 2 bars at ≤ 100 BPM, every bar for dense
   rap/reggaeton flows. Never put a breath inside a word or between article and noun.
6. **Consonants on fast notes**: plosives (p, t, k, b, d) cut through and help 16th-note
   flows; long liquids (l, m, n) and vowels suit long notes.

## Density by section (syllables per bar, mid tempo 85–105 BPM)
| Section | Spanish | English | Feel |
|---|---|---|---|
| Verse | 8–14 | 6–11 | Conversational, detail, more words |
| Pre-chorus | 6–10 | 5–8 | Shorter lines, rising, builds tension |
| Chorus / hook | 3–8 | 3–6 | Fewer words, longer notes, repetition |
| Rap verse | 12–20 | 10–16 | 16th grid, internal rhymes |
| Post-chorus / chant | 2–6 | 2–5 | One word or vocable repeated ("eh", "oh-oh") |
At faster tempos (> 120) reduce ~25%; half-time feels (trap at 140) use the 70 BPM column.
Contrast is the point: if the chorus is as dense as the verse, it won't feel like a chorus.

## Rhyme
Types, strongest to loosest:
- **Perfect / consonante** (amor/dolor, night/light): closes; use at the end of the chorus
  and on the title line.
- **Asonante** (vowel-only: noche/corre, cielo/tiempo) — the Spanish default, natural,
  less "nursery rhyme".
- **Family / slant rhyme** (EN: time/mine, love/up): modern, conversational.
- **Internal rhyme**: rap, reggaeton, fast pop verses — 2–3 per line max.
Placement (Pattison's idea: rhyme scheme controls stability):
- AABB / couplets = stable, resolved, closes. Good for chorus.
- ABAB = balanced, moves forward. Good for verses.
- XAXA (only 2 and 4 rhyme) = conversational, loose; Spanish ballads and corridos.
- An unrhymed or off-rhymed last line = deliberate instability (leads into the next
  section). Use on purpose, once.
Avoid cliché pairs that scream generic: corazón/canción/razón, fire/desire, heart/apart,
eyes/skies — unless the user wants them; then twist the line before the rhyme.

## Title and hook placement
- Title at the **first line or last line** of the chorus — ideally both. Strongest beat,
  highest or longest note.
- It should be singable (≤ 5 syllables, open vowel on its stressed syllable) and repeated
  2–4 times per chorus.
- The verse should earn the title: concrete images (place, object, time) so the chorus
  can be abstract. "Show, don't tell" in the verse; tell in the chorus.
- Each verse ends pointing at the title so the chorus feels inevitable.

## What makes lyrics sound AI-written (avoid)
- Abstract nouns piled up (dreams, soul, destiny, alma, destino, eternidad) with no image.
- Every line the same length and the same rhyme scheme throughout.
- Rhymes chosen first, meaning bent to fit ("y tu voz es como el sol / que me da su
  calor") — rhyme words must be the words you'd say anyway.
- Stress fights the melody and nobody fixed it.
- Explaining the emotion instead of a moment that causes it.
- Mixing languages randomly; in Spanglish, switch at phrase boundaries, keep the hook in
  one language.

## Tool workflow
1. `local_ableton_snapshot` → tempo, key; `local_ableton_tracks` → find the melody clip.
2. `local_ableton_get_notes` → build the stress grid (step 1). `local_harmony_map` if
   you need to know which notes are chord tones (stable for long vowels).
3. Show the user a table per line: syllables, notes, stress mismatches, vowel on peak.
4. Offer fixes as options: move a word, swap a synonym, split/merge a note. If they
   approve a melody change, write it with `local_ableton_write_notes` (new clip or after
   duplicating with `local_ableton_create_clip`), never overwriting their original.
5. Render a guide with `local_sing` (lyrics + the melody clip) so the user hears the
   prosody. Listen for crammed syllables and closed vowels on high notes; fix and re-sing.
   For full guide-vocal options see `chatmu-studio-guide-vocal`.

## Hard rules
- Never change the user's words silently; always show original vs proposal and why.
- Stress on long/high notes must match natural word stress.
- Open vowel on the peak note of the chorus.
- Chorus less dense than the verse.
- Title on the first or last line of the chorus.
- Count Spanish syllables with synalepha before judging line length.
- Options, not a finished song, unless the user asks for a full draft.

## Tell the user (example)
"Your chorus melody has 7 notes with the long one on beat 1 of bar 2. 'No me olvides
esta noche' is 9 written syllables but sings as 7 with synalepha (me_ol, des_es), so it
fits, and 'NO-che' puts the open 'o' on the long note, which is ideal. The problem is
'ol-VI-des': your melody stresses 'ol'. Option A: shift the word one 16th later. Option B:
keep the melody and sing 'No te vayas esta noche'. Which sounds more like you? Then I'll
sing a guide so you can hear it."
