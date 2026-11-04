---
name: chatmu-studio-genre-fusion
description: >
  Combines two (rarely three) genres into one coherent track in the user's
  Ableton Live set without it sounding like a collage: decides which genre owns
  each layer (tempo/feel, drums, bass, harmony, melody, sounds, form, mix),
  resolves the classic conflicts (swing vs straight, half-time vs double-time,
  dembow vs four-on-the-floor, modal vs functional harmony), and builds a
  signature where both genres are audible. Trigger phrases: "fusion", "mix
  reggaeton with house", "trap but with jazz", "cumbia meets techno",
  "genre blend", "fusión", "mezcla de géneros", "reggaetón con house",
  "trap con jazz", "corridos con trap", "que tenga algo de", "con toque de".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Fuse two genres coherently: assign each layer an owner, resolve tempo/groove/harmony conflicts, one signature"
version: "1.0"
tags: [studio, ableton, genre, fusion, arrangement, production]
requiresTools:
  - local_ableton_load_device
  - local_ableton_browser
  - local_sound_status
  - local_sound_set_preset
  - local_ableton_snapshot
  - local_ableton_set_tempo
  - local_music_theory
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_sound_find_preset
---

# Chatmu Studio — Genre fusion

A collage plays genre A, then genre B. A fusion plays **both at once**, because each layer
belongs to one genre on purpose. The rule: **one genre owns the body (tempo, drums, low end),
the other owns the colour (harmony, melody, sounds)** — and one signature element carries the
second genre into the body so they touch.

Use with the two genre skills involved (`chatmu-studio-genre-*`); this skill decides how to
combine them. Full song flow: `chatmu-studio-make-song`.

## 1. Name the host and the guest
- **Host** = the genre the track will be filed under (where it plays: club, urban playlist,
  regional radio). It owns tempo/feel, drums, bass and form.
- **Guest** = the colour. It owns 1–3 of: harmony, lead melody/hook, a signature instrument or
  sound, a rhythmic motif layered on top.
Ask the user only if it is truly ambiguous ("corridos with trap": regional host with trap drums,
or trap host with requinto? Propose one and say why).

## 2. Layer ownership table (fill it and show it)
| Layer | Owner | Notes |
|---|---|---|
| Tempo / feel | host | guest material is re-timed to it |
| Drums | host + 1 guest signature element | e.g. house kit + reggaetón rim on the dembow positions |
| Bass / low end | host | its rhythm comes from the host groove, its notes from the harmony |
| Harmony | guest (or host) | choose one harmonic language; don't alternate per section |
| Hook / lead | guest | the clearest place to hear the guest genre |
| Signature sound | guest | requinto, sax, log drum, accordion, bell, oud… |
| Form | host | guest may borrow one section idea (a breakdown, a solo) |
| Mix | host | balance and loudness of the host (`chatmu-mix-by-genre`) |

## 3. Resolve the conflicts
### Tempo
| Combination | Fix |
|---|---|
| One is ~2× the other (trap 140 + reggaetón 95 → 70/140) | use the half/double relation: host tempo, guest felt at half or double |
| Close tempos (house 124 + reggaetón 95) | host tempo; re-pattern the guest groove at the host tempo (dembow at 124 = moombahton-ish only if slowed to 105–112) |
| Far apart, no relation (ambient 70 + DnB 174) | DnB at 174 with half-time ambient pads (87 feel) |
Set it once with `local_ableton_set_tempo`. Never change tempo between sections in a fusion
unless the form is built around it (a bridge in half-time is fine; it's still the same BPM).

### Groove
- **Swing vs straight:** pick one grid for everything. If the host is straight (house, reggaetón),
  quantize guest material straight and keep only its accents. If the host swings (hip hop, jazz,
  amapiano), swing the guest too — mixed grids sound like a mistake.
- **Dembow vs four-on-the-floor:** keep the host kick; put the guest pattern on snare/rim/percussion.
- **Clave-based guest (salsa, cumbia):** the clave or güira/guacharaca pattern goes on top at low
  velocity; the host kick avoids fighting it (`chatmu-studio-afro-cuban-rhythms`).
- **Triplet hats (trap) in a straight genre:** limit rolls to transitions.

### Harmony
- **Modal guest over functional host** (Hijaz hook over pop chords): don't. Choose a pedal or a
  modal progression both can live on (see `chatmu-studio-genre-oriental-hiphop`).
- **Rich guest harmony (jazz, R&B) over a minimal host (trap, techno):** keep the rich voicings but
  slow the harmonic rhythm to the host's (1 chord per 2 bars), and keep the bass on roots.
- **Regional/folk harmony (I–IV–V7) in an urban host:** convert to the host's minor loop only if
  the guest melody still fits; otherwise keep I–IV–V7 and darken with the sounds.
Use `local_music_theory` (`progression`/`chords`) to write it and `chatmu-studio-harmony` for
voicings.

### Sound and register
Give the guest signature its own register and space: requinto/sax/flute high-mid, log drum in
the bass register only if the host bass steps back. Search the guest sound with
`local_sound_find_preset` (it may return a `fallback`; say so).

## 4. Proven pairings (starting points)
| Fusion | Host | Guest brings | Signature |
|---|---|---|---|
| Corridos tumbados (regional × trap) | regional | trap hats/808, dark minor | requinto lines over 808 |
| Reggaetón × house (moombahton / Latin house) | house or reggaetón | the other's drums on top | dembow rim over 4/4 kick |
| Trap × jazz | trap | rootless 9th/13th chords, sax or Rhodes hook | jazzy keys under 808 |
| Hip hop × oriental | hip hop | Hijaz/double harmonic, darbuka | ornamented flute hook |
| Afrobeats × R&B | afrobeats | R&B vocal style, 7th chords | log drum + R&B topline |
| Cumbia × electronic (cumbia digital) | cumbia | synth bass, electronic drums | güira/guacharaca + accordion over synths |
| Pop × rock | pop | live drums, guitars | guitar hook in the chorus |
| Ambient × techno | techno | evolving pads, long reverbs | filtered drone through the drop |
| Lo-fi × bossa | lo-fi hip hop | bossa chords and guitar | nylon guitar over swung drums |

## 5. Workflow
1. Read both genre skills' key sections (tempo, groove, harmony, sounds).
2. Fill the ownership table and the conflict fixes; show both in 4–6 lines.
3. Build the 8-bar idea in the host's build order (`chatmu-studio-make-song` phase 1), adding
   the guest signature as the 3rd layer at the latest — it must be in the idea from the start,
   not added at the end.
4. Fire after each layer; ask: "Do you hear both genres?" If one disappears, strengthen its
   signature (louder, more repeated, clearer register), don't add more guest layers.
5. Arrange and mix as the host.

## Hard rules
- One host, one guest. A third genre only as a single signature element, never a layer set.
- One grid (straight or swung) and one tempo for the whole track.
- One harmonic language for the whole track.
- The guest signature appears in the 8-bar idea and in every hook/chorus.
- Never alternate sections genre by genre (verse A, chorus B) unless the user asks for that.

## Tell the user (short)
`Corridos × trap: regional is the host (form, requinto, vocal style), trap is the guest (808 with glide, hat rolls only into the hook). 140 BPM felt as 70, straight grid, i–♭VI–♭VII–i minor. Signature: requinto answers over the 808.`

## Sounds
**Chatmu Sound first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Sound with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_sound_find_preset` with `genre: "the genres being fused"`, the `instrument` and a `character`. If it
   returns `fallback: true`, say it's the closest genre.
2. Load the plugin on the track: searching the browser by name does NOT find plugins, so use
   `local_ableton_browser` `path: "plugins"` (then its VST3 folder) to get Chatmu Sound's `uri`,
   and `local_ableton_load_device` with that `uri`.
3. Right after loading, `local_sound_set_preset { file }` (it goes to the newest instance), then
   `local_sound_status`: that track's instance must show the `preset_name`. An empty
   `preset_name` means no preset is loaded yet — never tweak or write on top of that.
Load every synth track first, then write notes. Live's instruments only when the library has
nothing for that part (say so). **Drums are not Chatmu Sound** (no noise source, no percussion
presets): use a Live Drum Rack / kit or samples; a Chatmu Sound 808 can sit under it as the low end.

