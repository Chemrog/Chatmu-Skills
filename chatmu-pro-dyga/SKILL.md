---
name: chatmu-pro-dyga
description: >
  Registra obras musicales (composición y letra) en DYGA Chile, la sociedad de
  derechos de autor de Chile, usando el navegador del propio artista.
  Úsala SIEMPRE que el usuario pida "registrar mi canción en DYGA Chile",
  "dar de alta mi obra", "cobrar regalías de autor en Chile",
  "registrar mi composición", o cuando un artista de Chile necesite
  que sus obras queden declaradas para performance, aunque no diga "skill".
compatibility: claude.ai
category: ops
subcategory: publishing
shortDesc: >-
  Da de alta obras y splits en DYGA Chile (Chile) con el navegador.
tags: [pro, performance, royalties, register-work, copyright, regalias, registro-de-obra, derechos-de-autor, dyga, cl]
version: "1.0"
---

# DYGA Chile — Registro de obras (Chile)

**País:** Chile · **Región:** LATAM

- Web: No especificado
- Portal: No especificado
- Ruta típica: buscar 'Register work' / 'Alta de obra'
- Auth detectado: unknown
- URL final de login: —

## Qué es y qué no

DYGA Chile recauda **derechos de performance/composición** (no distribuye audio y
normalmente no registra el master). El registro aquí es para que las regalías de
autor lleguen a las personas correctas. Si el artista además quiere registrar la
obra como evidencia legal, eso es el registro nacional (ver skill de registro de
obras del país).

## Regla de oro

Sesión del propio artista, una obra a la vez, sin contraseñas, sin pagos.
Cada envío espera el **Allow** del usuario en la página.

## Pre-flight

1. `browser_status`. Si no está conectado, pídele conectarlo.
2. Confirma que el artista **ya es miembro/socio** de DYGA Chile. Si no lo es, este
   flujo no aplica: primero hay que afiliarse (trámite aparte, normalmente con
   identificación y contrato). Avísale.
3. Reúne:
   - Título de la obra y títulos alternos.
   - Autores: **nombre legal completo**, rol (compositor / letrista / ambos),
     IPI/CAE si lo tiene, y **porcentaje de share**.
   - Editorial/publisher de cada autor (o "auto-editado").
   - Duración, género, idioma, año de creación.
   - ISWC si ya existe; ISRC de la grabación si aplica.
   - Letra (opcional según sociedad).
   - Datos de la grabación: artista, sello, fecha de publicación.
4. Verifica que **los shares sumen 100%**. Si no, detente y corrígelo con el
   usuario antes de enviar.

## Flujo

### 1. Permisos y apertura
1. `browser_allow_sites` con `["No especificado", "No especificado"]`.
2. `browser_open` en `No especificado` (o en `No especificado` si no hay portal directo).

### 2. Sesión
1. `browser_read`.
2. Si hay login/password: **detente** y pide al usuario iniciar sesión. No
   escribas credenciales.
3. Cuando diga "listo", `browser_read` y confirma que entró al área de socios.

### 3. Llegar al alta de obra
1. Busca: "Register work", "Alta de obra", "Registro de obras", "Declarar obra",
   "Obra nueva", "Werke anmelden", "Déclarer une œuvre", "作品届", "Cadastro de obras".
2. `browser_read` (interactiveOnly) → `browser_click` en el elemento correcto.
3. Si hay varios formularios (obra musical, audiovisual, etc.), elige **obra
   musical**.

### 4. Llenar la obra
Usa `browser_read` antes de cada campo; los refs cambian.
1. Título y títulos alternos.
2. Autores uno por uno: nombre legal, rol, IPI/CAE, share.
3. Publisher/editorial por autor.
4. Duración, género, idioma, año.
5. ISWC/ISRC si se piden.
6. Letra si se pide.
7. Grabación: artista, sello, fecha.

Si el portal tiene buscador de obras, busca antes de crear para no duplicar.

### 5. Validación de shares
Antes de enviar, muestra al usuario:
```
Autor            Rol            Share
...              ...            ...
Total                           100%
```
Si el total no es 100%, no envíes.

### 6. Envío
1. `browser_click` en "Submit"/"Enviar"/"Guardar".
2. Avisa que pedirá Allow. Espera.
3. `browser_wait` hasta confirmación o número de registro.

### 7. Cierre
- Captura **número de registro/folio** y fecha.
- Explica al artista qué sigue: la sociedad valida, asigna ISWC y empieza a
  recaudar.
- Si el flujo genera un **PDF o comprobante**, indícale descargarlo y guárdalo
  como evidencia.

## Si la sociedad exige formato en papel/PDF
Algunas sociedades piden un formulario firmado. En ese caso:
1. Genera una **hoja de datos prellenada** con todos los campos del paso 4.
2. Dile al usuario qué formulario descargar (te lo indica la página) y pásale la
   hoja para que la firme.
3. Si la sociedad acepta carga digital, sube el PDF firmado si la página lo
   permite; si no, indícale el canal (email/ventanilla).



## Troubleshooting
- **No eres socio:** detente; explica el alta de membresía.
- **ISWC desconocido:** déjalo vacío; la sociedad lo asigna.
- **Shares no suman 100:** corrige antes de enviar.
- **Sesión expirada:** vuelve al paso 2.
- **Error de validación:** lee el campo exacto y corrige solo eso.

## Éxito
Obra registrada con número de folio/registro y shares correctos.

> **URL por verificar:** el dominio no quedó confirmado en la fuente. Antes de abrir, confirma con el usuario que la URL es la correcta; si no, busca el sitio oficial y usa ese dominio.
