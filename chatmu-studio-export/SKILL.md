---
name: chatmu-studio-export
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) whenever the user wants a
  WAV/MP3 of their song, a range of it, or stems. Gets the real range from the
  arrangement clips, the duration from the export plan (never from arithmetic),
  checks tempo, saves straight into the folder the user wants (e.g. Descargas),
  and verifies the file is not silent, not gapped and the right length before
  delivering it. Trigger phrases: "exporta", "exporta la canción", "rebota",
  "rebotar", "saca el master", "quiero el WAV", "dame el audio", "para
  distribuir", "stems", "pistas separadas", "en MP3", "bounce", "render",
  "export my song", "ponlo en mis descargas", "pásalo a Descargas", "cópialo a
  mi escritorio".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Export the Ableton song (or a range / stems) to WAV/MP3 with the right range and duration, verified before delivery"
version: "1.3"
tags: ["studio", "ableton", "export", "bounce", "exportar", "wav", "mp3", "stems", "co-producer"]
requiresTools: ["local_ableton_status", "local_ableton_snapshot", "local_ableton_export", "local_ears_ensure_plugin", "local_ears_analyze_file", "local_copy_file", "local_list_access"]
---

# Chatmu Studio — Export (bounce)
**Version:** 1.3
**Requires:** Chatmu Desktop bridge + Ableton Live. Realtime needs the **Co-Producer Audio** plugin on the Master. Live's own exporter needs the setting in Chatmu Desktop + macOS Accessibility.
**Related:** chatmu-studio-listen-troubleshooting (playback/plugin checks), chatmu-studio-session-vs-arrangement. **Next:** chatmu-master-check (¿listo para distribuir?).

## What does this Skill do?

Give the user a WAV of the actual song (the right range, the right tempo, the real
duration) in the folder they want, and verify the file is usable before saying it is.
The failure mode is not "the export crashed": it is handing over a file that sounds
wrong, is silent, or sits somewhere the user cannot find, and calling it done.

Answer in the user's language (usually Spanish). Short messages, tables for the plan.

## HARD RULES

1. **The tool calculates the duration, not you.** Never state minutes from beats ÷ (bpm/60). Tempo may be automated or the Set's tempo may not be the project tempo. Get the duration from `action: "plan"`.
2. **Never pass a range you invented.** Round bar numbers ("1–128", "1–85") are almost always past the end of the music: Live stops and the export aborts with «playback stopped». No range = whole Arrangement up to the end of the last clip, the correct default for "la canción completa".
3. **The Set's end marker is not the end of the music.** The last beat with audio = max end across all arrangement clips (snapshot). The end locator can sit tens of seconds later.
4. **Read the tempo before exporting.** If it is not what the user expects (e.g. 151 BPM on a song written at 87), STOP. You have `local_ableton_set_tempo`, but never change tempo without the user saying the exact number.
5. **Ask the destination folder BEFORE exporting** (see Phase 1) and export straight there. If they ask afterwards, copy it with `local_copy_file` (never the terminal).
6. **Con el exportador de Live, la herramienta configura y verifica el diálogo; no confía en lo que Live recuerde.** Activa Live primero (macOS solo expone sus ventanas por Accesibilidad cuando está al frente), fija pista renderizada, WAV, profundidad, «Crear archivo de análisis» off, normalizar/mono off y MP3 si se pidió; lee Inicio y Duración y, si no coinciden con el plan, cancela y cae al bounce en tiempo real. Nunca prometas un rango que no se verificó.
7. **Realtime plays OUT LOUD.** Announce the duration, get a clear OK, tell the user not to touch Live while it runs.
8. **Never say "listo" from `state: done` alone.** Check silence, `lostFrames` (realtime) and the length (Phase 5).
9. **One export at a time;** it blocks the other Live tools. Poll every ~15 s, not in a tight loop.
10. **Never invent where a setting lives.** The only places are the ones written in this skill. If something is not here, say you are not sure instead of sending the user to a menu that may not exist.

## Phase 0 — Recon (read only, one batch)

- `local_ableton_status` → is Live playing? tempo? time signature? where is the playhead? loop on?
- `local_ableton_snapshot` (compact) → per track the arrangement clips (start/end in beats), mute/solo, master, locators. Last beat with audio = max clip end. In 4/4, bar N starts at beat (N-1)*4.
- `local_ears_ensure_plugin { install: false }` → is Co-Producer Audio on the Master?

Show a short recon:

| Dato | Valor |
|---|---|
| Tempo | 87 BPM (o "151 — ¿lo cambiaste tú?") |
| Último clip con audio | compás 77 (beat 304.5) |
| Final del Set (marcador) | compás 85 ← no es el final de la música |
| Plugin en el Master | sí / no |

If the tempo contradicts what the user told you about the song, ask before anything else.
If the plugin is missing and the method will be realtime: say so and offer `install: true` (asks approval). Do not start a realtime export without it.

**Con el exportador de Live:** la herramienta pone Live al frente antes de leer la línea base; si no, macOS no expone sus ventanas y la exportación fallaría. Pide al usuario que no toque el teclado ni el ratón mientras dura.

## Phase 1 — Range and destination

| El usuario dice | Argumentos |
|---|---|
| "la canción completa" / "toda" | nothing (default: whole Arrangement to the end of the last clip) |
| "del compás 1 al 40" | `start_bar: 1, end_bar: 40` (1-based, inclusive) |
| "los primeros 15 segundos" | `seconds: 15` |
| "de tal beat a tal beat" | `start_beats` / `end_beats` |
| "stems" / "pistas separadas" | `stems: true`: con exportador de Live = «Todas las pistas individuales» en **una sola pasada**; con realtime = N pasadas (soloando cada pista). `stem_tracks` (un subconjunto) siempre va en realtime. |
| "también en MP3" | `mp3: true` (same pass, no extra time) |

`tail_seconds` default 2 (reverb/release). `bit_depth` 24 by default; 32 only if they will master from it.

**Destination: ask where they want it, and export straight there.**
- Default: `~/Music/Chatmu Exports`.
- "en mis descargas", "para pasármelo al cel", "donde lo encuentre" → pass `folder: "<home>/Downloads"` (absolute path).
- If that folder is not granted yet, Chatmu Desktop shows an approval card: tell the user "te va a salir un permiso para guardar en Descargas, acéptalo".
- If they ask AFTER the export ("ponlo en Descargas"): `local_copy_file { source: <exported file>, destination: "~/Downloads" }` (one folder approval at most; never overwrites unless they ask). Copy the MP3 too if there is one. Report the new full path. Prefer copy over `local_move_file` (move needs write access on both folders). Never send them to the terminal or to menus that are not in this skill.

## Phase 2 — Plan (never skip)

`local_ableton_export { action: "plan", ...same range args }` → duration + announcement sentence. That number is the truth.

## Phase 3 — Confirm

One message: the announcement sentence, tempo, format, **folder**, and:
- it plays out loud, don't touch Live (realtime);
- roughly how long it takes (duration + tail; stems = N ×);
- MP3 in the same pass if they want it.

Wait for an explicit OK. A "sí" to an earlier unrelated question is not an OK for this.

## Phase 4 — Start and poll

`{ action: "start" }` with the same args → `jobId`. Then every ~15 s `{ action: "status", job_id }` until `done` / `failed` / `cancelled`. Say what it is doing once, not every poll.

## Phase 5 — Verify BEFORE delivering (all mandatory)

1. **State and warnings:** `state`, `warnings` (lost packets, restore problems).
2. **Not silent:** run `local_ears_analyze_file` with `loudness` on the exported WAV. Integrated loudness below about −60 LUFS (or true peak below −50 dBTP) = **the file is silent**. A silent file is never delivered: re-check `isPlaying` / the plugin / Session vs Arrangement (see chatmu-studio-listen-troubleshooting) and tell the user what happened. This is a real file, so its LUFS / true peak ARE delivery numbers (unlike a stream capture).
3. **No gaps:** `lostFrames / sampleRate` = seconds of silence inserted.

   | lostFrames | Veredicto |
   |---|---|
   | 0 | limpio |
   | < 0.05 s total | usable; mention it |
   | more | NOT deliverable: report it, don't hand it over as clean |

4. **Right length:** file duration vs plan duration (±2 s + tail). Wrong length = wrong range. En native, `lostFrames` no aplica (Live renderiza offline): aquí la comprobación que manda es duración = plan y que no esté silencioso.
5. **Live restored:** `local_ableton_status` → not playing, loop and playhead as they were before. If not, say so.

## Phase 6 — Deliver

Table: file · duration · rate/bit depth · size · **full path**. Para stems, una tabla por archivo (o el conteo + carpeta) y di explícitamente que el native incluye retornos/auxiliares. If it is for release ("para distribuir", "para Spotify"), offer `chatmu-master-check` on the main file. Plus one honest line on quality (loudness, any gaps). If it has problems, say how much silence and how many gaps and offer the fixes below. Never present a gapped or silent file as the master.

## Methods: realtime vs Live's exporter

- **Realtime (default):** plays the song through the Co-Producer Audio plugin and records it. Needs the plugin on the Master. Takes as long as the song.
- **Live's exporter (faster, no playback):** the user turns it on in **Chatmu Desktop → Ajustes → Co-Producer → tarjeta «Ableton Live» → sección «Exportar» → casilla «Exportar con el exportador de Live»** (not in Conectores; if the tool's `methodNote` names another place, use that). It also needs macOS Accessibility: if it's missing, Chatmu Desktop shows a **«Permitir»** card — tell the user in one line to press it. **Never write System Settings paths in text.** Then pass `method: "native"` (or leave `auto`). The tool activates Live, opens Export Audio/Video, sets **Rendered Track** (`Main`, o `Todas las pistas individuales` para stems), **WAV**, **24/32-bit**, **análisis off**, **normalizar/mono off** y **MP3** si se pidió. Después **verifica Inicio/Duración contra el plan**: si el diálogo recuerda otro rango, pulsa Esc y cae al bounce en tiempo real (rango exacto) en vez de entregar un archivo con otra duración. Al renderizar `Main` los efectos del master siempre entran; «Incluir efectos de retorno y del master» solo cambia el resultado de las pistas individuales. Los stems nativos exportan **todas** las pistas/canales (retornos y auxiliares incluidos) en una pasada.
- Last resort: the user exports by hand in Live, **File → Export Audio/Video** (Cmd+Shift+R).

## Multitrack (stems)

- **Native:** una sola pasada con «Todas las pistas individuales». Live escribe un WAV por pista/canal (incluye retornos y pistas auxiliares, p. ej. las de render) con el prefijo del nombre; según la versión, dentro de una subcarpeta. Cuenta los archivos, verifica que todos duren lo mismo que el plan y entrega la carpeta, no solo el primero.
- **Realtime:** una pasada por pista soleando. Úsalo si el usuario quiere **solo algunas** pistas (`stem_tracks`) o si el exportador de Live no está disponible.
- Si el usuario pide stems y el plugin no está en el Master, el realtime no puede; ofrece el exportador de Live (no necesita el plugin) o instala el plugin.

## Failure table (stop at the first row that explains it)

| Síntoma | Causa real | Arreglo |
|---|---|---|
| «playback stopped», aborts mid-way | range past the end of the music, or transport stopped | recompute the last clip; export without range |
| el exportador de Live se canceló y salió en tiempo real | el diálogo recordaba otro rango (Inicio/Duración ≠ plan) | es lo correcto: se entregó el rango exacto por realtime; no lo reportes como error |
| `errorCode: "silent_export"` (realtime stopped after ~6 s of silence, Live restored) | the range starts where nothing plays, or the music is in Session | move the range to where the clips are (snapshot) or fix Session vs Arrangement — don't retry the same range |
| file is silent, `lostFrames: 0` | the export never started playback / music is in Session, not Arrangement | check `isPlaying` in a re-run; chatmu-studio-session-vs-arrangement |
| hundreds of gaps ~20 ms | realtime stream drops packets | Live's exporter (setting above) or File → Export Audio |
| file sounds fast / short | Set tempo is not the project tempo | user confirms the tempo; fix in Live |
| «export in progress» stuck | a dead job died while restoring Live | reconnect the studio / restart the bridge, then re-read |
| aborts at the same second every time | the stream, not the range | note the second; change method, stop retrying blindly |
| plugin not streaming | Co-Producer Audio missing or disabled on Master | `local_ears_ensure_plugin` |
| "no encuentro el archivo" | exported to the default folder | give the full path; next time export into the folder they want |

Retry at most twice. Three identical failures = infrastructure: change method instead of repeating.

## Acceptance criteria — "la canción exportada"

- [ ] Range from the arrangement clips, or left empty
- [ ] Duration from `plan`, never by hand
- [ ] Tempo confirmed with the user when it looks off
- [ ] Saved in the folder the user wanted (asked before exporting)
- [ ] File checked not silent (loudness)
- [ ] `lostFrames` checked and translated to seconds
- [ ] File length matches the plan
- [ ] Si fue native: el rango del diálogo se verificó contra el plan (o cayó a realtime)
- [ ] Si fueron stems: se entregaron todos los archivos y se dijo que incluyen retornos/auxiliares
- [ ] Live left as it was (not playing, loop/playhead restored)
- [ ] Delivered with the full path and an explicit verdict on quality

## Don'ts

- Don't pass round bar numbers when the user asked for the whole song.
- Don't state minutes from beats/bpm arithmetic.
- Don't call it done from `state: done` alone.
- Don't tell the user to move files by hand or with the terminal: `local_copy_file`.
- Don't send the user to settings or menus that are not written here.
- Don't retry a third time without changing method.
- Don't tell the user the native exporter "uses whatever Live remembers": the tool sets and verifies the dialog.
- Don't deliver only the first file of a multitrack export.
