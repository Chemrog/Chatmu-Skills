---
name: chatmu-distribution
description: >
  Use when an artist or manager wants to distribute music to DSPs (Spotify, Apple Music, Deezer, etc.),
  upload a single or EP, fill out release metadata, configure credits, or submit a release for distribution review.
  Trigger phrases: "distribute my song", "release song", "subir canción a Spotify",
  "distribuir música", "lanzar sencillo", "upload WAV to distribution".
compatibility: claude.ai
---

# Chatmu — Music Distribution & DSP Submission Skill
**Version:** 1.0  
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

## Standard Operating Procedure (SOP) — 6-Step Execution Flow

Follow this sequence strictly when assisting a user with music distribution:

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
4. Inform the user in an encouraging tone that the drop zone is ready for their audio (WAV/FLAC) and album cover artwork.

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
