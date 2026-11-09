---
name: chatmu-dist-distrokid
description: >
  Distribuye un lanzamiento (single, EP o álbum) en DistroKid usando el navegador
  del propio artista con la extensión Chatmu Browser. Úsala SIEMPRE que el
  usuario pida "subir mi canción a DistroKid", "distribuir en DistroKid", "lanzar
  mi sencillo", "publicar mi EP", "subir el master", o cuando ya tenga cuenta en
  DistroKid y quiera hacer el release sin llenar formularios a mano, aunque no
  mencione la palabra "skill".
compatibility: claude.ai
category: ops
subcategory: distribution
shortDesc: >-
  Sube y publica un release en DistroKid con el navegador del artista.
tags: [distribution, release, upload, distributor, spotify, apple-music, dsp, distribuir, lanzamiento, distrokid, global]
version: "1.0"
---

# DistroKid — Distribución de un lanzamiento

**Tipo:** artist · **Región:** global · **API:** none · **Riesgo ToS:** high

- Web: https://distrokid.com
- Login: https://distrokid.com/signin
- Dashboard: https://distrokid.com/dashboard
- Precio/plan: ~$23/año, sin comisión
- Notas: Prohibe 'high volume, automated, or electronic means… robots, spiders or scripts'. Terminación at-will.
- Perfil de flujo: self_serve_upload
- Auth detectado: password+email+google+apple+sso
- URL final de login: https://distrokid.com/signin/
- Verificación: ⚠️ El bot no pudo cargar el sitio (403/timeout). Ábrelo en el navegador del usuario y confirma el dominio antes de actuar.

## Regla de oro

Trabajas **en la sesión del propio artista**, con su permiso, **un release a la vez**.
Nunca tipos contraseñas ni datos de tarjeta. Nunca haces acciones masivas.
Cada clic que envíe, guarde, publique o pague **espera el Allow del usuario** en
la página (salvo que haya activado "Let the agent decide"). Si el usuario no está
presente para dar Allow, detente y pídeselo.

## Pre-flight (antes de abrir el navegador)

1. `browser_status`. Si no está conectado: dile "Conecta Chatmu Browser en Chrome
   (icono → Connect this browser)" y espera. No sigas sin navegador.
2. Reúne del usuario o del catálogo de Chatmu:
   - Artista principal (nombre exacto como debe aparecer).
   - Tipo: Single / EP / Album.
   - Título del release y de cada track.
   - Género principal y secundario, idioma.
   - Fecha de lanzamiento (mínimo 14 días; si es menos, avisa).
   - Sello o "Independiente", línea © y línea ℗ (año + titular).
   - ISRC (opcional; si no hay, se asigna), UPC (si aplica).
   - Créditos: compositores, letristas, productores, intérpretes y rol.
   - Explicit / clean, letra (opcional).
   - Audio master **WAV** 44.1/48 kHz, 16/24-bit, estéreo.
   - Portada JPG/PNG cuadrada ≥3000×3000, RGB, sin logos de plataformas.
3. Verifica que tengas **URLs públicas HTTPS** de audio y portada para
   `browser_upload`.

> **Límite real:** `browser_upload` acepta archivos de **máximo 10 MB**. Un WAV
> master casi siempre pesa más. Si el audio pesa más de 10 MB, **no intentes
> subirlo con la tool**: pide al usuario que arrastre el WAV al campo de la página
> y tú sigues con el resto. La portada normalmente sí cabe.

### Perfil: autoservicio

El artista sube su propio release. Sigue el flujo tal cual; si el dashboard cambia, prioriza las etiquetas visibles.

**Login:** OAuth (Google/Apple/Facebook). El usuario elige el proveedor y entra; el agente espera.

## Flujo

### 1. Permisos y apertura
1. `browser_allow_sites` con `["https://distrokid.com", "https://distrokid.com/signin", "https://distrokid.com/dashboard"]`
   (máx. 20). Pide al usuario que apruebe en Chrome.
2. `browser_open` en `https://distrokid.com/dashboard`.

### 2. Detectar sesión (sin tocar contraseñas)
1. `browser_read`.
2. Si ves "Sign in", "Log in", "Iniciar sesión", un campo `password` o la URL de
   login: **DETENTE**. Dile: "Inicia sesión tú en DistroKid; cuando estés dentro,
   dime 'listo' y sigo." No escribas credenciales.
3. Cuando confirme, `browser_read` otra vez. Si ya está el dashboard, continúa.

### 3. Crear el release
1. Busca el botón de crear: el botón de 'New release', 'Upload', 'Create release' o equivalente.
2. `browser_read` (interactiveOnly) para ubicar el ref y `browser_click`.
3. Si pide tipo de release, elige el que corresponda (artist).
4. Selecciona el artista. Si no existe, créalo con los datos exactos.

### 4. Metadata
Llena en el orden en que la página los pida. Usa `browser_read` antes de cada
`browser_type`/`browser_select` porque **los refs cambian en cada lectura**.
- Título, versión, artista, feat.
- Género, subgénero, idioma, explicit.
- Fecha de lanzamiento, sello, ©, ℗.
- ISRC/UPC si el formulario los pide (no inventes).
- Créditos y splits (si la plataforma los pide).

Botón 'Upload' en el dashboard. Pide artista, tipo (Single/Album), título, género, fecha, tiendas, audio y portada.

### 5. Archivos
1. Portada: `browser_upload` con la URL pública (≤10 MB).
2. Audio: si pesa ≤10 MB, `browser_upload`; si no, pide al usuario que lo
   arrastre manualmente y espera a que confirme.
3. Espera a que termine el procesamiento (`browser_wait` con el texto de
   "uploaded"/"processing"/"complete").
4. Si hay waveform/preview, verifica que el track correcto quedó asociado.

### 6. Tiendas y opciones
- Selecciona todas las tiendas que el usuario quiera (por defecto todas).
- Configura Content ID / YouTube si la plataforma lo ofrece y el usuario acepta.
- Revisa territorios y fecha.

### 7. Revisión humana (obligatoria)
1. `browser_read` de la pantalla de resumen.
2. Resume al usuario en 5 líneas: título, artista, tracks, fecha, tiendas.
3. Pregunta: "¿Lo envío así?" y espera un sí explícito.

### 8. Submit
1. `browser_click` en **Upload / Distribute**.
2. Avisa antes: "Voy a enviar el release; te va a pedir Allow en la página."
3. Espera el Allow. Si el usuario lo niega, no reintentes: pregunta qué corregir.
4. `browser_wait` hasta ver confirmación / "submitted" / "in review".

### 9. Cierre
- Captura el **ID de release** o mensaje de confirmación.
- Reporta: estado, fecha de publicación estimada, y qué sigue (revisión de la
  distribuidora, posible corrección de metadata).
- Si hubo errores de metadata, explica en palabras simples y ofrece corregirlos.

## Requisitos de archivo
WAV/FLAC, portada JPG/PNG cuadrada ≥1400px

## Flujo capturado (real) — 2026-11-09

Entrada: https://distrokid.com/dashboard

1. **open** (Si hay login, el usuario entra.)
2. **click** — «Upload» (Menú superior.)
3. **select** — «Release type» → `release.type`
4. **type** — «Artist» → `artist.stage_name`
5. **type** — «Release title» → `release.title`
6. **select** — «Genre» → `release.genre`
7. **type** — «Release date» → `release.date`
8. **upload** — «Artwork» → `files.cover`
9. **upload** — «Audio» → `files.audio` (Si >10 MB, lo arrastra el usuario.)
10. **confirm** — «Submit» (Allow humano obligatorio.)

Avisos:
- El ToS de DistroKid prohíbe acceso automatizado de alto volumen; usar solo en la sesión del artista y con Allow.

## Troubleshooting
- **La página cambió:** vuelve a `browser_read`; no uses refs viejos.
- **No aparece el botón:** `browser_scroll` y `browser_read` de nuevo; a veces
  está en un menú lateral.
- **Error de metadata:** lee el mensaje exacto y corrige solo ese campo.
- **Sesión expirada:** vuelve al paso 2.
- **Audio >10 MB:** el usuario lo sube a mano; tú continúas.
- **Pago/checkout:** si hay que pagar, **detente** y deja que el usuario pague.
  Nunca ingreses tarjetas.

## Éxito
El release queda en estado "submitted"/"in review" y el usuario ve su ID o
confirmación. Si la plataforma manda email de confirmación, recuérdale revisarlo.
