---
name: chatmu-mix-by-genre
description: >
  Balances a mix to the conventions of its genre in the user's Ableton Live set:
  who owns the low end, how far the vocal or lead sits above the beat, how loud
  drums, bass, chords and FX are relative to the mix, how wide and how wet each
  element is, and the master loudness target — measured per track with Chatmu
  Ears (local_ears_track_levels) and corrected with real mixer moves. Trigger
  phrases: "mix this like a trap song", "balance the mix", "levels", "the vocal
  is buried", "the 808 is too loud", "mix for the genre", "mezcla por género",
  "balancea la mezcla", "niveles", "la voz no se oye", "el 808 está muy
  fuerte", "mézclalo como reggaetón", "que suene como el género".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Genre-correct balance: low-end owner, vocal over beat, relative levels, width, space, measured per track"
version: "1.0"
tags: [mixing, studio, ableton, balance, genre, levels, ears]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ears_track_levels
  - local_ears_listen
  - local_ableton_mixer
  - local_ableton_apply
  - local_ableton_undo
---

# Chatmu — Mix by genre

Every genre has a balance its listeners expect. A trap mix with a quiet 808 or a rock mix
with a vocal 8 LU over the band sounds "wrong" even when each sound is good. This skill sets
the **balance** (levels, low-end ownership, width, space) to the genre, measures it, and
corrects it. Tone shaping (EQ, compression, chains) stays in `chatmu-mixing-progressive`,
`chatmu-mix-eq`, `chatmu-mix-compression`; preparing the session in `chatmu-session-prep`.

## When to use
After the arrangement is done (or at approval 3 of `chatmu-studio-make-song`), or when the user
says the mix "doesn't sound like the genre", something is buried or too loud.

## How the numbers work
`local_ears_track_levels` solos each track over the same bars and returns, per track,
`vs_mix_lu` = track short-term loudness minus the full mix (always negative; closer to 0 =
louder in the mix), plus bands and `masking` pairs. Targets below are **vs_mix_lu ranges for
the loudest section (hook/chorus/drop)**, measured on the stream (indicative, good for
comparisons). Use them as a starting map, then trust the ear and a reference
(`chatmu-studio-reference`).

Roles: a track's role comes from its name/colour (`chatmu-session-prep`); with several tracks
in one role (e.g. 3 synth layers), measure the group/bus.

## Genre balance targets (vs_mix_lu in the loudest section)
| Genre | Low-end owner | Kick | Bass / 808 | Snare/clap | Lead vocal / main hook | Chords / pads | Master target (LUFS-I) |
|---|---|---|---|---|---|---|---|
| Pop | kick + bass share (kick 50–80 Hz, bass 80–150) | −6 to −8 | −7 to −9 | −7 to −9 | −2 to −4 (vocal is king) | −10 to −14 | −9 to −11 |
| Rock | bass guitar under kick | −6 to −8 | −8 to −10 | −5 to −7 (snare loud) | −4 to −6 (inside the band) | guitars −5 to −8 (L/R) | −8 to −10 |
| Dark trap / drill | **808** (30–60 Hz) | −8 to −11 (short, clicky) | −3 to −5 | −6 to −8 | −2 to −4 (vocal) / hook −6 to −8 when a vocal exists | −12 to −16 | −7 to −9 |
| Hip hop (boom bap/lo-fi) | kick + bass, sample filtered | −5 to −7 | −7 to −9 | −5 to −7 | −2 to −4 (rap upfront, dry) | sample/keys −8 to −12 | −9 to −11 (lo-fi −12 to −14) |
| Reggaetón | kick + bass in unison feel | −5 to −7 | −6 to −8 | −6 to −8 (snare/rim of the dembow) | −2 to −4 | −10 to −14 | −7 to −9 |
| House / techno | **kick** (sidechained bass) | −3 to −5 | −7 to −9 | −7 to −9 | lead/vocal −5 to −8 | −10 to −14 | −7 to −9 |
| DnB | kick/sub split (sub 40–80) | −6 to −8 | −4 to −6 | −4 to −6 (snare cracks) | −5 to −8 | −10 to −14 | −6 to −8 |
| R&B | sub bass, soft kick | −7 to −9 | −6 to −8 | −8 to −10 | −1 to −3 (vocal very forward) | −8 to −12 | −9 to −11 |
| Ambient | pad/drone, no defined owner | — or −12+ | −10 to −14 | — | lead texture −6 to −10 | −3 to −6 (the pads ARE the track) | −16 to −14 |
| Regional mexicano | tuba/tololoche + kick | −8 to −10 | −5 to −7 | −8 to −10 | −1 to −3 (vocal on top, dry) | requinto/guitars −5 to −8 | −9 to −11 |
| Cinematic | low strings/brass + taikos | percussion −4 to −8 at hits | low strings −5 to −8 | — | theme −3 to −6 | −6 to −10 | −14 to −12 (−18 to −16 for media/library) |

Master targets are for the final export (measured by `chatmu-master-check`), not the stream.
If the user gives a reference, match the reference instead.

## Width and space by genre
| Genre | Centre (mono) | Wide | Space |
|---|---|---|---|
| Pop | kick, snare, bass, lead vocal | doubles, pads, BVs, hats slightly | vocal plate 1.2–1.8 s, delay 1/4 or 1/8 dotted |
| Rock | kick, snare, bass, vocal | rhythm guitars hard L/R (double-tracked) | room on drums, short plate on vocal |
| Trap / drill | kick, 808, snare, vocal | hook layers, pads, hat counter-patterns | dark long reverb on the hook, vocal fairly dry with 1/8 delay throws |
| Hip hop | kick, snare, bass, rap | sample stereo as recorded | little reverb; vinyl/room texture |
| Reggaetón | kick, bass, dembow snare, vocal | pads, percussion fills, ad-libs | vocal reverb short + 1/4 delay; percussion dry |
| House / techno | kick, bass, clap | hats, percussion, pads, FX | big returns on breakdown, short on drop |
| Ambient | — | almost everything wide | long reverbs 4–10 s, delays with feedback; it is the sound |
| Cinematic | low end, theme | sections by orchestral seating (violins L, cellos R-centre) | hall 2–3 s; pre-delay 20–40 ms |

## Workflow
1. **Read the set:** `local_ableton_snapshot` / `local_ableton_tracks` (roles, current faders).
   Confirm the genre from the brief or ask once.
2. **Measure:** `local_ears_track_levels` over the loudest section (tell the user it plays out
   loud and how long: ≈ (tracks + 1) × (seconds_per_track + 1.5) s). One approval covers it.
3. **Compare** each role's `vs_mix_lu` with the table. List only the roles out of range, worst
   first, and the `masking` pairs that matter for the genre (kick vs 808 in trap, vocal vs
   synths in pop).
4. **Plan** (show it as a short table: track, now, target, move in dB). Rules:
   - Fix the low-end owner first; then the vocal/lead; then the rest relative to those two.
   - Move faders in small steps (1–2 dB) — a 3 LU error rarely needs more than 3 dB.
   - Prefer turning things **down**; keep the mix headroom (peaks under −6 dBFS on the
     master before mastering).
   - A masking pair is fixed with EQ/sidechain (`chatmu-mix-eq`, `chatmu-studio-sidechain`),
     not only with faders.
5. **Apply** after OK with `local_ableton_apply` (one batch of mixer moves, `type: "mixer"`,
   `property: "volume"`, values in dB) or `local_ableton_mixer` for a single change.
6. **Re-measure** the same bars with `local_ears_track_levels` (only the tracks you moved plus
   the reference roles). Keep changes that moved toward target and that the user likes;
   otherwise `local_ableton_undo`.
7. **Listen** with the user (`local_ears_listen` for the mix), then hand over to EQ/compression
   or to mastering.

## Hard rules
- Measure before moving; never balance from track names alone.
- Same bars before and after; otherwise the numbers don't compare.
- The table is a map, not law: a reference or the user's ear beats it.
- Never push the master into clipping to make things "louder"; loudness is the master's job.
- Never change more than one role's level at a time without re-listening.

## Tell the user (short)
`Trap balance (hook): 808 −7 LU → target −4 (raising 3 dB), vocal sits right at −3, hook synth
−5 → −7 (lowering 2 dB so it doesn't fight the vocal). Kick vs 808 overlap 0.62 → sidechain
next. Applying the three moves?`
