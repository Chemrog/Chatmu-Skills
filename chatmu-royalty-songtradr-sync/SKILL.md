---
name: chatmu-royalty-songtradr-sync
description: >
  Registra, reclama y reconcilia regalías en Songtradr (Sync licensing) usando el
  navegador del artista. Úsala SIEMPRE que el usuario pida "cobrar regalías",
  "reclamar mis canciones en Songtradr", "revisar si me deben", "registrar mi
  catálogo en Songtradr", "SoundExchange", "MLC", "neighboring rights", o cuando
  haya que cruzar el catálogo de Chatmu con lo que la entidad tiene registrado,
  aunque no diga "skill".
compatibility: claude.ai
category: ops
subcategory: royalties
shortDesc: >-
  Registra y reclama regalías en Songtradr (Sync licensing).
tags: [royalties, recaudacion, cobrar-regalias, sync, songtradr-sync, global]
version: "1.0"
---

# Songtradr — Sync licensing

- Web: https://songtradr.com
- Portal: https://songtradr.com
- Cubre: Marketplace de sync licensing.
- Herramientas: Upload, Metadata, Licencias

## Regla de oro

Sesión del propio artista, sin contraseñas, sin pagos. Cada envío espera el
**Allow**. No hagas reclamos masivos sin confirmación: primero muestra el
diagnóstico y luego actúa.

## Flujo general

### 1. Diagnóstico con Chatmu (antes del navegador)
1. Con el MCP de Chatmu, obtén el catálogo del artista: títulos, ISRC, ISWC,
   splits, fechas, sello.
2. Pregunta al usuario qué quiere: **registrar**, **reclamar**, **revisar
   regalías** o **corregir shares**.
3. Arma una tabla de trabajo:
```
Obra/Track | ISRC | ISWC | Autores | Shares | Estado en Songtradr
```

### 2. Navegador
1. `browser_status`; si no está conectado, pídele conectarlo.
2. `browser_allow_sites` con `["https://songtradr.com", "https://songtradr.com"]`.
3. `browser_open` en `https://songtradr.com`.
4. `browser_read`. Si hay login: **detente**, pide al usuario iniciar sesión.
5. Al confirmar, `browser_read` y ubica el área de trabajo.

### 3. Buscar y comparar
1. Usa el buscador de la entidad (por ISRC, título o artista).
2. Para cada obra/track, anota: registrado sí/no, shares, titular, estado.
3. Marca: **sin reclamar**, **shares mal**, **sin match de ISRC**, **no
   registrado**.
4. Muestra el resumen al usuario antes de tocar nada.

### 4. Acción
1. Crea el perfil de artista si no existe.
2. Sube tracks con metadata, stems y versiones (instrumental, clean).
3. Marca clears/restricciones (samples, features, exclusividades).
4. Aplica a briefs o espera curaduría.

### 5. Confirmar y cerrar
1. Antes de cada envío, di qué vas a hacer y espera Allow.
2. `browser_wait` hasta confirmación.
3. Captura folios/IDs y estado.
4. Reporta: qué se registró, qué se reclamó, qué falta, y el impacto estimado.



## Troubleshooting
- **Sin cuenta:** explica el alta (y si requiere ser socio/artista registrado).
- **Obra no aparece:** puede no estar registrada; usa el flujo de registro.
- **Shares en conflicto:** muestra el conflicto y pide decisión al usuario.
- **Pago/tax:** si pide datos fiscales (W-9/W-8BEN), pide al usuario que los
  capture él; no inventes datos fiscales.

## Éxito
Catálogo reconciliado: cada obra/track con estado claro (registrado, reclamado,
pendiente) y sin shares inválidos.
