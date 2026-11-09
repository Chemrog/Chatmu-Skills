---
name: chatmu-music-browser
description: >
  Router maestro para TODO lo que se hace en el navegador del artista con Chatmu
  Browser: distribuir música, registrar obras, afiliarse a PROs, cobrar regalías
  (MLC, SoundExchange, neighboring), registrar copyright, ISRC/ISWC, Content ID y
  sync. Úsala SIEMPRE que el usuario diga "entra a mi distribuidora", "sube mi
  canción", "registra mi obra", "cobra mis regalías", "revisa mi MLC", "entra a
  mi PRO", "llena el formato", o pida ayuda con cualquier plataforma musical,
  aunque no nombre una skill específica. Esta skill decide a cuál de las 265
  skills de entidad ir y cómo usar el navegador sin romper la sesión.
compatibility: claude.ai
category: ops
subcategory: browser
shortDesc: >-
  Router maestro: elige la skill de distribuidora, PRO, registro o regalías y
  opera el navegador del artista.
tags: [router, browser, distribution, pro, registry, royalties, browser-automation, distribucion, regalias, registro-de-obra, navegador]
version: "1.0"
---

# Chatmu Music Browser — router maestro

Esta skill no ejecuta el trámite: **elige la skill correcta** y aplica las reglas
comunes del navegador. Hay 265 skills de entidad en `skills/`:
`chatmu-dist-*`, `chatmu-pro-*`, `chatmu-reg-*`, `chatmu-royalty-*`.

## 1. Clasifica la intención

| El usuario quiere… | Skill prefijo | Ejemplos |
|---|---|---|
| Publicar música en DSPs | `chatmu-dist-*` | DistroKid, TuneCore, CD Baby, Symphonic, ONErpm |
| Cobrar derechos de autor (performance) | `chatmu-pro-*` | SACM, ASCAP, BMI, SGAE, PRS, APRA |
| Proteger/registrar la obra como evidencia | `chatmu-reg-*` | INDAUTOR, US Copyright Office, DNDA |
| Cobrar mechanical / neighboring / publishing | `chatmu-royalty-*` | The MLC, SoundExchange, PPL, GVL |
| Auditar catálogo contra el MLC | `chatmu-mlc-audit` | — |

Si hay duda, pregunta en una sola frase: "¿Quieres publicar en una distribuidora,
registrar la composición en tu PRO, registrar la obra como evidencia, o cobrar
regalías que ya te deben?"

## 2. Encuentra la entidad

1. Busca por nombre en `INDEX.md` o en `skills.json`.
2. Si el usuario no dice cuál:
   - **Distribuidora:** pregunta en cuál tiene cuenta. Si no tiene, recomienda
     según país y presupuesto (no inventes precios; lee la ficha de la skill).
   - **PRO:** usa el país del artista (`data/pros.json`).
   - **Registro:** usa el país del artista (`data/registries.json`); si no hay,
     usa la skill `chatmu-reg-wipo` para ubicar la oficina.
3. Carga **solo** la skill de la entidad elegida; no mezcles varias.

## 3. Reglas comunes del navegador (obligatorias)

### Herramientas
`browser_status` · `browser_allow_sites` · `browser_open` · `browser_read` ·
`browser_click` · `browser_type` · `browser_scroll` · `browser_select` ·
`browser_upload` · `browser_wait`

### Ciclo obligatorio
1. `browser_status` → si no está conectado, pide conectar.
2. `browser_allow_sites` con todas las URLs del flujo (máx. 20).
3. `browser_open` en la URL de entrada.
4. `browser_read` (o `interactiveOnly: true`) **antes de cada acción**.
5. Ejecuta una acción.
6. Vuelve a `browser_read`: **los refs cambian en cada lectura**.
7. Usa `browser_wait` cuando algo cargue lento.

### Prohibiciones
- **Nunca** escribas contraseñas, OTP, tarjetas ni datos fiscales.
- Si hay login: **detente** y pide al usuario iniciar sesión. Cuando diga "listo",
  vuelve a leer.
- **Nunca** hagas pagos. Si hay checkout, detente y pasa la referencia.
- **Nunca** acciones masivas sin mostrar antes el diagnóstico y pedir confirmación.

### Allow
Cualquier clic que envíe, guarde, publique o borre pausa y espera el **Allow** en
la página. Antes de ese clic, di exactamente qué se va a enviar.

### Límite de archivos
`browser_upload` acepta **≤10 MB** y solo `<input type=file>`.
- Portadas: normalmente caben.
- WAV masters: casi siempre pesan más → pide al usuario que arrastre el archivo a
  la página y tú sigues con metadata.
- Si el campo es drag-and-drop sin input visible, también lo sube el usuario.

## 4. Datos que siempre necesitas

Antes de abrir el navegador, reúne (según el caso):
- Nombre legal del artista y nombre artístico.
- País y correo.
- Título(s), ISRC, ISWC, UPC.
- Autores, compositores, productores, splits (deben sumar 100%).
- Fecha de lanzamiento (≥14 días para distribución).
- Sello, © y ℗.
- Audio WAV y portada 3000×3000.
- Credenciales **no**: el usuario inicia sesión.

## 5. Entrega de PDFs y formularios

Cuando el trámite genere un PDF, un acuse o un formato firmable:
1. Genera una **hoja de datos prellenada** (título, autores, shares, folio, fecha).
2. Dile al usuario qué PDF descargar y dónde.
3. Si hay que firmar (e.firma, firma autógrafa), que lo haga el usuario.
4. Guarda folio y estado en el reporte final.

## 6. Cierre

Reporta siempre:
- Entidad y URL usada.
- Acción realizada y estado.
- Folio/ID/release ID.
- Qué falta y qué sigue.
- Si hubo un Allow negado o un error, qué se corrigió.
