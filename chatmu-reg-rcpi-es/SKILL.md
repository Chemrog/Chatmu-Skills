---
name: chatmu-reg-rcpi-es
description: >
  Registra una obra musical como evidencia legal ante Registro Central de la Propiedad Intelectual en
  España, usando el navegador del artista, y le entrega los datos y
  comprobantes que necesita. Úsala SIEMPRE que el usuario pida "registrar mi
  canción en España", "sacar el registro de autor", "proteger mi obra",
  "llenar el formato de Registro Central de la Propiedad Intelectual", "INDAUTOR", "copyright office", o cuando
  necesite evidencia legal de autoría, aunque no diga "skill".
compatibility: claude.ai
category: ops
subcategory: registries
shortDesc: >-
  Registra obras ante Registro Central de la Propiedad Intelectual (España) y entrega comprobantes.
tags: [copyright, registration, evidence, registro-de-obra, proteger-obra, copyright-office, rcpi-es, es]
version: "1.0"
---

# Registro Central de la Propiedad Intelectual — Registro de obra (España)

**País:** España

- Web: https://www.cultura.gob.es
- Portal: https://www.cultura.gob.es
- Formularios: Solicitud de inscripción
- Costo: consultar
- En línea: sí
- Descarga / formulario: https://www.cultura.gob.es/cultura/areas/propiedadintelectual/mc/rpi/registro-obras/impresos-solicitud.html

**Formatos y links:**
- [Impresos de solicitud (PDF)](https://www.cultura.gob.es/cultura/areas/propiedadintelectual/mc/rpi/registro-obras/impresos-solicitud.html) (pdf)
- [Solicitud telemática](https://www.cultura.gob.es/cultura/areas/propiedadintelectual/mc/rpi/solicitud-telematica.htm) (online)
- [Sede electrónica RPI](https://sede.mcu.gob.es/rpi4/webpages/publico/presentacion.seam) (online)
- Auth detectado: form
- URL final de login: https://www.cultura.gob.es/portada.html

## Antes de empezar: qué significa registrar

En la mayoría de países el derecho de autor **nace con la obra** (Convenio de
Berne); el registro **no es obligatorio**. Sirve como **prueba** de autoría y
fecha. En EE.UU. sí conviene registrar antes de demandar (daños estatutarios).
Díselo al artista en una frase, sin dar cátedra.

## Regla de oro

Sesión del propio artista, una obra a la vez, sin contraseñas. Si hay que pagar
una tasa, **detente** y deja que el usuario pague. Nunca metas datos de tarjeta.

## Pre-flight

1. `browser_status`; si no hay navegador, pídele conectarlo.
2. Reúne:
   - Título de la obra.
   - Autor(es): nombre legal, nacionalidad, domicilio, correo.
   - Datos del solicitante (titular de derechos) y su identificación.
   - Tipo de obra: musical con letra / sin letra / grabación.
   - Año de creación y de publicación.
   - Letra y/o partitura si se piden.
   - Audio (si el trámite lo pide).
   - Comprobante de pago (si aplica).
3. Si el portal pide **e.firma / firma electrónica**, confirma que el usuario la
   tiene y que puede usarla.

## Flujo

### 1. Permisos y apertura
1. `browser_allow_sites` con `["https://www.cultura.gob.es", "https://www.cultura.gob.es"]`.
2. `browser_open` en `https://www.cultura.gob.es`.

### 2. Identificar el trámite correcto
1. `browser_read`.
2. Busca el trámite de **registro de obra musical** (no marca, no ISBN, no
   editorial). Si hay varios, pregunta al usuario cuál corresponde.
3. Si el portal tiene buscador de trámites, usa el nombre exacto de los
   formularios: Solicitud de inscripción.

### 3. Sesión / identificación
1. Si hay login: **detente**, pide al usuario iniciar sesión (y e.firma si aplica).
2. `browser_read` al confirmar.

### 4. Llenar el formulario
Usa `browser_read` antes de cada campo.
1. Datos del solicitante/titular.
2. Datos del autor(es).
3. Datos de la obra: título, tipo, género, año, idioma.
4. Adjuntar: letra, partitura, audio, portada (según se pida).
5. Datos de publicación (si aplica).

Registros autonómicos también.

### 5. Pago (si aplica)
- Si hay que generar una referencia de pago: genera la referencia y **pásasela
  al usuario** con instrucciones claras.
- **No pagues tú**. Espera a que el usuario pague y te confirme.
- Si el portal acepta comprobante, súbelo cuando el usuario lo tenga.

### 6. Envío y folio
1. `browser_click` en enviar/registrar.
2. Avisa que pedirá Allow.
3. `browser_wait` hasta ver folio, acuse o "recibido".
4. Captura: **folio, fecha, estado, PDF/acuse**.

### 7. Entrega al artista (importante)
Entrega en el chat:
1. **Hoja de datos prellenada** con todo lo que se capturó (para que pueda
   revisar, corregir o reusar en otro trámite).
2. **Folio/acuse** y estado.
3. **Qué sigue**: plazo de resolución, cómo descargar el certificado, y si debe
   firmar o recoger algo.
4. Si el portal generó un PDF, dile exactamente dónde descargarlo y que lo
   guarde.

## Plantilla de hoja de datos

```
REGISTRO DE OBRA — Registro Central de la Propiedad Intelectual (España)
Título:
Tipo de obra:
Autor(es) / nombre legal / nacionalidad:
Titular / solicitante:
Año de creación:
Año de publicación:
Letra: (sí/no, adjunta)
Audio: (sí/no, adjunta)
Formulario usado: Solicitud de inscripción
Folio:
Fecha:
Estado:
```



## Troubleshooting
- **El portal no carga / bloquea:** prueba `browser_wait`, recarga con
  `browser_open` en la misma URL, y si sigue, usa el canal alternativo.
- **Pide e.firma y no hay:** explícale cómo obtenerla; no inventes.
- **Pide pago:** detente y pasa la referencia.
- **No hay trámite en línea:** genera la hoja de datos y explícale el trámite
  presencial o por correo.

## Éxito
Folio/acuse capturado y hoja de datos entregada. Si el registro no es obligatorio,
recuérdale que igual es útil como prueba.
