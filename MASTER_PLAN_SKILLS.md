# MASTER PLAN — Skills de producción musical del Co-Producer

Actualizado: 2026-11-02 · Autor: Opus (sesión de skills) · Para: Chema

Objetivo: que el Co-Producer de Chatmu Desktop pueda hacer **cualquier canción que pida un usuario**
(cualquier género, mood o fusión) con buena melodía, armonía, arreglo, mezcla y master, trabajando
en Ableton paso a paso como lo haría una persona: cada paso se escucha, se puede interrumpir y se
puede deshacer. No es Suno: el agente no "genera un audio", **toma decisiones de productor** y las
escribe con las tools reales del bridge.

---

## 1. Diagnóstico

### 1.1 El problema de fondo: por qué la música hecha por IA "no engancha"
Esto guía todo el catálogo, no solo la skill de melodía.

1. **Elige la nota más probable cada vez.** Un modelo de lenguaje escribe la melodía nota por nota
   eligiendo la opción "segura": grados conjuntos, nota del acorde en cada tiempo fuerte, frases de
   4 compases que terminan en la tónica. El resultado es correcto y olvidable. La memoria musical
   funciona por **predicción + sorpresa moderada** (Huron): si todo se cumple, el cerebro deja de
   prestar atención; si nada se cumple, se pierde. El gancho vive en el medio.
2. **No tiene motivo.** Escribe 8 compases de notas nuevas en vez de una idea de 1–2 compases que se
   repite y se transforma. Lo que se recuerda es la repetición con un cambio, no la cantidad de notas.
3. **Ritmo plano.** Todas las notas caen en la rejilla y duran lo mismo (corcheas a velocidad 100).
   Las melodías que enganchan tienen **una figura rítmica reconocible** (síncopa, anacrusa, silencio
   antes del golpe) que se reconoce aunque se cambien las notas.
4. **No hay punto alto planeado.** El pico de la melodía aparece por accidente o en cada frase.
5. **Termina todas las frases cerradas.** Sin una frase que "pregunte" (que acabe en 2, 5 o 7) no hay
   tirón hacia la siguiente.
6. **Ignora el registro y el instrumento.** Escribe en MIDI 60–72 siempre, sin pensar en dónde suena
   bien una voz, un sinte o un 808.
7. **Genérico por género.** "Trap = escala menor + hi-hats". Falta lo que hace que un género se
   reconozca: el lugar del acento, el tipo de intervalo, el color del sonido, cuánta repetición tolera.

Regla que sale de aquí y que aplica a todas las skills de composición: **cada decisión musical
debe tener una razón nombrable** (función, motivo, contraste, gancho). Si el agente no puede decir
por qué está esa nota/acorde/sonido, no lo escribe.

### 1.2 Lo que encontré en el repo
- 37 skills de estudio + 5 de mezcla/master en `Chatmu Skills`. La base operativa (clips, export,
  grabar, drum rack, session vs arrangement, sound design, sound profile, guide vocal) está bien y
  usa tools reales.
- **Las de DeepSeek** (commit `b3ea539` del 1 nov + `chatmu-studio-world-scales` sin commitear):
  `harmony-functional`, `melody-hooks`, `spatial-panning`, `afro-cuban-rhythms`, `club-grooves`,
  `breakbeats`, `sampling`, `world-scales`. Más las "cards" en `Chatmu_V2/music-kb/` (10 archivos).
- Los libros (`~/Downloads/Chatmu Music Books`, 11 carpetas, ~60 libros) cubren bien armonía,
  melodía, jazz, ritmo, escalas del mundo, sampling, mezcla y master. Raga Guide trae 74 ragas en
  audio (4 discos, `.m4a`) más el PDF.

### 1.3 Fallo estructural de las skills de DeepSeek (afecta a las 8)
**Todas dependen de una "card" en `music-kb/…` que el agente no puede leer.** `music-kb` no está en
ningún repo, no se publica con el sync y no está en la máquina del usuario. En producción la skill
dice "lee la card" y el agente se queda con 60 líneas de reglas sueltas. La propia skill es solo un
índice; el conocimiento vive en otro lado.

Decisión: **las skills deben ser autocontenidas.** Lo bueno de las cards se funde dentro de cada
skill (en `SKILL.md` o en un `reference.md` dentro de la misma carpeta, que sí viaja con el sync).
`music-kb` queda como cuaderno de investigación interno, no como dependencia.

---

## 2. Auditoría de las skills de DeepSeek, una por una

| Skill | Veredicto | Por qué |
|---|---|---|
| `chatmu-studio-melody-hooks` | **REESCRIBIR** → `chatmu-studio-hook-melody` (hecha en esta rama) | Principios correctos (outline, tensión, contorno, prosodia) pero sin método ejecutable: no dice cómo inventar el motivo ni el ritmo, no ataca los vicios de IA, y su validación es "pídele al usuario que la cante". No usa `local_harmony_map` ni `local_sing`. Al quedar la nueva, **borrar**. |
| `chatmu-studio-harmony-functional` | **FUSIONAR** con `harmony-voicing` | Reglas sólidas (funciones, cadencias, voice leading), pero duplica a `harmony-voicing` y no aprovecha `local_music_theory action:progression`, que ya hace voice leading. Una sola skill de armonía: "progresión por función + voicing por género". |
| `chatmu-studio-world-scales` | **REESCRIBIR** (dividir) | Dos reglas rompen el caso de uso principal: "nunca aproximes un maqam a 12-TET" y "no pongas acordes occidentales bajo un maqam". Para hip hop, trap o reggaetón con color árabe lo correcto es justo lo contrario: Hijaz/Phrygian dominante en 12-TET sobre un bajo pedal. Además pide afinación microtonal/pitch bends que el bridge no sabe escribir (`local_ableton_write_notes` no manda pitch bend). Se divide en: `chatmu-studio-genre-oriental-hiphop` (fusión, hecha en esta rama) y `chatmu-studio-world-scales` (maqam/raga "de verdad", con drone y ornamentos, usando los audios de Raga Guide como referencia de sayr/pakad). Sin commitear hoy: no la toco. |
| `chatmu-studio-breakbeats` | **QUEDA** con retoque | Orden de construcción por capas y velocidades de ghost notes, correcto. Quitar la referencia a la card, meter las 13 "elementos" dentro de la skill (hoy son números sin significado: "añade el elemento 4"). |
| `chatmu-studio-afro-cuban-rhythms` | **QUEDA** con retoque | Clave, cáscara, tumbao, songo: bien. Meter los grids en 16avos dentro de la skill y conectar con `local_music_theory drum_pattern` donde aplique. |
| `chatmu-studio-club-grooves` | **FUSIONAR** en las skills de género (house, techno, DnB…) | Es una tabla de BPM + grids que se repite con `drums-by-genre` y `genre-templates`. Cada género tendrá su propia skill (ver §3). |
| `chatmu-studio-sampling` | **QUEDA** con retoque | Tipos de sample, fades, warp vs repitch, clearance: correcto. Cambiar "chop con `local_ableton_create_audio_clip`" (no chopea, crea un clip de audio desde un archivo) por el flujo real: `local_stems_separate` / `local_fetch_to_library` + `local_ableton_clip` (warp, pitch, loop markers). |
| `chatmu-studio-spatial-panning` | **QUEDA** con retoque | Planos, opuestos, reverb por send: bien. "Suma a mono" no tiene tool: usar `local_ears_listen` (stereo/correlación) o cargar Utility con `local_ableton_load_device` + `local_ableton_set_device_param`. Enlazar con `local_ears_track_levels` para enmascaramiento. |

Otras skills existentes que el plan toca:

| Skill | Veredicto |
|---|---|
| `compose-core`, `drum-rack`, `record`, `export`, `session-vs-arrangement`, `automation`, `sidechain`, `humanize`, `sound-design`, `synth`, `clone-sound`, `sound-profile-*`, `guide-vocal`, `remake-song`, `separate-stems`, `verify-ai`, `reference`, `listen-troubleshooting`, `vocal-chops`, `session-prep` | QUEDAN (operativas, bien) |
| `melody-over-chords` | QUEDA. Buen método (mapa armónico primero). Al final se alinea con `hook-melody` para no contradecirse (ver orden de trabajo). |
| `harmony-voicing` | Absorbe `harmony-functional` → `chatmu-studio-harmony` |
| `drums-by-genre`, `genre-templates`, `club-grooves` | Se reparten en las skills de género y desaparecen como skills sueltas |
| `song-structure`, `arrangement`, `drop-buildup` | Se fusionan en `chatmu-studio-arrangement` (forma + energía + transiciones por género) |
| `mix-eq`, `mix-compression`, `mixing-progressive` | QUEDAN; se añade `chatmu-mix-by-genre` (balance objetivo por género) |
| `master-chain`, `master-check` | QUEDAN (ya v1.1 con loudness por género) |

---

## 3. Catálogo propuesto

Tres capas. Las de **oficio** saben hacer una cosa (melodía, armonía…). Las de **género** saben
cómo suena un estilo y llaman a las de oficio con los parámetros del estilo. La de **canción
completa** orquesta todo.

### 3.1 Orquestador
| Skill | Qué hace |
|---|---|
| `chatmu-studio-make-song` | De "hazme una canción de X" a una canción entera: brief (género, mood, referencia, BPM, tonalidad, voz sí/no) → elige la skill de género → orden de trabajo (armonía o melodía primero según el género) → arreglo → mezcla → master. Pide aprobación en 3 puntos: idea de 8 compases, arreglo completo, mezcla. Interrumpible en cualquier paso. |
| `chatmu-studio-genre-fusion` | Cómo cruzar dos géneros sin que suene a collage: qué capa toma de cada uno (ritmo de A, armonía/sonido de B), qué tempo manda, conflictos típicos (swing vs recto, 4/4 vs dembow, BPM medio-tiempo). |

### 3.2 Oficio — composición
| Skill | Estado |
|---|---|
| `chatmu-studio-hook-melody` — melodía con gancho (motivo, ritmo firma, punto alto, pregunta/respuesta, anti-vicios de IA) | **Hecha en esta rama** |
| `chatmu-studio-harmonize-melody` — armonizar una melodía existente (tarareada, grabada o MIDI) | **Hecha en esta rama** |
| `chatmu-studio-melody-over-chords` — melodía sobre armonía existente | Existe; alinear |
| `chatmu-studio-harmony` — progresión por función + voicing + rearmonización (fusión de functional + voicing; Felts y Levine para rearmonizar) | Fusionar |
| `chatmu-studio-bass-lines` | Existe; ampliar por género |
| `chatmu-studio-counter-melody` — contramelodías, segundas voces, respuestas de metales/cuerdas | Nueva |
| `chatmu-studio-world-scales` — maqam y raga reales (drone, sayr, pakad, ornamentos); referencias de audio Raga Guide | Reescribir |
| `chatmu-studio-lyrics-prosody` — letra que cae bien en la melodía (acentos, vocales abiertas en notas largas, rima) — Pattison | Nueva |

### 3.3 Oficio — ritmo y arreglo
| Skill | Estado |
|---|---|
| `chatmu-studio-breakbeats`, `chatmu-studio-afro-cuban-rhythms`, `chatmu-studio-humanize`, `chatmu-studio-drum-rack` | Quedan (retoque) |
| `chatmu-studio-arrangement` — forma, curva de energía, entradas/salidas de instrumentos, transiciones, drops (fusión de 3) | Fusionar |
| `chatmu-studio-sampling`, `chatmu-studio-vocal-chops` | Quedan |

### 3.4 Géneros (una skill por familia; cada una con BPM, groove en 16avos, armonía típica, melodía típica, sonidos del factory de Chatmu Synth, forma, mezcla objetivo y "qué lo arruina")
| Skill | Notas |
|---|---|
| `chatmu-studio-genre-pop` | Pop actual: coro en el registro alto, pre-coro que sube, gancho en los primeros 10 s |
| `chatmu-studio-genre-rock` | Riff primero, power chords, batería real humanizada, guitarras dobladas L/R |
| `chatmu-studio-genre-dark-trap` | Menor/frigio, 808 con glide, hi-hats en tresillos y rolls, melodía de campana/flauta, espacio |
| `chatmu-studio-genre-hiphop` | Boom bap / lo-fi / moderno: swing (Dilla), sample o teclado, bajo |
| `chatmu-studio-genre-oriental-hiphop` — hip hop/trap con color árabe/oriental | **Hecha en esta rama** (plantilla de género) |
| `chatmu-studio-genre-reggaeton` | Dembow, i–VI–III–VII y variaciones, perreo vs romántico |
| `chatmu-studio-genre-ambient` | Calma/ambient/lo-fi chill: armonía estática, texturas, evolución lenta, sin golpes |
| `chatmu-studio-genre-rnb` | R&B / neo-soul: 7ª/9ª, voicings drop2, swing suave |
| `chatmu-studio-genre-house-techno` | De `club-grooves`: house, deep, techno, melodic |
| `chatmu-studio-genre-dnb-garage` | DnB, jungle, UK garage, 2-step |
| `chatmu-studio-genre-regional-mx` | Corridos tumbados, banda, norteño (hay presets "Regional Mexican") |
| `chatmu-studio-genre-latin-tropical` | Salsa, cumbia, bachata, merengue (usa afro-cuban-rhythms) |
| `chatmu-studio-genre-afrobeats-amapiano` | Log drum, shakers, swing africano |
| `chatmu-studio-genre-cinematic` | Orquestal/épico/tensión (Rimsky-Korsakov para orquestación) |
| `chatmu-studio-genre-jazz` | Standards, ii-V, voicings, walking bass (Levine) |

### 3.5 Mezcla y master
| Skill | Estado |
|---|---|
| `chatmu-mixing-progressive`, `chatmu-mix-eq`, `chatmu-mix-compression`, `chatmu-studio-spatial-panning`, `chatmu-studio-sidechain` | Quedan |
| `chatmu-mix-by-genre` — balance objetivo por rol y género (cuántos LU va la voz sobre el beat, dónde vive el 808, cuánta reverb), medido con `local_ears_track_levels` | Nueva |
| `chatmu-mix-effects` — reverb, delay, modulación, saturación con intención (Farnell, Mixing with Impact) | Nueva |
| `chatmu-master-chain`, `chatmu-master-check` | Quedan |

Total objetivo: ~45 skills de estudio (hoy 42), pero **sin duplicados** y con 15 de género nuevas.

---

## 4. Formato de cada skill (plantilla)

Basado en la skill de crear skills (frontmatter estricto, cuerpo accionable) y en el linter real
del Desktop (`bridge/skillLint.ts`):

- Frontmatter: `name` = nombre de la carpeta (kebab-case), `description` con disparadores en
  **inglés y español** (search_skills hace match ahí), `category: creative`, `shortDesc` ≤ 120
  caracteres, `tags` como **lista de strings**, `requiresTools` solo con tools registradas.
- **Solo tools que existen** en el bridge (lista de `release/0.1.74`, 102 tools). El linter falla
  si el cuerpo menciona un `local_*` inventado.
- Autocontenida: nada de "lee la card en music-kb". Si hace falta tabla larga → `reference.md`
  en la misma carpeta.
- Estructura: cuándo usar → qué preguntar (lo mínimo) → flujo con tools → reglas duras →
  autocrítica antes de enseñar → qué decirle al usuario.
- Cuerpo en inglés (como el resto del repo); el agente responde en el idioma del usuario.
- Conocimiento destilado de los libros con criterio propio, sin copiar texto.

---

## 5. Orden de trabajo

| # | Entrega | Por qué en este orden |
|---|---|---|
| 1 | **Esta rama** (`feat/production-skills-opus`): plan + `hook-melody` + `harmonize-melody` + `oriental-hiphop` | Melodía es lo que más falla; la de género sirve de plantilla para las demás |
| 2 | Chema revisa/prueba las 3 en Desktop (con Ableton abierto) → ajustes | Validar el formato antes de escribir 40 |
| 3 | `chatmu-studio-harmony` (fusión) + alinear `melody-over-chords` con `hook-melody` | Base de todas las de género |
| 4 | `chatmu-studio-arrangement` (fusión de 3) | La canción completa depende de esto |
| 5 | Géneros pedidos: pop, rock, dark-trap, ambient, reggaetón, hiphop | Los que Chema nombró |
| 6 | `chatmu-studio-make-song` + `chatmu-studio-genre-fusion` | Necesitan géneros y oficio hechos |
| 7 | `chatmu-mix-by-genre`, `chatmu-mix-effects` | Mezcla por género tras tener los géneros |
| 8 | Resto de géneros + `world-scales` reescrita (con escucha de Raga Guide) + `counter-melody` + `lyrics-prosody` | Cobertura |
| 9 | Borrar: `melody-hooks`, `harmony-functional`, `club-grooves`, `genre-templates`, `drums-by-genre`, `song-structure`, `drop-buildup` (tras fusionar) | Al final, cuando su reemplazo ya esté publicado |
| 10 | Retoques: breakbeats, afro-cuban, sampling, spatial-panning (quitar dependencia de music-kb, tools reales) | Rápido, en paralelo |

Cada tanda: rama → PR → Chema prueba en Desktop → merge a `main` → `POST /api/skills/sync`.
**Nunca** sync a producción desde una rama.

### Cómo probar cada skill (criterio de "hecha")
1. Pasa el linter del Desktop: `CHATMU_SKILLS_DIR=<worktree> npx vitest run bridge/skillLint.test.ts`.
2. Prueba en Ableton con 3 pedidos distintos (p. ej. melodía: pop alegre, trap oscuro, balada).
3. Prueba ciega: ¿Chema recuerda la melodía al día siguiente? ¿Suena "a IA"? Si sí, la skill no está.

---

## 6. Riesgos y preguntas abiertas
- **Microtonos:** el bridge no escribe pitch bend. Para maqam real hace falta un sinte con
  afinación microtonal (Chatmu Synth podría cargar `.scl`; ver `scala-scales` en los libros) o una
  tool nueva. Hasta entonces, las skills dicen honestamente que usan 12-TET.
- **Validación melódica:** Ears no transcribe melodía. La autocrítica es simbólica (el agente
  revisa sus propias notas con reglas) + `local_sing` para oírla cantada + el oído del usuario.
- `music-kb` y las cards: decidir si se versionan como repo interno o se archivan.
