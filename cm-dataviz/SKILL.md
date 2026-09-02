---
name: cm-dataviz
category: analytics
version: "1.0"
shortDesc: "Generar gráficas y visualizaciones (PNG/SVG) con matplotlib y pandas."
description: >
  Usa esta skill cuando el usuario pida gráficas, charts, plots o visualizaciones
  de datos: barras, líneas, pie, scatter, heatmaps, distribuciones, series de
  tiempo, comparativas por plataforma/mercado/mes, dashboards estáticos.
  Genera imágenes PNG (o SVG) profesionales con matplotlib + pandas dentro del
  sandbox de Python, aplicando la paleta de marca de Chatmu.
tags: ["chart", "plot", "matplotlib", "pandas", "dataviz", "png", "svg"]
roles: ["Analytics", "Managers", "Artists"]
requiresTools: ["execute_python"]
compatibility: chatmu-agent-v3
---

# cm-dataviz — Data visualization con matplotlib

Genera gráficas para reportes, presentaciones y análisis usando **matplotlib** y
**pandas** dentro del sandbox de Python.

## Chatmu execution environment

- **NO ejecutes Python localmente.** Toda ejecución va por el tool `execute_python`,
  que corre en un sandbox aislado con matplotlib, pandas, numpy, pillow preinstalados.
- **Inputs**: si el usuario adjunta un CSV/JSON/XLSX, decláralo en `inputFiles` con
  `workspacePath` — llega al sandbox en `/workspace/in/<filename>`.
- **Outputs**: escribe siempre a `/workspace/out/<name>.png` (o `.svg`). Si vas a
  devolver un solo archivo, decláralo en `outputFiles: ["chart.png"]` — se copia al
  workspace del usuario automáticamente.
- **Cierra las figuras** con `plt.close(fig)` — el sandbox tiene memoria limitada.
- **DPI recomendado**: 150 para pantalla, 300 para impresión/PDF.

## Paleta de marca (Chatmu)

```
PRIMARY   = "#E11D48"   # rosa acento
DARK      = "#18181B"   # foreground
MUTED     = "#71717A"   # gris texto secundario
SURFACE   = "#F4F4F5"   # fondo cards
BORDER    = "#E4E4E7"   # bordes suaves
SUCCESS   = "#10B981"
WARNING   = "#F59E0B"
DANGER    = "#EF4444"
```

Para categorías múltiples usa esta secuencia (accesible + brand-aligned):

```
["#E11D48", "#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#14B8A6", "#F97316"]
```

## Patrón base — configurar matplotlib con estilo Chatmu

```python
import matplotlib
matplotlib.use("Agg")  # backend sin display, obligatorio en sandbox
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": "#E4E4E7",
    "axes.linewidth": 0.8,
    "axes.labelcolor": "#18181B",
    "axes.titlecolor": "#18181B",
    "axes.titleweight": "bold",
    "axes.titlesize": 13,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.color": "#71717A",
    "ytick.color": "#71717A",
    "grid.color": "#E4E4E7",
    "grid.linewidth": 0.5,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.bbox": "tight",
    "savefig.dpi": 150,
})

PRIMARY = "#E11D48"
PALETTE = ["#E11D48", "#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899"]
```

## Gráfica 1 — Barras horizontales (comparativa)

Ideal para: streams por plataforma, ingresos por mercado, top-N.

```python
data = pd.DataFrame({
    "plataforma": ["Spotify", "Apple Music", "YouTube", "Amazon", "Deezer"],
    "streams_m": [385, 112, 96, 41, 18],
})
data = data.sort_values("streams_m", ascending=True)

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.barh(data["plataforma"], data["streams_m"], color=PRIMARY, height=0.6)
ax.set_title("Streams mensuales por plataforma (millones)")
ax.set_xlabel("Streams (M)")
ax.grid(axis="x", linestyle="--", alpha=0.6)
ax.set_axisbelow(True)
for bar in bars:
    w = bar.get_width()
    ax.text(w + 5, bar.get_y() + bar.get_height() / 2, f"{w:,.0f}",
            va="center", fontsize=9, color="#18181B")
fig.savefig("/workspace/out/streams_por_plataforma.png")
plt.close(fig)
```

## Gráfica 2 — Línea de tiempo (evolución)

Ideal para: streams mensuales, oyentes, followers, ingresos por mes.

```python
df = pd.DataFrame({
    "mes": pd.to_datetime(["2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]),
    "streams_m": [1842, 1906, 1971, 2045, 2118, 2194],
})

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.plot(df["mes"], df["streams_m"], color=PRIMARY, linewidth=2.5, marker="o", markersize=7)
ax.fill_between(df["mes"], df["streams_m"], alpha=0.12, color=PRIMARY)
ax.set_title("Streams mensuales — últimos 6 meses")
ax.set_ylabel("Streams (M)")
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.set_axisbelow(True)
for x, y in zip(df["mes"], df["streams_m"]):
    ax.annotate(f"{y:,}", (x, y), textcoords="offset points",
                xytext=(0, 10), ha="center", fontsize=9, color="#18181B")
fig.autofmt_xdate()
fig.savefig("/workspace/out/streams_evolucion.png")
plt.close(fig)
```

## Gráfica 3 — Donut (distribución con centro libre para KPI)

Ideal para: cuota por plataforma, mix geográfico, distribución de género.

```python
labels = ["Spotify", "Apple Music", "YouTube", "Amazon", "Deezer", "Otros"]
values = [385, 112, 96, 41, 18, 6]
total = sum(values)

fig, ax = plt.subplots(figsize=(6, 6))
wedges, _ = ax.pie(values, colors=PALETTE, startangle=90,
                    wedgeprops=dict(width=0.35, edgecolor="white", linewidth=2))
ax.text(0, 0.08, f"{total:,}M", ha="center", va="center", fontsize=22,
        fontweight="bold", color="#18181B")
ax.text(0, -0.12, "streams/mes", ha="center", va="center", fontsize=10, color="#71717A")
ax.legend(wedges, [f"{l} · {v/total:.1%}" for l, v in zip(labels, values)],
          loc="center left", bbox_to_anchor=(1.05, 0.5), frameon=False, fontsize=9)
ax.set_title("Cuota de streaming por plataforma", pad=20)
fig.savefig("/workspace/out/cuota_plataformas.png")
plt.close(fig)
```

## Gráfica 4 — Barras agrupadas (comparativas)

Ideal para: comparar 2-3 series (este año vs. anterior, por plataforma × trimestre).

```python
import numpy as np

meses = ["Mar", "Abr", "May", "Jun", "Jul", "Ago"]
spotify = [1120, 1155, 1198, 1240, 1285, 1330]
apple = [340, 348, 358, 368, 378, 388]

x = np.arange(len(meses))
w = 0.38

fig, ax = plt.subplots(figsize=(9, 4.5))
ax.bar(x - w/2, spotify, w, label="Spotify", color=PALETTE[0])
ax.bar(x + w/2, apple, w, label="Apple Music", color=PALETTE[1])
ax.set_xticks(x, meses)
ax.set_ylabel("Streams (M)")
ax.set_title("Streams por plataforma — evolución mensual")
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="y", linestyle="--", alpha=0.6)
ax.set_axisbelow(True)
fig.savefig("/workspace/out/comparativa_plataformas.png")
plt.close(fig)
```

## Gráfica 5 — Heatmap (matriz)

Ideal para: audiencia por país × edad, streams por día × hora, correlaciones.

```python
import numpy as np

paises = ["MX", "ES", "AR", "CO", "US", "CL"]
edades = ["18-24", "25-34", "35-44", "45+"]
data = np.array([
    [3.2, 4.8, 2.1, 0.9],
    [2.8, 3.9, 1.7, 0.6],
    [1.9, 2.6, 1.2, 0.4],
    [1.5, 2.2, 1.0, 0.3],
    [0.9, 1.4, 0.7, 0.2],
    [0.6, 0.9, 0.4, 0.1],
])

fig, ax = plt.subplots(figsize=(7, 5))
im = ax.imshow(data, cmap="RdPu", aspect="auto")
ax.set_xticks(range(len(edades)), edades)
ax.set_yticks(range(len(paises)), paises)
ax.set_title("Oyentes mensuales (M) por país × edad")
for i in range(len(paises)):
    for j in range(len(edades)):
        color = "white" if data[i, j] > data.max() * 0.55 else "#18181B"
        ax.text(j, i, f"{data[i, j]:.1f}", ha="center", va="center",
                color=color, fontsize=9, fontweight="bold")
fig.colorbar(im, ax=ax, shrink=0.85, label="Oyentes (M)")
fig.savefig("/workspace/out/heatmap_pais_edad.png")
plt.close(fig)
```

## Cargar datos del workspace

Si el usuario aporta un CSV/XLSX/JSON, pásalo por `inputFiles`:

```python
# tool call from agent side:
# inputFiles: [{path: "streams.csv", workspacePath: "data/streams.csv"}]

import pandas as pd
df = pd.read_csv("/workspace/in/streams.csv")
# ... generar chart ...
```

Para Excel: `pd.read_excel("/workspace/in/data.xlsx", sheet_name="Sheet1")`.
Para JSON: `pd.read_json("/workspace/in/data.json")`.

## Generar varias gráficas en una sola llamada

Puedes escribir varios PNGs en la misma ejecución. Declara todos en `outputFiles`:

```
outputFiles: ["streams_por_plataforma.png", "streams_evolucion.png", "cuota.png"]
```

Cierra cada figura con `plt.close(fig)` antes de crear la siguiente.

## Reglas de estilo (obligatorias)

1. **Nunca uses el estilo default** de matplotlib — aplica el `plt.rcParams.update(...)` del patrón base.
2. **Ejes**: quita spines top y right (`axes.spines.top/right = False`).
3. **Grid**: solo en el eje relevante (`ax.grid(axis="y", ...)`), gris claro punteado.
4. **Etiquetas de valor**: siempre en barras (etiqueta encima o al lado).
5. **Formatea números grandes**: `f"{x:,.0f}"` para separadores de millares.
6. **Fechas**: usa `fig.autofmt_xdate()` para rotarlas.
7. **Colores**: primero PRIMARY para la serie principal, luego PALETTE para series adicionales.
8. **Título**: siempre, corto y descriptivo, sin punto final.

## Formatos de salida

- **PNG** (default) — para reportes .docx, presentaciones, web. `savefig.dpi=150` es suficiente.
- **SVG** — para escalado infinito. Cambia extensión y `savefig("...svg")`.
- **PDF** — para reports impresos. Cambia extensión.

## Errores comunes

- **"Cannot find display"** → falta `matplotlib.use("Agg")` antes de `import pyplot`.
- **Memoria/OOM en batch** → cierra figuras con `plt.close(fig)`.
- **Fuentes raras** → el sandbox solo tiene DejaVu Sans; no pidas Inter/Roboto.
- **Encoding en labels** → los strings van UTF-8, sin issues con acentos.
