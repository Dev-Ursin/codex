from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def build_pdf(title: str, subtitle: str, rows: list[dict]) -> bytes:
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    w, h = A4
    y = h - 18*mm

    c.setFont("Helvetica-Bold", 14)
    c.drawString(18*mm, y, title)
    y -= 7*mm
    c.setFont("Helvetica", 10)
    c.drawString(18*mm, y, subtitle)
    y -= 10*mm

    c.setFont("Helvetica-Bold", 10)
    c.drawString(18*mm, y, "Protocolo")
    c.drawString(52*mm, y, "Nome")
    c.drawString(120*mm, y, "Status")
    c.drawString(150*mm, y, "Prioridade")
    y -= 5*mm
    c.line(18*mm, y, w-18*mm, y)
    y -= 6*mm

    c.setFont("Helvetica", 9)
    for r in rows:
        if y < 18*mm:
            c.showPage()
            y = h - 18*mm
            c.setFont("Helvetica", 9)
        c.drawString(18*mm, y, str(r.get("protocolo",""))[:18])
        c.drawString(52*mm, y, str(r.get("nome",""))[:34])
        c.drawString(120*mm, y, str(r.get("status",""))[:14])
        c.drawString(150*mm, y, str(r.get("prioridade",""))[:10])
        y -= 5.2*mm

    c.showPage()
    c.save()
    return buf.getvalue()

