---
name: chatmu-emerging-artist
description: Metodología de 6 meses para llevar a un artista musical emergente de cero a 1,000 oyentes mensuales, validando el repertorio en redes sociales antes de distribuir en streaming. Usar SIEMPRE que el usuario trabaje con un artista nuevo, sin catálogo distribuido, con menos de 1,000 oyentes mensuales, o pregunte cómo lanzar un proyecto desde cero, validar canciones antes de lanzarlas, estructurar los primeros sencillos, o pida un plan/roadmap/calendario para un artista debutante. Aplica a "artista sin oyentes", "primer lanzamiento", "estrategia para artista nuevo", o artistas del roster de Chatmu sin tracción aún. Trigger for any brand-new or pre-release artist, under 1,000 monthly listeners, or requests for a launch plan/content-validation strategy/roadmap for a debut act.
---

# Desarrollo de Artista Emergente (0 → 1,000 oyentes/mes)

Metodología de 6 meses para construir un proyecto artístico desde cero: valida el concepto y el repertorio en redes sociales *antes* de gastar presupuesto o capital de marca en una distribución oficial. La regla de oro: **el contenido guía las decisiones, no la intuición ni el gusto personal del equipo.**

Usa este skill como guion de trabajo completo cuando el usuario te pida ayuda con un artista en esta etapa. No apliques todas las fases de golpe si el usuario solo pregunta por una — identifica en qué fase está el artista y entra ahí directamente (ver "Cómo usar este skill" abajo).

## Cómo usar este skill

1. Pregunta o infiere en qué fase está el artista (identidad definida? repertorio grabado? ya está publicando contenido diario? ya sabe qué canciones validaron?). No repitas fases ya completadas.
2. Si el usuario tiene el artista cargado en Chatmu (tiene UUID en tus memorias o el usuario lo menciona), usa las tools de Chatmu para traer datos reales — no asumas cifras. Ver sección "Integración con Chatmu" abajo.
3. Entrega output accionable y específico: calendarios con fechas, listas de contenido, criterios de decisión — no teoría genérica.
4. Sé directo y crítico. Si el plan del usuario se salta la validación (por ejemplo "quiero distribuir ya" con 0 datos de redes), díselo — el riesgo de lanzar sin validar es quemar el mejor material sin saber si conecta.

---

## Fase 1 — Identidad artística (Semana 1)

Antes de grabar, define el proyecto. Pide o ayuda a construir:

- **5 artistas de referencia** que el artista admire + **5 proyectos comparables** activos y relevantes hoy (no referencias de hace 10 años).
- Para cada referencia, analizar: estilo musical, imagen, forma de comunicar, tipo de contenido, audiencia, valores del proyecto, frecuencia de lanzamientos.
- Responder a partir del análisis: ¿quién es su público? ¿qué los hizo crecer? ¿qué contenido publican? ¿cómo presentan su música? ¿qué los diferencia? ¿qué patrones se repiten entre todos?

**Entregable de la fase:** género musical, personalidad artística, estética, público objetivo y diferenciador — documentados en 1 página antes de escribir una sola canción.

---

## Fase 2 — Repertorio (Semanas 2 a 5)

Objetivo: **volumen, no perfección.** Meta: **15 maquetas.**

- No necesitan producción final — solo deben transmitir con claridad: melodía, letra, emoción, identidad.
- El objetivo es tener banco suficiente para que la Fase 3 (datos reales de audiencia) decida cuáles valen la pena, en vez de decidirlo el equipo por gusto.

---

## Fase 3 — Validación en redes sociales (30 días)

No se distribuye nada todavía. Se prueba el mercado con contenido.

- **1 publicación diaria** durante 30 días.
- Formatos: fragmentos de canciones, versiones acústicas, proceso creativo, storytelling, interpretación, tendencias adaptadas al catálogo, reacciones del público.
- Plataformas prioritarias: **TikTok** e **Instagram Reels**. YouTube Shorts se incorpora después, una vez identificado qué contenido funciona.
- El objetivo NO es conseguir seguidores. Es conseguir información. Rastrea para cada pieza de contenido: reproducciones, comentarios, guardados/compartidos (señal de intención más fuerte que views), y retención.

Preguntas que esta fase debe responder al final de los 30 días:
- ¿Qué canción genera más reproducciones?
- ¿Cuál obtiene más comentarios?
- ¿Cuál provoca que la gente la guarde o comparta?
- ¿Qué formato de video funciona mejor?
- ¿Qué tipo de contenido retiene más audiencia?

Cuando ayudes con esta fase, arma una tabla/tracker simple (canción × pieza de contenido × plataforma × views × comentarios × guardados/shares) para que la decisión de la Fase 4 sea con datos, no con opinión.

---

## Fase 4 — Selección de sencillos

Con los resultados de la Fase 3, selecciona **3 canciones** para el calendario de lanzamiento:

1. La canción con mejor respuesta (ganadora, validada por datos).
2. Una canción con desempeño medio.
3. Una canción con alto potencial artístico o comercial (aunque no haya sido la más viral) — esta es la apuesta estratégica del equipo, no solo la data.

---

## Fase 5 — Estrategia de lanzamiento (6 meses, ~2 meses por sencillo)

**Lanzamiento 1 (meses 1–2):** posicionar al artista, generar reconocimiento inicial, aprender qué contenido convierte mejor hacia streaming.

**Lanzamiento 2 (meses 3–4):** replicar el contenido que mejor funcionó en el Lanzamiento 1. No se empieza desde cero — se optimiza con lo aprendido.

**Lanzamiento 3 (meses 5–6):** mantener la línea de contenido con mejor rendimiento y aumentar volumen de publicaciones para consolidar el crecimiento.

**Después de cada lanzamiento, analizar:**
- Videos con más vistas / mayor retención / más comentarios / más compartidos / mejores guardados.
- Incremento de oyentes mensuales.
- Tasa de conversión de contenido social → streaming (si tienes acceso a Chatmu, usa `analyze_social_to_streaming_conversion` o `analyze_audience_conversion`).

El contenido ganador de cada ciclo se convierte en la base del siguiente sencillo. La estrategia se ajusta con datos reales, nunca con suposiciones.

---

## Metas de crecimiento (referencia, no promesa)

| Momento | Oyentes mensuales objetivo |
|---|---|
| Al iniciar | ~10 |
| Después del Lanzamiento 1 | ~100 |
| Después del Lanzamiento 2 | ~200 |
| Después del Lanzamiento 3 | ~400–500 |
| Meta de la etapa (con crecimiento orgánico sostenido, sin viralización) | ~1,000 |

Si algún contenido o canción se viraliza, estas metas pueden superarse antes de tiempo — pero no se debe planear asumiendo viralidad.

---

## Principios del método (no negociables al dar consejo)

- La música se valida **antes** de lanzarse — nunca al revés.
- El contenido guía las decisiones, no la intuición del equipo.
- Se construye comunidad antes que catálogo.
- Cada lanzamiento aprovecha explícitamente los aprendizajes del anterior — no se repite el mismo plan sin ajustar.
- Éxito = capacidad de generar audiencia recurrente y sostenible, no solo reproducciones o viralidad puntual.

---

## Integración con Chatmu (si el usuario tiene el conector activo)

Cuando el artista ya tenga UUID en Chatmu (aunque sea con pocos datos), usa las tools reales en vez de estimar a mano:

- **Fase 1 / referencias:** `find_similar_artists_advanced`, `find_genre_competitors` para encontrar y analizar proyectos comparables reales.
- **Fase 3 / validación:** `get_instagram_posts`, `analyze_instagram_media` para leer performance de contenido publicado; `get_platform_audience` para trackear crecimiento base.
- **Fase 4/5 / decisión y lanzamiento:** `audience_demographics`, `get_fans_dna_details` para afinar el ángulo de contenido antes del Lanzamiento 1; `get_artist_growth_trajectory` para proyectar el crecimiento esperado de cada ciclo.
- **Después de cada lanzamiento:** `analyze_social_to_streaming_conversion`, `get_artist_current_stats`, `geographic_growth_analysis` para el análisis post-lanzamiento de la fase 5.

Si el artista aún no está cargado en Chatmu, usa `search_artist` / `search_chatmu_artists_db` primero; si no existe, procede con el plan igual, apoyándote en investigación manual (redes del artista y de sus referencias) en vez de bloquear el trabajo.

## Output esperado

Cuando el usuario pida ayuda con un artista en esta etapa, entrega según lo que pida:
- Un documento/plan de fase específica (ej. solo el tracker de validación de 30 días), o
- El roadmap completo de 6 meses con fechas reales a partir de la fecha de inicio que dé el usuario.

Si el usuario no especifica formato, entrega en texto/markdown estructurado en el chat; solo genera un archivo (docx/xlsx) si el usuario pide explícitamente un documento o tracker descargable.
