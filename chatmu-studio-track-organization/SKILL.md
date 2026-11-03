---
name: chatmu-studio-track-organization
description: >
  Use in Co-Producer to organize the tracks of an Ableton Live set: rename,
  reorder, group, add a track to an existing group, ungroup and color by role.
  Trigger phrases: "organiza las pistas", "ordena la sesión", "agrupa",
  "agrupa los drums", "mete el kick al grupo", "junta las pistas", "reordena",
  "mueve la pista", "renombra", "ponle nombre al grupo", "desagrupa",
  "colorea las pistas", "limpia la sesión", "organize my tracks", "group the
  drums", "add to group", "reorder tracks", "rename tracks".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Rename, reorder, group and color Ableton tracks the way a producer does"
version: "1.0"
tags: ["studio", "ableton", "tracks", "group", "organize", "co-producer"]
requiresTools: ["local_ableton_tracks", "local_ableton_edit_track", "local_ableton_move_track", "local_ableton_group_tracks", "local_ableton_color"]
---

# Chatmu Studio — Organize tracks
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live. Moving and grouping are
macOS only today and need the «Organizar pistas en Live» switch + Accessibility.

Tested by hand on Live 12 (2 nov 2026) with the same keys the bridge uses.

## What a producer does, and what the tools do instead

A person clicks a track, Shift+clicks to select a contiguous range or Cmd+clicks
(Ctrl on Windows) to pick tracks that are apart, then drags them together and
presses Cmd+G. The bridge can't click or drag reliably, so:

| Person | Agent |
|---|---|
| Cmd+click tracks that are apart, drag them together | `local_ableton_move_track` — one move per track, in one batch |
| Shift+click a range, Cmd+G | `local_ableton_group_tracks` with `firstIndex..lastIndex` |
| Pick scattered tracks and group them at once | `local_ableton_group_tracks` form (b) `tracks: [{index, expectName}]` (moves them together, then groups) |
| Double-click the name, type | `local_ableton_edit_track` `{ action: "rename" }` — works on groups too, any time |
| Right-click → color | `local_ableton_color` (several tracks/groups in one call) |

## Step 0 — always: read, then rename auto-named tracks

1. `local_ableton_tracks` → names, indexes, which are groups, who is inside what.
2. **Live's automatic names carry a number that Live rewrites when tracks move**:
   `1-MIDI`, `2-Audio`, `3-Drum_Loop_6_120_BPM` (every sample dragged from Splice or the
   browser gets one). Group or move anything and they become `2-…`, `3-…`, `4-…`. The
   move/group tools check names after acting, see the renumbered name as "the wrong
   track", and undo work that was actually right.
3. So before moving or grouping, rename every track whose name starts with `N-`
   to a clean name (`3-Drum_Loop_6_120_BPM` → `Drum Loop`, `2-Hat_Loop_Zain_Wolf_120` →
   `Hats`). A name set by hand is never renumbered. Renaming is non-destructive and
   needs no approval. Tell the user in one line ("les pongo nombres limpios para
   poder ordenarlas").
4. Read `local_ableton_tracks` again after any move, group or rename: indexes
   shift. Never reuse an index from before.

## Step 1 — decide the order

Default layout for a song (left to right in Session = top to bottom in Arrangement):

1. **Drums** — kick, snare/clap, hats, percussion, loops
2. **Bass** — bass, sub, 808
3. **Music** — keys, piano, guitars, chords, pads, synths, leads
4. **Vocals** — lead, doubles, harmonies, chops
5. **FX** — risers, impacts, ear candy

Inside a family: low to high, or most important first (kick before hats). If the user
already has an order they like, keep it and only group. Say the plan in one line
before acting ("Drums: Kick, Snare, Clap, Hats → Bass → Music: Piano, Pad → Vocal").

## Step 2 — reorder

`local_ableton_move_track` with all the moves in ONE batch (one approval).
Each move's `index` and `toIndex` refer to the list **after** the previous moves,
so plan them in order on a copy of the list:

```
start:  Kick, Bass, Hats, Piano, Snare, Pad, Vocal, Clap
move Snare 4→2:  Kick, Bass, Snare, Hats, Piano, Pad, Vocal, Clap
move Clap  7→3:  Kick, Bass, Snare, Clap, Hats, Piano, Pad, Vocal
move Bass  1→4:  Kick, Snare, Clap, Hats, Bass, Piano, Pad, Vocal
```

Rules (seen in Live):
- A track moves among its **siblings** only. A top-level track jumps OVER a whole
  group, it never enters it. A track inside a group stays inside it.
- Moving a group moves everything in it.
- Returns and the Main/Master can't be moved or grouped. Say so, don't try.

Form (b) of `local_ableton_group_tracks` does the gathering for you when the only
goal is a group; use `move_track` when the order itself matters.

## Step 3 — group

`local_ableton_group_tracks` `{ firstIndex, lastIndex, expectNames, name }` on a
contiguous range, after Step 2. Starting at index 0 is fine. The new group appears at
`firstIndex` and everything after it shifts +1: if you group Drums (0–3) and then
want Music, the Music range is now one higher. Re-read first.

The group comes out named, with no devices and sends at -inf. To rename it later:
`local_ableton_edit_track` rename on the group's index.

## Add a track to an existing group

There is no "add to group" in Live's API, and a track can't be moved into a group.
What works:
1. Move the track right next to the group (just after its last child, or just before
   the group) with `move_track`.
2. Ungroup the group (Live: select the group, Cmd+Shift+G). Its children stay in
   place. **The group's own devices, color and name are lost**, so tell the user first if
   the group has devices on it.
3. Group the new range again with the same name.

If the bridge has no ungroup step yet, say so in one line and ask the user to select
the group and press Cmd+Shift+G (or right-click → Ungroup), then continue.

## Step 4 — color

`local_ableton_color` in one call, group and its tracks the same color. Use the
user's preference if known; default: drums red, bass orange, keys/chords yellow,
leads green, pads blue, vocals pink/purple, FX gray. Don't touch returns.

## When a move or group fails

- Read the error: it says what Live ended up with. Don't report "it failed" if the
  error says a group was created and then undone — say what happened.
- Re-read `local_ableton_tracks`. If names changed from `1-…` to `2-…`, that is
  the renumbering above: rename (Step 0) and retry once.
- `needs_permission` → one line: press «Permitir» in the card. Never write
  System Settings paths. On Windows these tools are not available yet: say so.
- A plug-in window open steals the keys; the bridge hides them, but if it keeps
  failing ask the user to close plug-in windows and retry.

## Don'ts

- Don't move or group with stale indexes. Read, act, read.
- Don't ungroup a group that has devices on it without telling the user.
- Don't reorder the user's session "because it looks better" unless they asked to
  organize it; grouping alone is less invasive.
- Don't say the LOM can't rename groups: it can (`edit_track` rename).
