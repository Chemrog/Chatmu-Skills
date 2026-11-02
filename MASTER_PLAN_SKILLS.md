# MASTER PLAN — Skills de producción musical del Co-Producer

Actualizado: 2026-11-02 (v2, tras el inventario completo) · Autor: Opus · Para: Chema

Objetivo: que el Co-Producer de Chatmu Desktop pueda hacer **cualquier canción que pida un
usuario** (cualquier género, mood o fusión) con buena melodía, armonía, arreglo, mezcla y master,
trabajando en Ableton paso a paso como una persona: cada paso se escucha, se puede interrumpir y
se puede deshacer. No es Suno: el agente toma decisiones de productor y las escribe con las tools
reales del bridge.

---

## 1. Inventario completo (conteo real)

Busqué en todos los sitios donde pueden vivir skills:

| Dónde | Qué hay | Skills |
|---|---|---|
| `Chemrog/Chatmu-Skills` · `main` | Todo el catálogo. **V3 sincroniza desde aquí** (`syncFromMarketplace` lee `main` en GitHub) | **77** |
| `Chatmu Skills` local, sin commitear | `chatmu-studio-world-scales` (DeepSeek) + `_bundles/` (7 `.md` = copias de las 7 de DeepSeek de `b3ea539`, no son skills nuevas) | **1** |
| Rama `feat/production-skills-opus` (esta) | `hook-melody`, `harmonize-melody`, `genre-oriental-hiphop` | **3** |
| Ramas `integrate/round3` | ya mergeada en `main`, sin diferencias | 0 |
| Marketplace de saasrock (`admin_list_skills`) | 13 skills de negocio antiguas (zips); ninguna de producción | 0 de producción |
| Repo de Chatmu Desktop (`release/0.1.74`) | No empaqueta skills; las pide a V3. Solo `bridge/skillLint.ts` (el linter) y skills de desarrollo `cp-author`, `cp-reviewer`, `cp-qa-browser` (para Claude Code, no para el Co-Producer) | 0 |
| Resto de `Chatmu_V2` | `chatmu-plugins/skills/chatmu-plugin-designer` (diseño de plugins, relacionado pero no de producción); el resto son skills de finanzas, paperclip, saasrock | 0 de producción |
| `Chatmu_V2/music-kb` | 10 "cards" de conocimiento de DeepSeek. **No son skills y no se publican** | — |

**Total: 81 skills.** De ellas, **46 son de producción musical / Co-Producer** (42 en `main` +
1 sin commitear + 3 de esta rama). Las otras **35** son de negocio, analítica, legal y
documentos (`chatmu-analytics`, `chatmu-contracts`, `cm-pdf`…): fuera del alcance de este plan,
no las toco.

### Chequeos automáticos sobre las 81
- **Tools inexistentes:** ninguna. Todas las `local_*` que nombran existen en el bridge 0.1.74
  (102 tools). Las pasé por `bridge/skillLint.ts`.
- **Linter:** 1 fallo — `chatmu-mix-compression` tenía `shortDesc` de 123 caracteres (máx. 120).
  **Corregido en esta rama.**
- **Referencias rotas a `music-kb`:** **10 skills** (las 8 de DeepSeek + `harmony-voicing` y
  `melody-over-chords`, a las que DeepSeek añadió el puntero). **Corregidas en esta rama** (ver §4).
- **Referencias a skills que no existen:** ninguna en `main`.
- **Hallazgo importante del sync:** V3 solo descarga `SKILL.md` de cada carpeta. Cualquier
  archivo extra (`reference.md`, licencias) no llega al agente. Todo el conocimiento tiene que
  estar dentro de `SKILL.md`.

---

## 2. Auditoría de las 46 skills de producción

Veredictos: **mantener** · **corregir** · **renombrar** · **fusionar** · **borrar**.
"Calidad" = juicio sobre el contenido (A: sólida y operativa, B: correcta pero incompleta,
C: delgada o con errores).

### 2.1 Operación de Ableton y del set (base técnica)
| Skill | Qué hace | Calidad | Veredicto |
|---|---|---|---|
| `chatmu-studio-compose-core` | Flujo de clips, mapa de pitch (60 = C3), escalas, reglas básicas de melodía | A | **Mantener.** Sus "Melody rules" se quedan como mínimo común; la melodía en serio va en `hook-melody` |
| `chatmu-studio-session-vs-arrangement` | Session vs Arrangement, mover ideas al timeline | A | Mantener |
| `chatmu-studio-listen-troubleshooting` | Escuchar con fiabilidad, `silent_capture` | A | Mantener |
| `chatmu-studio-record` | Grabar con count-in, Capture MIDI | A | Mantener |
| `chatmu-studio-export` | Exportar con verificación | A | Mantener |
| `chatmu-studio-automation` | Envolventes, automatización | A | Mantener |
| `chatmu-studio-drum-rack` | Montar y afinar un kit | A | Mantener |
| `chatmu-session-prep` | Preparar sesión para mezcla, buses, gain staging | A | Mantener |

### 2.2 Sonido (sintes, perfiles, audio)
| Skill | Calidad | Veredicto |
|---|---|---|
| `chatmu-studio-sound-design` (v2, de Chema) | A | Mantener |
| `chatmu-studio-synth` | A | Mantener |
| `chatmu-studio-clone-sound` | A | Mantener |
| `chatmu-studio-sound-profile-build` / `-edit` / `-produce` | A | Mantener (las tres) |
| `chatmu-studio-separate-stems` | A | Mantener |
| `chatmu-studio-remake-song` | A | Mantener |
| `chatmu-studio-verify-ai` | A | Mantener |
| `chatmu-studio-guide-vocal` | A | Mantener |
| `chatmu-studio-vocal-chops` | A | Mantener |

### 2.3 Composición: armonía y melodía
| Skill | Origen | Calidad | Problemas | Veredicto |
|---|---|---|---|---|
| `chatmu-studio-harmony-voicing` | Glincker (MIT) + correcciones | B | Puntero roto a `music-kb` (corregido); solo ~6 géneros | **Fusionar** con `harmony-functional` → `chatmu-studio-harmony` |
| `chatmu-studio-harmony-functional` | DeepSeek | B | Dependía de la card (corregido: contenido dentro); duplica a `harmony-voicing`; no usa `local_music_theory progression` | **Fusionar** (ver arriba) |
| `chatmu-studio-melody-over-chords` | Chema | A | Puntero roto (corregido); apuntaba a `melody-hooks` | **Mantener**, ahora apunta a `hook-melody` y `harmonize-melody` |
| `chatmu-studio-melody-hooks` | DeepSeek | C | Principios sin método; validación "que el usuario la cante"; sin `local_harmony_map` ni `local_sing` | **Borrar** — sustituida por `hook-melody` (**borrada en esta rama**) |
| `chatmu-studio-hook-melody` | Opus (esta rama) | A | — | Nueva |
| `chatmu-studio-harmonize-melody` | Opus (esta rama) | A | — | Nueva |
| `chatmu-studio-bass-lines` | Glincker + Chatmu | B | Pocos géneros | **Corregir** (ampliar por género cuando existan las skills de género) |
| `chatmu-studio-world-scales` (sin commitear) | DeepSeek | C | Card rota; prohíbe 12-TET y acordes occidentales (rompe el caso hip hop/trap con color árabe); pide pitch bends que el bridge no escribe | **Reescribir** (maqam/raga reales con drone; la fusión urbana ya está en `genre-oriental-hiphop`). No la toqué: es trabajo sin commitear de otra sesión |

### 2.4 Ritmo
| Skill | Origen | Calidad | Problemas | Veredicto |
|---|---|---|---|---|
| `chatmu-studio-drums-by-genre` | Glincker + correcciones | B | Grids de ~10 géneros, se solapa con templates y club-grooves | **Fusionar** en las skills de género (cada una trae su groove); hasta entonces se queda |
| `chatmu-studio-breakbeats` | DeepSeek | B | Card rota (corregido, los 13 elementos ahora están dentro) | **Corregir** — hecho |
| `chatmu-studio-afro-cuban-rhythms` | DeepSeek | B | Card rota (corregido, grids dentro) | **Corregir** — hecho |
| `chatmu-studio-club-grooves` | DeepSeek | B | Card rota (corregido); duplica tablas de drums-by-genre | **Fusionar** en `genre-house-techno` y `genre-dnb-garage` |
| `chatmu-studio-humanize` | Glincker | A | — | Mantener |

### 2.5 Forma y arreglo
| Skill | Calidad | Problemas | Veredicto |
|---|---|---|---|
| `chatmu-studio-song-structure` (Chema) | A | Se solapa con `arrangement` | **Fusionar** → `chatmu-studio-arrangement` |
| `chatmu-studio-arrangement` | A | Se solapa con `song-structure` (el linter ya les separó los papeles, pero el agente duda cuál usar) | **Fusionar** (es el nombre que se queda) |
| `chatmu-studio-drop-buildup` | A | Es una parte del arreglo electrónico | **Fusionar** como sección de `arrangement` (o mantener como sub-skill si la fusión supera ~300 líneas) |
| `chatmu-studio-genre-templates` | B | 6 géneros en una sola skill, superficial | **Borrar** cuando existan las skills de género (su contenido se reparte) |

### 2.6 Sampling
| Skill | Calidad | Problemas | Veredicto |
|---|---|---|---|
| `chatmu-studio-sampling` (DeepSeek) | B | Card rota; decía "chop con `local_ableton_create_audio_clip`" (esa tool no corta) | **Corregir** — hecho: flujo real con `local_stems_separate` + `local_ableton_clip` (markers, warp, pitch) |

### 2.7 Mezcla y master
| Skill | Calidad | Problemas | Veredicto |
|---|---|---|---|
| `chatmu-mixing-progressive` | A | — | Mantener |
| `chatmu-mix-eq` | A | — | Mantener |
| `chatmu-mix-compression` | A | `shortDesc` > 120 (corregido) | **Corregir** — hecho |
| `chatmu-studio-sidechain` | A | — | Mantener |
| `chatmu-studio-spatial-panning` (DeepSeek) | B | Card rota; "suma a mono" sin tool | **Corregir** — hecho: Utility Width 0 + `local_ears_listen` |
| `chatmu-studio-reference` | A | — | Mantener |
| `chatmu-master-chain` | A | — | Mantener |
| `chatmu-master-check` | A | — | Mantener |

### 2.8 Género
| Skill | Veredicto |
|---|---|
| `chatmu-studio-genre-oriental-hiphop` (esta rama) | Nueva — plantilla para las demás skills de género |

### Resumen de veredictos (46)
| Veredicto | Nº | Skills |
|---|---|---|
| Mantener | 27 | 2.1 (8), 2.2 (11), melody-over-chords, humanize, mixing-progressive, mix-eq, sidechain, reference, master-chain, master-check |
| Corregir (hecho en esta rama) | 5 | breakbeats, afro-cuban-rhythms, sampling, spatial-panning, mix-compression |
| Corregir (pendiente) | 1 | bass-lines |
| Fusionar | 7 | harmony-voicing + harmony-functional → `harmony`; song-structure + arrangement + drop-buildup → `arrangement`; drums-by-genre, club-grooves → skills de género |
| Borrar | 2 | melody-hooks (hecho), genre-templates (cuando existan los géneros) |
| Reescribir | 1 | world-scales |
| Nuevas (esta rama) | 3 | hook-melody, harmonize-melody, genre-oriental-hiphop |

Ninguna necesita **renombrarse** por sí sola: los nombres nuevos salen de las fusiones.

---

## 3. Catálogo objetivo (~45) mapeado contra lo que ya existe

Leyenda: ♻️ reutiliza tal cual · 🔧 se corrige/fusiona desde existentes · 🆕 nuevo de verdad.

### 3.1 Orquestación
| Skill objetivo | Estado | Sale de |
|---|---|---|
| `chatmu-studio-make-song` (brief → género → idea de 8 compases → arreglo → mezcla → master, con 3 aprobaciones) | 🆕 | — (usa todas las demás) |
| `chatmu-studio-genre-fusion` (cómo cruzar dos géneros sin collage) | 🆕 | — |

### 3.2 Composición
| Skill objetivo | Estado | Sale de |
|---|---|---|
| `chatmu-studio-compose-core` | ♻️ | igual |
| `chatmu-studio-hook-melody` | ✅ hecha | sustituye `melody-hooks` |
| `chatmu-studio-melody-over-chords` | ♻️ | igual (punteros corregidos) |
| `chatmu-studio-harmonize-melody` | ✅ hecha | — |
| `chatmu-studio-harmony` | 🔧 | `harmony-voicing` + `harmony-functional` + rearmonización (Felts, Levine) |
| `chatmu-studio-bass-lines` | 🔧 | ampliar por género |
| `chatmu-studio-counter-melody` (segundas voces, respuestas) | 🆕 | — |
| `chatmu-studio-lyrics-prosody` (letra que cae en la melodía) | 🆕 | — |
| `chatmu-studio-world-scales` | 🔧 | reescritura de la de DeepSeek; referencias de audio de Raga Guide (74 ragas) |

### 3.3 Ritmo y arreglo
| Skill objetivo | Estado | Sale de |
|---|---|---|
| `chatmu-studio-drum-rack`, `chatmu-studio-humanize` | ♻️ | igual |
| `chatmu-studio-breakbeats`, `chatmu-studio-afro-cuban-rhythms` | ♻️ | corregidas en esta rama |
| `chatmu-studio-arrangement` | 🔧 | `arrangement` + `song-structure` + `drop-buildup` |
| `chatmu-studio-sampling`, `chatmu-studio-vocal-chops` | ♻️ | sampling corregida |

### 3.4 Géneros (15) — una por familia, con BPM, groove en 16avos, armonía, melodía, sonidos del factory de Chatmu Synth, forma, mezcla objetivo y "qué lo arruina"
| Skill objetivo | Estado | Material existente que absorbe |
|---|---|---|
| `chatmu-studio-genre-pop` | 🔧 | sección Pop de `genre-templates` + `drums-by-genre` |
| `chatmu-studio-genre-rock` | 🆕 | — |
| `chatmu-studio-genre-dark-trap` | 🔧 | Trap de `genre-templates` / `drums-by-genre` / `harmony-voicing` |
| `chatmu-studio-genre-hiphop` (boom bap, lo-fi, moderno) | 🔧 | Lo-fi de `genre-templates`, `breakbeats` |
| `chatmu-studio-genre-oriental-hiphop` | ✅ hecha | — |
| `chatmu-studio-genre-reggaeton` | 🔧 | Reggaetón de `genre-templates`, dembow de `drums-by-genre`, ejemplo de `bass-lines` |
| `chatmu-studio-genre-ambient` | 🆕 | — |
| `chatmu-studio-genre-rnb` | 🔧 | R&B de `genre-templates` |
| `chatmu-studio-genre-house-techno` | 🔧 | `club-grooves`, Deep house de `genre-templates`, `sidechain`, `drop-buildup` |
| `chatmu-studio-genre-dnb-garage` | 🔧 | `club-grooves`, `breakbeats` |
| `chatmu-studio-genre-regional-mx` | 🆕 | (presets "Regional Mexican" del factory) |
| `chatmu-studio-genre-latin-tropical` | 🔧 | `afro-cuban-rhythms` |
| `chatmu-studio-genre-afrobeats-amapiano` | 🆕 | — |
| `chatmu-studio-genre-cinematic` | 🆕 | — |
| `chatmu-studio-genre-jazz` | 🔧 | ii–V de `harmony-voicing` |

### 3.5 Sonido, mezcla y master
| Skill objetivo | Estado |
|---|---|
| sound-design, synth, clone-sound, sound-profile ×3, separate-stems, remake-song, verify-ai, guide-vocal | ♻️ (10) |
| session-prep, mixing-progressive, mix-eq, mix-compression, sidechain, spatial-panning, reference, master-chain, master-check | ♻️ (9; dos corregidas aquí) |
| `chatmu-mix-by-genre` (balance objetivo por rol y género, medido con `local_ears_track_levels`) | 🆕 |
| `chatmu-mix-effects` (reverb, delay, modulación, saturación con intención) | 🆕 |

### Cuentas del catálogo objetivo
- **Reutilizadas tal cual (o ya corregidas):** 32
- **Corregidas por fusión/ampliación:** 4 (`harmony`, `arrangement`, `bass-lines`, `world-scales`)
  + 8 géneros que nacen del material existente
- **Ya hechas en esta rama:** 3
- **Nuevas de verdad:** 12 (make-song, genre-fusion, counter-melody, lyrics-prosody, rock,
  ambient, regional-mx, afrobeats-amapiano, cinematic, mix-by-genre, mix-effects, + world-scales
  si se cuenta como reescritura completa)
- **Desaparecen:** melody-hooks (hecho), harmony-functional, song-structure, drop-buildup,
  genre-templates, drums-by-genre, club-grooves (tras fusionar)

Resultado: de 46 hoy a ~56 al final, sin duplicados.

---

## 4. Lo que corregí ya en esta rama
- **Referencias rotas a `music-kb` (10 → 0):**
  - `breakbeats`, `afro-cuban-rhythms`, `club-grooves`, `harmony-functional`, `sampling`,
    `spatial-panning`: el contenido de su card va ahora dentro de la skill (sección
    "Reference"). Es el conocimiento de DeepSeek, revisado; las tablas ya no se pierden en prod.
  - `harmony-voicing`, `melody-over-chords`: puntero cambiado a las skills reales.
  - `melody-hooks`: borrada (la sustituye `hook-melody`).
  - `world-scales`: sin commitear en otra sesión; se reescribe en una tanda posterior.
- **Tools mal usadas:** `sampling` (chop real con `local_ableton_clip`) y `spatial-panning`
  (comprobación mono real).
- **Linter:** `mix-compression` `shortDesc` ≤ 120.
- Las 81 pasan el linter del Desktop (tools reales de `release/0.1.74`).

**Ojo al mergear:** `bridge/skillLint.test.ts` del Desktop exige que la lista de carpetas
`chatmu-studio-*` coincida con su tabla `STUDIO_KEYWORDS`. Hay que añadir las 3 nuevas y quitar
`melody-hooks` en ese archivo (repo Desktop) o el test falla.

---

## 5. Por qué la música hecha por IA "no engancha" (guía de todas las skills de composición)
1. **Elige la nota más probable cada vez** → correcto y olvidable. La memoria musical funciona
   por predicción + sorpresa moderada (Huron). Solución: una sorpresa planeada por frase.
2. **No tiene motivo** → 8 compases de material nuevo. Solución: motivo de 1–2 compases repetido
   y variado.
3. **Ritmo plano** (corcheas iguales, velocidad 100). Solución: ritmo firma con síncopa,
   anacrusa y silencios.
4. **Sin punto alto planeado.** Solución: un solo pico por sección, tarde y largo.
5. **Todas las frases cierran en la tónica.** Solución: pregunta (2/5/7) y respuesta.
6. **Registro único (MIDI 60–72).** Solución: registro por rol.
7. **Género genérico.** Solución: celdas rítmicas, intervalos y sonidos propios de cada género.

Regla común: **cada decisión musical debe tener una razón nombrable**. Si el agente no puede decir
por qué está esa nota, acorde o sonido, no lo escribe.

---

## 6. Formato de cada skill
- Frontmatter: `name` = carpeta, `description` con disparadores en inglés **y** español,
  `category: creative`, `subcategory: studio`, `shortDesc` ≤ 120, `tags` como lista de
  **strings**, `requiresTools` solo con tools registradas.
- **Todo dentro de `SKILL.md`** (el sync no lleva otros archivos).
- Estructura: cuándo usar → qué preguntar (mínimo) → flujo con tools → reglas duras →
  autocrítica → qué decirle al usuario.
- Cuerpo en inglés; el agente responde en el idioma del usuario.
- Conocimiento destilado de los libros con criterio propio, sin copiar texto.

---

## 7. Orden de trabajo
| # | Entrega | Estado |
|---|---|---|
| 1 | Inventario + auditoría + 3 skills + correcciones de referencias rotas (esta rama) | ✅ |
| 2 | Chema prueba `hook-melody`, `harmonize-melody`, `genre-oriental-hiphop` en Desktop | pendiente |
| 3 | `chatmu-studio-harmony` (fusión) | |
| 4 | `chatmu-studio-arrangement` (fusión de 3) | |
| 5 | Géneros pedidos: pop, rock, dark-trap, ambient, reggaetón, hiphop | |
| 6 | `make-song` + `genre-fusion` | |
| 7 | `mix-by-genre`, `mix-effects` | |
| 8 | Resto de géneros, `world-scales` reescrita, `counter-melody`, `lyrics-prosody`, `bass-lines` ampliada | |
| 9 | Borrar las fusionadas (cuando su reemplazo esté en `main`) | |

Cada tanda: rama → PR → prueba en Desktop → merge a `main` → `POST /api/skills/sync`.
**Nunca** sync a producción desde una rama.

### Criterio de "hecha"
1. Pasa el linter del Desktop (`CHATMU_SKILLS_DIR=<worktree> npx vitest run bridge/skillLint.test.ts`).
2. Probada en Ableton con 3 pedidos distintos.
3. Prueba ciega: ¿se recuerda la melodía al día siguiente? ¿Suena "a IA"?

## 8. Riesgos
- **Microtonos:** el bridge no escribe pitch bend; maqam real necesita sinte microtonal o tool nueva.
- **Validación melódica:** Ears no transcribe melodía; la autocrítica es simbólica + `local_sing`
  + el oído del usuario.
- **`music-kb`:** queda como cuaderno interno; nada en producción debe apuntar a ella.
- **Licencia Glincker (MIT):** 5 skills derivan de ella; la licencia vive en un `.txt` que el sync
  no lleva. Conviene una línea de crédito dentro de cada `SKILL.md` (ya la tienen en
  "Credits & license").
