from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os
import uuid
import re


# =========================
# CLEAN TEXT FUNCTION 🔥
# =========================
def clean_text(text: str) -> str:
    text = str(text)

    # Remove markdown symbols
    text = re.sub(r"[*#`]", "", text)

    # Replace multiple newlines
    text = text.replace("\n\n", "\n")

    # Convert line breaks for reportlab
    text = text.replace("\n", "<br/>")

    return text.strip()


# =========================
# SECTION FORMATTER 🔥
# =========================
def add_section(title, body, styles):
    return [
        Paragraph(title, styles["Heading2"]),
        Spacer(1, 8),
        Paragraph(clean_text(body), styles["BodyText"]),
        Spacer(1, 20),
    ]


# =========================
# MAIN FUNCTION 🚀
# =========================
def generate_pdf_report(steps, charts=None):

    if charts is None:
        charts = []

    filename = f"report_{uuid.uuid4().hex}.pdf"
    output_path = os.path.join(os.getcwd(), filename)

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()

    # 🔥 Custom styling (clean + professional)
    styles.add(
        ParagraphStyle(
            name="CustomTitle",
            fontSize=18,
            leading=22,
            spaceAfter=20,
            textColor=colors.black,
        )
    )

    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            fontSize=14,
            leading=18,
            spaceAfter=10,
            textColor=colors.darkblue,
        )
    )

    styles.add(
        ParagraphStyle(
            name="CustomBody",
            fontSize=10,
            leading=14,
        )
    )

    content = []

    # =========================
    # TITLE
    # =========================
    content.append(Paragraph("Autonomous Data Analyst Report", styles["CustomTitle"]))
    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Generated using Agentic AI-driven analysis system", styles["BodyText"]
        )
    )
    content.append(Spacer(1, 25))

    # =========================
    # MAIN SECTIONS
    # =========================
    for step in steps:
        content.extend(add_section(step["step"], step["output"], styles))

    # =========================
    # CHARTS SECTION 📊
    # =========================
    if charts:
        content.append(Paragraph("Data Visualizations", styles["SectionTitle"]))
        content.append(Spacer(1, 10))

        for chart in charts:
            try:
                content.append(Image(chart, width=450, height=260))
                content.append(Spacer(1, 15))
            except Exception:
                continue

    # =========================
    # FOOTER NOTE
    # =========================
    content.append(Spacer(1, 30))
    content.append(
        Paragraph(
            "This report was generated automatically using Autonomous Data Analyst system.",
            styles["BodyText"],
        )
    )

    # Build PDF
    doc.build(content)

    return output_path
