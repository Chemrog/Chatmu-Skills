---
name: chatmu-flow-capture
description: >
  Captura un flujo real que el artista acaba de completar en su navegador
  (distribuidora, PRO, registro de obra o regalías) y lo guarda como JSON para
  que la skill de esa entidad se vuelva más precisa. Úsala SIEMPRE que el usuario
  diga "guarda este flujo", "captura cómo se hace", "así se hace en mi
  distribuidora", "aprende este proceso", o después de completar con éxito un
  release/registro/reclamo, aunque no diga "skill".
compatibility: claude.ai
category: ops
subcategory: browser
shortDesc: >-
  Captura y guarda un flujo real para afinar la skill de la entidad.
tags: [browser, flow, capture, automation, skill-improvement, captura, flujo, navegador]
version: "1.0"
---

# Capturador de flujos

Objetivo: convertir un trámite que **ya funcionó** en un JSON reutilizable, sin
guardar credenciales ni refs efímeros. El flujo capturado se inyecta en la skill
de la entidad y la hace más exacta en la próxima corrida.

## Cuándo capturar

- Justo después de un release/registro/reclamo exitoso.
- Cuando el usuario diga "así se hace" o corrija un paso.
- Cuando el dashboard cambió y la skill falló.

## Qué registrar (por paso)

Después de cada `browser_read`, anota:

| Campo | Ejemplo |
|---|---|
| `action` | `open`, `click`, `type`, `select`, `upload`, `confirm`, `wait`, `scroll`, `read` |
| `label` | el texto visible del botón/campo: "Upload", "Release title", "Genre" |
| `value_from` | de dónde sale el dato: `release.title`, `artist.stage_name`, `files.cover` |
| `note` | contexto: "menú superior", "pestaña Tracks", "si >10 MB lo sube el usuario" |

**No guardes:** `ref` (cambia en cada lectura), contraseñas, OTP, tarjetas,
tokens, ni datos personales sensibles.

## Procedimiento

1. Identifica la entidad y su `kind` (`distributor`, `pro`, `registry`, `royalty`).
2. Mientras operas, mantén una lista mental/visible de pasos.
3. Al terminar, arma el JSON:

```json
{
  "entity": "distrokid",
  "kind": "distributor",
  "captured_at": "2026-11-09",
  "entry_url": "https://distrokid.com/dashboard",
  "auth": "password+email+google+apple+sso",
  "steps": [
    {"n": 1, "action": "open", "url": "https://distrokid.com/dashboard"},
    {"n": 2, "action": "click", "label": "Upload", "note": "menú superior"},
    {"n": 3, "action": "type", "label": "Release title", "value_from": "release.title"},
    {"n": 4, "action": "upload", "label": "Artwork", "value_from": "files.cover"},
    {"n": 5, "action": "confirm", "label": "Submit", "note": "Allow humano"}
  ],
  "warnings": []
}
```

4. Valida y guarda:

```bash
python3 tools/save_flow.py flows/<entity>.json
python3 tools/generate.py
```

Si no tienes shell, entrega el JSON en el chat y dile al usuario/equipo que lo
guarde en `flows/<entity>.json` y corra `generate.py`.

5. Re-empaqueta esa skill:

```bash
python3 tools/package_all.py <skill-name>
```

## Reglas

- Un flujo por entidad; si ya existe, usa `--replace`.
- Si un paso es condicional, anótalo en `note` ("solo si hay feat", "solo si pide
  splits").
- Si el paso requiere Allow, usa `action: "confirm"`.
- Si el paso sube un archivo >10 MB, anota que lo hace el usuario.
- Si el flujo es de API, no lo captures como UI: anota `"api": true` y el endpoint.

## Resultado

`flows/<entity>.json` válido + skill regenerada con la sección
**"Flujo capturado (real)"**.
