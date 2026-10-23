---
name: chatmu-distribution
description: >
  Use when an artist or manager wants to distribute music to DSPs (Spotify,
  Apple Music, Deezer, etc.), upload a single or EP, fill out release metadata,
  configure credits, or submit a release for distribution review. Trigger
  phrases: "distribute my song", "release song", "subir canción a Spotify",
  "distribuir música", "lanzar sencillo", "upload WAV to distribution",
  "te mando el master", "sube mi canción por WhatsApp".
compatibility: claude.ai
category: ops
subcategory: distribution
shortDesc: >-
  Distribute music to DSPs, upload singles/EPs, fill metadata, and submit for
  review
---

# Chatmu — Music Distribution & DSP Submission Skill
**Version:** 1.1  
**Required MCP:** Chatmu 3.5 MCP  
**For:** Independent artists and label managers uploading and distributing tracks to global streaming platforms.  
**Repository:** github.com/Chemrog/Chatmu-Skills

---

## What does this Skill do?

It guides artists and record labels through the complete end-to-end music distribution workflow on Chatmu. It transforms the technical process of presigned uploads, audio feature extraction, lyric transcription, metadata hydration, and DSP submission into a smooth, encouraging, and friendly experience.

---

## Tone & Communication Guidelines

- **Artist-Centric & Encouraging:** Speak like a dedicated label manager / executive. Focus on celebrating the artist's new music.
- **Clear Next Steps:** Never leave the user hanging. Always explain what happens next in simple, non-technical language.
- **Never Overwhelm:** Do not mention internal cloud storage endpoints (presigned S3/R2 URLs, JSON schemas, UUID hashes). Keep technical mechanics invisible.

---

## Which flow?

- **On WhatsApp** (the conversation is on the WhatsApp channel): follow **the WhatsApp flow** below. The upload widget and the metadata wizard do not exist there — never call `open_distribution_uploader`, `open_distribution_wizard`, `get_distribution_upload_urls` or `proxy_r2_upload_chunk`.
- **On the web**: follow the **6-step SOP**.

---

## WhatsApp flow (singles only)

This version handles **singles only** (one song). If the user wants an EP or album, tell them it is coming soon on WhatsApp and that they can do it today from chatmu.io.

### W1 — Check the limits BEFORE asking for any file
Never let the user send a 60 MB master and then find out they cannot release.
1. `get_saved_artists_for_distribution` → pick the primary artist (ask if there are several).
2. `get_artist_distributions` → if there is already a **draft**, reuse it (only 1 new release per month; `start_music_distribution_draft` answers 429 otherwise). If the artist's last submitted/approved/published release is less than **30 days** before the date they want, say so now.
3. The release date must be **at least 14 days from today**. Mention it when you ask for the date.
4. No draft yet → `start_music_distribution_draft` and keep the `releaseId`.

### W2 — Ask for the files, with the specs
Whenever the user asks how to send the song (or before they send it), give them the specs in one short message:

> *Master:* archivo WAV (no MP3, no FLAC), 44.1 kHz o 48 kHz, 16 o 24 bits, estéreo, máximo 100 MB.
> *Portada:* JPG o PNG, cuadrada, mínimo 3000 × 3000 px, en RGB, sin logos de plataformas ni URLs.
> Mándalos *como documento* (clip 📎 → Documento), no como foto ni como audio: WhatsApp comprime las fotos y los audios y ya no sirven para distribuir.

If a file is over 100 MB, WhatsApp cannot carry it: the user uploads it from the release page on chatmu.io.

### W3 — Attach each file as it arrives
The message a file arrives in gives its workspace path. Call `attach_file_to_release` with the `releaseId`, `kind` (`"audio"` for the WAV, `"artwork"` for the cover) and that `path`.
- It validates and moves the file. If it reports errors, explain them in plain words (e.g. "tu WAV está a 22 kHz, expórtalo a 44.1 kHz") and ask for a corrected file. Mention any warnings.
- A file that arrived as a **photo** or a WhatsApp **audio** is compressed: do not try to attach it; ask for it again as a document.
- MP3, M4A or FLAC: ask for the WAV export.
- Never paste a file URL into `patch_distribution_metadata` — `submit_distribution_for_review` re-checks every file and will reject it.

### W4 — Metadata in ONE numbered message
Send the user a single message with this numbered list (in their language) and ask them to reply **with the same numbers**. Fill in what you already know (artist name, the title in the file name) so they only confirm it.

```
Para terminar el lanzamiento, respóndeme con estos datos usando los mismos números:

1. Título de la canción:
2. Artista principal:
3. Artistas invitados (feat.) — opcional:
4. Género principal:
5. Género secundario — opcional:
6. Fecha de lanzamiento (DD/MM/AAAA, mínimo 14 días a partir de hoy):
7. Sello discográfico (o "Independiente"):
8. Línea © — año y titular de la composición (ej. "2026 Ana López"):
9. Línea ℗ — año y titular de la grabación (ej. "2026 Ana López"):
10. Idioma de la letra:
11. ¿Contenido explícito? (Sí/No):
12. ISRC — opcional (si no tienes, se asigna):
13. Intérpretes y su rol (ej. "Ana López — voz"):
14. Compositores / autores (ej. "Ana López — compositora y letrista"):
15. Productores (ej. "Beto Ruiz — productor"):
16. Letra — opcional (pégala aquí):
```

When they reply:
1. Parse it by number. If something required is missing or unclear (1, 2, 4, 6, 7, 8, 9, 13, 14, 15), ask **only for those numbers**, again numbered.
2. Check the date is ≥ 14 days away before saving it.
3. `patch_distribution_metadata` with: `albumName` (= song title, for a single), `primaryArtists` (uuid), `featuringArtists`, `primaryGenre`, `secondaryGenre`, `liveDate` (ISO), `labelName`, `cLine`, `pLine`, and `tracks: [{ trackNumber: 1, title, isrc, lyrics, audioLanguage, parentalAdvisory, contributors }]`. Contributors: 13 → category `performing`, 14 → `composition`, 15 → `production`, role = what they wrote. `parentalAdvisory` is `"Explicit"` or `"Not Explicit"`.
   Tracks are merged by `trackNumber`: do not resend the audio, it is already attached.

### W5 — Review and submit
1. Read back a short summary (title, artist, date, genre, credits) and ask for a yes.
2. `submit_distribution_for_review`. If it answers `missing_fields` or `media_errors`, explain each one simply and fix it (ask only for what is missing).
3. On success: the release is with the Chatmu team for review; share the `releaseUrl`.

---

## Standard Operating Procedure (SOP) — 6-Step Execution Flow (web)

Follow this sequence strictly when assisting a user with music distribution on the web:

### STEP 1 — Verify & Select Primary Artist
1. Execute `get_saved_artists_for_distribution` to retrieve authorized primary artists in the user's workspace.
2. If multiple artists exist, ask the user: *"Which primary artist are we releasing this song for?"*
3. Capture the exact `uuid` of the selected primary artist.

### STEP 2 — Initialize Distribution Draft
1. Call `start_music_distribution_draft` to create a fresh draft release in the system.
2. Save the returned `releaseId`.

### STEP 3 — Setup Upload Panel & Present Uploader
1. Call `get_distribution_upload_urls` with `releaseId` and `type: "audio"` to acquire presigned audio slots.
2. Call `get_distribution_upload_urls` with `releaseId` and `type: "artwork"` to acquire presigned artwork slots.
3. Call `open_distribution_uploader` passing the generated `audioUploadUrl`, `artworkUploadUrl`, `audioPublicUrl`, and `artworkPublicUrl`.
4. Inform the user in an encouraging tone that the drop zone is ready for their audio (WAV only — FLAC and MP3 are rejected at submission) and album cover artwork.

### STEP 4 — Confirm Uploads & Analyze Audio
1. Once the user confirms upload completion in the chat, call `confirm_distribution_uploads` with `releaseId`.
2. Analyze the uploaded track audio:
   - Call `analyze_raw_audio_url` to extract musical key, BPM, tempo, primary genre, and mood.
   - Call `transcribe_audio_url_lyrics` to obtain Whisper AI transcribed lyrics.

### STEP 5 — Persist Metadata & Launch Metadata Wizard
1. Call `patch_distribution_metadata` to persist all analyzed properties into the draft release:
   - `releaseId`, `albumName` (song title), `primaryGenre`, `artworkUrl`, `primaryArtists` (UUID array), `tracks` array (containing `audioUrl`, `lyrics`, `title`, and default `contributors`).
2. Call `open_distribution_wizard` with `releaseId` to open the pre-populated multi-step metadata form for the user to review release dates, ISRCs, C-Lines, P-Lines, and collaborator credits.

### STEP 6 — Final Review & Submission
1. Check the response from `patch_distribution_metadata` or `get_distribution_draft_details`.
2. If any mandatory fields remain in `missing_fields` (such as missing composition credits or release date), politely request those details from the user and patch them.
3. Call `submit_distribution_for_review` with `releaseId`.
4. When successful, present the final `releaseUrl` and congratulate the artist on submitting their music for global distribution!
