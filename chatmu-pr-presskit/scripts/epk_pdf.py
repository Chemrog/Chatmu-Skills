#!/usr/bin/env python3
"""Generate a .pdf press kit (EPK) from a JSON bundle.

Convention:
  - Read JSON from /workspace/in/epk.json (or first argv).
  - Write output to /workspace/out/EPK_<slug>.pdf.
Run only via the execute_python sandbox. reportlab is preinstalled.
"""
import json
import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def load_input() -> dict:
    path = sys.argv[1] if len(sys.argv) > 1 else "/workspace/in/epk.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build(epk: dict) -> None:
    title = epk.get("artist_name", "Artist")
    slug = epk.get("slug", title.lower().replace(" ", "-").replace("/", "-"))

    styles = getSampleStyleSheet()
    h1 = ParagraphStyle("h1", parent=styles["Title"], fontSize=24, leading=28, textColor=colors.HexColor("#0f172a"))
    h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontSize=14, leading=18, spaceBefore=10, textColor=colors.HexColor("#be123c"))
    body = ParagraphStyle("body", parent=styles["BodyText"], fontSize=10.5, leading=15)

    out_dir = "/workspace/out"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"EPK_{slug}.pdf")
    doc = SimpleDocTemplate(out_path, pagesize=A4, topMargin=20 * mm, bottomMargin=20 * mm)

    story = [Paragraph(title, h1)]
    if epk.get("tagline"):
        story.append(Spacer(1, 6))
        story.append(Paragraph(epk["tagline"], body))

    if epk.get("long_bio"):
        story.append(Paragraph("Biography", h2))
        story.append(Paragraph(epk["long_bio"], body))
    if epk.get("short_bio"):
        story.append(Paragraph("Short Bio", h2))
        story.append(Paragraph(epk["short_bio"], body))
    if epk.get("one_sheet"):
        story.append(Paragraph("One Sheet", h2))
        for item in epk["one_sheet"]:
            story.append(Paragraph(f"• {item}", body))
    if epk.get("stats"):
        story.append(Paragraph("Key Stats", h2))
        for stat in epk["stats"]:
            if isinstance(stat, dict):
                story.append(Paragraph(f"<b>{stat.get('label', 'Stat')}:</b> {stat.get('value', '')}", body))
            else:
                story.append(Paragraph(str(stat), body))
    if epk.get("tracks"):
        story.append(Paragraph("Key Tracks", h2))
        for t in epk["tracks"]:
            if isinstance(t, dict):
                story.append(Paragraph(f"• {t.get('title', '')} — {t.get('note', '')}".strip(" —"), body))
            else:
                story.append(Paragraph(f"• {t}", body))
    if epk.get("socials"):
        story.append(Paragraph("Connect", h2))
        for social in epk["socials"]:
            story.append(Paragraph(f"{social.get('network', 'Social')}: {social.get('handle', '')}", body))

    doc.build(story)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    build(load_input())
