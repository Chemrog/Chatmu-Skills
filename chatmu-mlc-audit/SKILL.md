---
name: chatmu-mlc-audit
description: >
  Cruza el catálogo de Chatmu (canciones, ISRC, ISWC, autores, splits) contra
  The MLC para encontrar obras no registradas, shares sin reclamar, ISRC sin
  match y overclaims, y luego registra o reclama desde el portal de The MLC con
  el navegador del artista. Úsala SIEMPRE que el usuario pregunte "¿estoy
  cobrando todo en MLC?", "revisa mi catálogo en The MLC", "tengo canciones sin
  reclamar", "me faltan mechanical royalties", "cruza mis canciones con MLC", o
  cuando un artista de EE.UU. publique música y quiera cobrar mechanical, aunque
  no diga "skill".
compatibility: claude.ai
category: ops
subcategory: royalties
shortDesc: >-
  Audita Chatmu vs The MLC y registra/reclama obras con el navegador.
tags: [mlc, mechanical, royalties, audit, usa, the-mlc, cobrar-regalias, mechanical-royalties, regalias]
version: "1.0"
---

# The MLC — auditoría y reclamo de mechanical (EE.UU.)

The MLC recauda **mechanical digital de EE.UU.** para compositores y publishers
auto-administrados. Si una obra no está registrada o su share no está reclamado,
el dinero se queda sin dueño. Esta skill encuentra ese dinero.

- Portal: https://portal.themlc.com/login
- Búsqueda pública: https://www.themlc.com (Public Work Search)
- Herramientas: Claiming, Works Registration (Individual/Bulk/CWR), Matching,
  Overclaims, Catalog Export, Catalog Transfer.

## Regla de oro
Un artista a la vez, sin contraseñas, sin acciones masivas sin confirmación.
El registro/claim se envía con `browser_upload` (Excel/CWR) o con clics
individuales. Todo envío espera **Allow**.

## Fase A — Diagnóstico (sin navegador)

### A1. Trae el catálogo de Chatmu
Con el MCP de Chatmu, obtén por artista:
- Título de cada obra, ISRC, ISWC (si existe).
- Autores/compositores y sus shares.
- Publisher/editorial (o auto-editado).
- Fecha de publicación, sello, país.
- Estado de distribución.

### A2. Trae el estado en MLC
Usa las tools del MLC MCP por prefijo (los nombres exactos pueden variar):
- `mlc_search_*` / `mlc_find_*` / `mlc_lookup_*`: buscar obras y grabaciones.
- `mlc_cross_reference_*`: cruzar catálogo.
- `mlc_get_*` / `mlc_list_*`: detalle y listas.
- `mlc_build_*` / `mlc_validate_*` / `mlc_export_*`: armar/validar/exportar el
  Excel o CWR para bulk registration.
- `mlc_registration_wizard`: wizard interactivo (si está disponible).

Si el MCP no responde, usa el navegador con Public Work Search (Fase B) para
verificar manualmente.

### A3. Clasifica cada obra
```
Título | ISRC | ISWC | Autores | Shares | Estado MLC | Problema
```
Problemas:
- **NO_REGISTRADA** — no existe en MLC.
- **SIN_RECLAMAR** — existe pero el share está sin reclamar.
- **SHARE_MAL** — shares no suman 100% o están asignados mal.
- **ISRC_SIN_MATCH** — la grabación no está vinculada a la obra.
- **OVERCLAIM** — shares >100%.
- **OK** — nada que hacer.

### A4. Presenta el diagnóstico
Muestra la tabla y el resumen:
"Tienes N obras: X OK, Y sin registrar, Z sin reclamar, W con shares mal.
Esto puede valer ≈ $____/mes (si hay datos de regalías)."

Pregunta: "¿Quieres que registre/reclame las que faltan?" No actúes sin sí.

## Fase B — Verificación en el navegador (opcional)

1. `browser_status` → si no está conectado, pide conectar.
2. `browser_allow_sites` con `["https://www.themlc.com","https://portal.themlc.com"]`.
3. `browser_open` en `https://www.themlc.com`.
4. `browser_read`; usa Public Work Search por título/ISRC para confirmar los
   casos dudosos.
5. Anota lo que confirmes.

## Fase C — Registro / reclamo

1. `browser_open` en `https://portal.themlc.com/login`.
2. `browser_read`. Si pide login: **detente** y pide al usuario iniciar sesión.
   Cuando confirme, vuelve a leer.
3. Entra a **Member Hub**. (Si es songwriter sin Member Hub, usa **Songwriter
   Hub**, que tiene Matching y Catalog Export, pero no registro.)
4. Elige la herramienta según el problema:
   - **NO_REGISTRADA** → **Works Registration** → **Bulk** (Excel/CWR) o
     **Individual Work Registration**.
   - **SIN_RECLAMAR** → **Claiming Tool**.
   - **ISRC_SIN_MATCH** → **Matching Tool**.
   - **OVERCLAIM** → **Overclaims Tool**.
   - **SHARE_MAL** → corrige en el registro/claim o usa Overclaims.
5. Para bulk:
   - Genera el archivo con `mlc_build_*` / `mlc_export_*` (Excel ≤10 MB).
   - `browser_upload` en el input de archivo.
   - `browser_wait` hasta que valide.
   - Si hay errores, corrígelos y re-sube.
6. Para individual: llena título, autores, shares, publisher, ISWC/ISRC, fechas.
7. Antes de enviar, resume y pide confirmación.
8. `browser_click` en Submit/Claim. Avisa del Allow.
9. `browser_wait` hasta confirmación. Captura IDs/folios.

## Fase D — Cierre

Reporta:
- Obras registradas / reclamadas / corregidas (con IDs).
- Obras que quedaron pendientes y por qué.
- Acción recomendada (ej. "pide a tu co-autor que reclame su share").
- Copia del Excel/CWR generado, si aplica.
- Recordatorio: MLC paga mechanical de EE.UU.; para performance falta la PRO y
  para master falta SoundExchange.

## Errores comunes
- **No eres Member:** solo Members registran; los Users pueden buscar. Explica el
  alta.
- **El Excel no valida:** revisa que los shares sumen 100% y que el ISWC/ISRC
  tenga formato correcto.
- **Obra ya existe con otro titular:** no dupliques; usa Claim o contacta soporte.
- **Sesión expirada:** vuelve a login.
- **Pago/tax:** los datos bancarios/fiscales los captura el usuario.

## Éxito
Cada obra del catálogo tiene estado claro en MLC y las que faltaban quedaron
registradas o reclamadas, con evidencia (ID/folio).
