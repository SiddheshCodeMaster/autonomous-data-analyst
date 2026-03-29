import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(steps, filename="report.pdf"):

    # Save in a fixed folder
    output_path = os.path.join(os.getcwd(), filename)

    doc = SimpleDocTemplate(output_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Autonomous Data Analyst Report", styles["Title"]))
    content.append(Spacer(1, 20))

    for step in steps:
        content.append(Paragraph(step["step"], styles["Heading2"]))
        content.append(Spacer(1, 10))

        text = step["output"].replace("\n", "<br/>")
        content.append(Paragraph(text, styles["BodyText"]))
        content.append(Spacer(1, 20))

    doc.build(content)

    return output_path
    