---
name: chatmu-session-prep
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) BEFORE mixing, to prepare
  the session with Progressive Mixing: recon of every track by role, readable
  names, a stable mixer order, the bus tree DRUMS / MELODIC / VOCALS (groups),
  gain staging (school A or B), zero armed tracks and solos, sane sends, and a
  before/after measurement on the same bars. Reversible and measurable: it
  never moves the creative balance and never adds EQ or compression. Also a
  "solo ordenar" mode (organize only: names, colors by role, order, groups,
  empty/duplicate tracks — no gain staging, no buses processing). Trigger
  phrases: "ordena mi sesión", "ordena mi mezcla", "organiza mi mezcla",
  "solo ordénala", "ponle nombres y colores", "nombres y colores", "colores
  por rol", "agrupa lo melódico", "los drums a la izquierda", "quita las
  pistas vacías", "pistas duplicadas", "prepara la sesión", "preparar la sesión para mezclar", "ordena la
  sesión", "limpia la sesión", "organiza las pistas", "renombra las pistas",
  "agrupa las pistas", "crea los grupos", "buses", "gain staging", "ganancia",
  "headroom", "deja la sesión lista para mezclar", "antes de mezclar",
  "session prep", "prep my session", "clean up my session", "organize my
  tracks", "rename tracks", "group tracks", "set up buses", "gain staging",
  "get ready to mix", "Progressive Mixing", "mezcla progresiva", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Prepare an Ableton session to mix: roles, names, order, DRUMS/MELODIC/VOCALS buses, gain staging"
version: "1.3"
tags: ["studio", "ableton", "mixing", "mezcla", "session-prep", "gain-staging", "buses", "organize", "ordenar", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_tracks", "local_ableton_status", "local_ableton_devices", "local_ableton_device_params", "local_ableton_edit_track", "local_ableton_color", "local_ableton_mixer", "local_ableton_apply", "local_ableton_group_tracks", "local_ableton_move_track", "local_ableton_load_devices", "local_ableton_set_device_param", "local_ableton_tempo_map", "local_ableton_transport", "local_ableton_song", "local_ableton_undo", "local_ableton_move_device", "local_ableton_lom", "local_ears_ensure_plugin", "local_ears_listen"]
---

# Chatmu — Session Prep (Progressive Mixing, part 1)
**Version:** 1.1
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live (AbletonOSC + AbletonMCP control surfaces) + Chatmu Ears.
**Continues with:** `chatmu-mixing-progressive` (bus chains, family mix, depth). **Listening checks:** `chatmu-studio-listen-troubleshooting`.

## What this skill does

Progressive Mixing mixes by families, smallest to largest, bottom-up, until the whole song
fits in **3 top faders: DRUMS · MELODIC · VOCALS**. This skill is the verifiable half: it
leaves the session clean, ordered, grouped and gain-staged, and measures it. Everything here
is reversible and measurable. **It never moves the creative balance, never adds EQ /
compression / reverb, in the same operation as cleaning the session.** The creative half is
`chatmu-mixing-progressive`.

Answer the user in their language (usually Spanish). Keep messages short; show plans as
tables.

## Modes (shared with `chatmu-mixing-progressive`)

| Mode | What runs | Writes |
|---|---|---|
| `organize` ("solo ordenar") | phase 0 (recon, no listening needed) + phase 1 (names, colors, order, cleanup) + phase 3 steps 1–3 (groups) → short deliverable | names, colors, order, groups, empty/duplicate tracks (with OK). No faders, no Utility, no sends, no gain staging. |
| `prep` (**default**) | this skill: phases 0–3, then 7–8 | names, colors by role, solo/arm cleanup, sends sanitized, groups, gain-staging faders (school base value) + Utility trims. No balance moves, no EQ/comp chains. |
| `full` | this skill, then `chatmu-mixing-progressive` phases 4–8 | everything |
| `review` | `chatmu-mixing-progressive` review mode | none (diagnosis only) |

**`organize` triggers:** "ordena mi sesión / mi mezcla", "organiza mi mezcla", "ponle nombres
y colores", "agrupa lo melódico", "los drums a la izquierda", "solo ordénala". Run only
organize; at the end offer `prep` ("¿sigo con el gain staging?"). A request that mixes both
("ordénala y déjala lista para mezclar") is `prep`.

If the user just says "mezcla mi canción", run `prep`, deliver, and offer to continue with
`full`. Never jump to mixing on a session that has not passed the acceptance criteria below.

## HARD RULES

1. **Identity by name, always.** Live renumbers tracks after any create/delete/group.
   Re-read `local_ableton_tracks` (or the snapshot) right before every write batch and
   match each planned target by **name**, not by the index you saw earlier. Use
   `expectName` / `expectNames` / `expectTrackName` wherever a tool accepts it. If a name
   doesn't match the plan, stop and re-plan.
2. **Plan → OK → batch.** Show the plan (table) and get the user's OK before every batch of
   changes. One OK can cover a whole phase.
3. **Log every change for undo:** `tool · target (index + name) · property · old → new`.
   Old values come from the snapshot taken before the batch. Undo = re-apply the old values
   with `local_ableton_apply` (preferred, exact) or `local_ableton_undo` for the last Live
   operation(s) (say what will be undone).
4. **Bars and beats, never minutes.** Tempo may change inside the song; map sections in
   bars/beats (4/4: bar N starts at beat `(N - 1) * 4`). Use `local_ableton_tempo_map` to
   see tempo changes.
5. **Measurements from `local_ears_listen` are indicative** (stream captured pre-Master-
   fader at the plugin position). Use them only for before/after comparisons on the **same
   bars**. Never say "it meets -14 LUFS" from the stream (delivery numbers: see
   `chatmu-mixing-progressive`, phase 7).
6. **One listen at a time;** never parallel `local_ears_listen` calls.
7. **Approvals:** every device load needs an on-screen approval → batch loads with
   `local_ableton_load_devices` (up to 8, ONE approval). Deleting / creating tracks and
   `local_ableton_group_tracks` ask once per call; `local_ableton_move_track` asks once per
   batch. Tell the user "aprueba en la app".
8. **Not available:** Master sends (Live's Master has none). **Returns and the Master always
   stay at the right in Live** and can't be moved or grouped: plan around them and say so
   ("los returns y el Master siempre quedan a la derecha"). Reordering is
   `local_ableton_move_track`, grouping `local_ableton_group_tracks` (both experimental).
9. **Permissions: one line, never a path.** If `local_ableton_move_track` /
   `local_ableton_group_tracks` answer `needs_permission`, Chatmu Desktop shows a
   **«Permitir»** card in the chat: say in ONE line "Pulsa **Permitir** en la tarjeta de
   arriba y sigo" and retry when the app says it's granted. **Never write System Settings
   paths or permission steps in text.** (Outside Chatmu Desktop:
   `local_open_system_settings { pane }` opens the exact pane, then one line naming the switch.)
10. **Never say a Live feature "is not exposed"** (track colors, a device option, a routing)
    without `local_ableton_lom describe` on the object first.

---

## Phase 0 — Recon (read only)

`organize` mode: run steps 2, 4 and 5 only (no plugin check, no tempo map, no listening).

1. `local_ears_ensure_plugin` `{ install: false }` (check only) and `local_ableton_status`.
2. `local_ableton_snapshot` (compact). Keep it as the **"before" photo** for the log.
   Note: track type, devices, clips (Session + arrangement summary), mute/solo/arm,
   volume/pan/sends, groups (`isFoldable`, `isGrouped`, `groupTrackIndex`), returns, the
   `master` block (volume in dB), locators, tempo, time signature.
3. `local_ableton_tempo_map` → if `automated: true`, list the tempo events (beat → bpm). It
   reads the **last saved** .als: if `savedAt` is older than the user's recent work, ask
   them to save (Cmd+S) and read again.
4. **Classify every track by role** using name, devices (Drum Rack, Simpler, bass synth,
   vocal chain…), clip names and type. Families:
   - **DRUMS:** kick, snare, clap, hats, toms, cymbals, percussion, drum loops.
   - **MELODIC → BASE:** bass, 808 (as bass), guitars.
   - **MELODIC → KEYS:** coros (harmonic backing/choir layers), chords, piano, harps, pads.
   - **MELODIC → LEAD:** lead synths, melodic hooks, riffs.
   - **VOCALS:** lead vocal, doubles, vocal chops, vocal ambiences.
   - **FX aux:** return tracks (reverb/delay). They are NOT a top fader.
   - **Unclear:** solo-listen it on the reference bars (one short listen) or ask.
5. Flag **duplicates** (same name, or same clips/devices), **empty tracks** (no clips in
   Session or Arrangement), muted-forever tracks, armed tracks, solos, and sends ≥ ~0.8 on
   tonal tracks.
6. **Pick the reference bars** with the user: the densest section (usually the chorus/drop),
   8 bars, e.g. "compases 33–40". Convert to beats. All before/after listens use exactly
   this range.
7. **"Before" measurement:** set the loop to the reference bars (`local_ableton_song`
   `loopStart`/`loopLength` in beats, `loop: true` — note the old loop to restore it),
   `local_ableton_transport` `{ action: "play", fromBeat }`, then `local_ears_listen`
   `{ seconds: 8–15 }`. Record LUFS (indicative), true peak, crest/dynamics.

Show the user a **map** table: `# · current name · role · family/bus · issues`.

## Phase 1 — Housekeeping (names, order, cleanup, group proposal)

**Decision point — ask in one message:** naming convention OK? delete empty/duplicate
tracks or just mute and leave them at the end? "coros" go to KEYS (method default) or with
VOCALS? Any track the user wants outside the tree?

1. **Names:** readable role names, short, unique: `Kick`, `Snare`, `Hats`, `Perc Shaker`,
   `Bass`, `Gtr L`, `Gtr R`, `Keys Piano`, `Pad`, `Coros`, `Lead Synth`, `Hook`,
   `Lead Vox`, `Vox Double`, `Vox Chops`. After OK: `local_ableton_edit_track`
   `{ action: "rename", index, name }` per track (no approval). Re-read names after.
2. **Cleanup:**
   - Disarm every armed track: `local_ableton_mixer` `{ index, property: "arm", on: false }`
     (arm writes may ask an approval).
   - Clear accidental solos (confirm none is intentional): one `local_ableton_apply` batch of
     `{ type: "mixer", track, property: "solo", on: false }`.
   - Empty/duplicate tracks: only with explicit OK, `local_ableton_edit_track`
     `{ action: "delete", index, expectName }` (approval each). Default: leave them muted at
     the end of the set and list them in the deliverables.
3. **Colors by role** (every mode that writes: organize, prep and full; skip only if the user
   says not to touch colors): one color per
   family, the same for every track of the family **and its group**.
   - **Palette:** use the user's saved color preference (memory or the artist's notes). If
     there is none, propose the default and ask only this first time: drums red, bass
     orange, keys/chords yellow, leads/melody green, pads/atmosphere blue, vocals pink (or
     purple), FX gray; returns stay as they are. When they answer (or say "como quieras"),
     save it with `save_memory` (e.g. "Colores por rol: drums rojo, bajo naranja…") so you
     never ask again.
   - **Apply:** ONE `local_ableton_color` call for the whole session:
     `{ targets: [{ trackIndex, expectName, color: "rojo" }, ...] }` (names es/en,
     `#RRGGBB` or palette index 0-69; up to 64). Add `alsoClips: true` when the user wants
     the clips to match too. The result reports the `colorIndex` Live stored for each one;
     `local_ableton_tracks` shows each track's `colorIndex` before and after.
   - A target with `ok: false` (e.g. a renamed track) changed nothing: re-read the tracks
     and retry only that one.
4. **Order:** show the user the exact target order as a numbered list of track **names**,
   top to bottom, family by family:
   DRUMS (Kick → Snare/Clap → Hats → Perc) · BASE (Bass → Guitars) · KEYS · LEAD ·
   VOCALS (Lead Vox → Doubles → Chops → Ambiences). With their OK, reorder with
   `local_ableton_move_track` `{ moves: [{ index, expectName, toIndex }, ...] }` (≤ 16
   moves, ONE approval; each move's indexes refer to the list after the previous moves;
   a track only moves among its siblings — if the error lists valid `toIndex` values, use
   one of them). Then `local_ableton_tracks` and compare name by name.
   The order is for the track list only: returns and the Master stay at the right
   (rule 8). If a move answers `needs_permission`: rule 9.
   **Fallback** (tool missing, disabled or failed for another reason): "Arrastra las pistas
   en Live a este orden y avísame", then re-read and compare.
5. **Group proposal:** the bus tree table (built in phase 3):

```
DRUMS    ← all drums + percussion
MELODIC  ├ BASE  ← bass + guitars
         ├ KEYS  ← coros, chords, harps, pads
         └ LEAD  ← leads and hooks
VOCALS   ← lead vocal, chops, vocal ambiences
FX aux   ← returns (not a top fader)
Top faders: DRUMS · MELODIC · VOCALS   (exactly 3)
```

**The bass never goes to the top.** It lives in MELODIC → BASE; a 4th top fader breaks the
method. If the user insists, explain once, then respect their decision and log it.

## Phase 2 — Gain staging

**Decision point — ask:** "¿Escuela A o B?" Default **B**.

| School | Track faders | Master fader |
|---|---|---|
| **A** | 0 dB | -10 dB |
| **B** (default) | -9 to -10 dB | 0 dB |

**Rule:** per-track level corrections go in a **Utility at the start of the chain**, not on
the fader. The fader is for balance (later, in the mixing skill).

1. **Faders to the school's base value.** `local_ableton_mixer`
   `{ index, property: "volume", db: -10 }` on the first track → note `observedValue`; then
   one `local_ableton_apply` batch for the rest with that `value` (0..1), each change for a
   track you just re-verified by name. Check `observedDb` in the results / snapshot.
   Master: `local_ableton_mixer` `{ target: "master", property: "volume", db: -10 }`
   (school A) or `db: 0` (school B). Group tracks (later) stay at 0 dB.
2. **Measure by family** on the reference bars: solo the family's tracks (one apply batch,
   `solo: true`), play from the reference beat, `local_ears_listen` 8 s, then un-solo.
   Measure single tracks only for outliers (a family that reads much hotter than the others,
   or one track that obviously jumps out). Working values to propose (adjust with the user):
   no soloed track or family above about -6 dBTP on the stream; full mix leaving about
   3–6 dB of headroom below 0 dBTP.
3. **Trims:** for each track that needs it, a Utility. Batch the loads:
   `local_ableton_load_devices` `{ loads: [{ target: "track", trackIndex, name: "Utility",
   expectTrackName }, …] }` (≤ 8 per call, one approval). Then:
   - `local_ableton_devices` on each track: if the Utility didn't land **first**, move it:
     `local_ableton_move_device { action: "move", trackName, deviceName: "Utility",
     expectName: "Utility", position: 0 }` (one undo step).
   - `local_ableton_device_params` → read the `Gain` parameter (`display_value`), set it in
     real units with `local_ableton_set_device_param { trackName, deviceName: "Utility",
     param: "Gain", display: "-3 dB" }` (or `local_ableton_apply` `device_param` +
     `display` for several at once) and report what Live read back. Re-listen: the
     measurement is the truth, not the parameter number.
4. **School A note:** the stream is pre-Master-fader, so it reads about 10 dB hotter than
   what leaves the Master. Compare like with like and say so.

## Phase 3 — Bus tree (groups) + FX aux + sends

1. Re-read `local_ableton_snapshot` (names, indexes, existing groups).
2. **Group, inner to outer:** BASE, KEYS, LEAD, then MELODIC (those three groups), then
   DRUMS, then VOCALS. Show the list first and get OK. For each group:
   - **Tracks not next to each other** (the usual case before reordering): form (b),
     `local_ableton_group_tracks { tracks: [{ index, expectName }, …], name: "DRUMS" }` —
     the bridge first moves them together right after the first listed track, then groups
     them. No need to reorder by hand first.
   - **Already contiguous:** form (a), `{ firstIndex, lastIndex, expectNames: [every name
     in the range, in order], name }`. Idempotent (`reused: true` if that range already is
     one group).
   One approval per call (none under «Recomendado»). **Re-read the snapshot after every
   group** — indices shift (+1 after the group, and form (b) moves tracks). Returns and
   the Master can't be grouped (rule 8). `needs_permission` → rule 9.
3. **Fallback (tool disabled, or it failed and undid itself for another reason):** ask
   the user to do it by hand, with the exact names: "En Live, haz clic en **Kick**,
   Shift+clic en **Perc Shaker** (si no están juntas: Cmd+clic en cada una), pulsa **Cmd+G**
   (Ctrl+G en Windows) y llama al grupo **DRUMS**." One group per message. Then verify with `local_ableton_snapshot`: the group
   has `isFoldable: true`, and every child has `isGrouped: true` and `groupTrackIndex` =
   the group's index. Rename with `local_ableton_edit_track` `rename` if needed.
4. **Group faders at 0 dB** (`local_ableton_mixer` `db: 0`); groups start empty (no devices).
5. **FX aux:** list the existing returns and what they hold. Don't create returns or load
   reverbs here (that's depth, in the mixing skill).
6. **Sanitize sends:** no tonal element (bass, keys, leads, vocals) at 100 % reverb; flag
   sends ≥ ~0.8 and propose sane values (e.g. 0.1–0.35). Apply with one
   `local_ableton_apply` batch of `{ type: "mixer", track, property: "send", sendId, value }`
   after OK. A send that is clearly an effect (a throw, a 100 % wet FX track) → ask.

## Phase 7 — Verification (same bars)

1. `local_ableton_snapshot` → check the acceptance list below.
2. "After" listen with the **same** loop, start beat and seconds as the "before" one.
3. Report before → after: LUFS (indicative), true peak, crest/dynamics; no clipping.
4. Restore the user's previous loop settings (`local_ableton_song`) and stop playback if you
   started it.

## Phase 8 — Deliverables

Give these in chat (only if the user asks for a file: `local_write_file` into a folder they
granted):
1. **Map:** final order, name, role, bus, Utility trim.
2. **Plan:** what `chatmu-mixing-progressive` would do next (chains per bus, order of the
   progressive mix, depth F1/F2/F3).
3. **Change log:** every change, old → new (rule 3), and how to undo.
4. **Artist's decisions still open:** e.g. tracks left muted, "coros" placement, school
   choice, sends that look intentional, anything you didn't touch.

## Acceptance criteria — "sesión preparada"

- [ ] Every track has a readable role name.
- [ ] Mixer order stable and documented (verified by name).
- [ ] Bus tree built; top faders = DRUMS · MELODIC · VOCALS (bass inside MELODIC → BASE).
- [ ] Gain staging applied (school A or B) and measured, no clipping.
- [ ] Zero armed tracks, zero accidental solos.
- [ ] Sends sanitized (no tonal element at 100 % reverb).
- [ ] Before/after measurement on the same bars.
- [ ] Explicit list of what remains the artist's decision.

## Organize mode — deliverable

Short: the final order (names, family, color), the groups created, what was renamed,
tracks deleted or left muted at the end, and "los returns y el Master quedan a la derecha".
Verification is the snapshot (no listening needed: nothing that sounds was changed). Then
offer `prep`.

## Don'ts

- Don't move balance faders, pans or add EQ/compression/reverb here.
- Don't delete anything without explicit OK and `expectName`.
- Don't trust an index from an earlier read after any structural change.
- Don't claim delivery loudness from the stream.
- Don't leave solos, loops or playback in a state the user didn't have.
