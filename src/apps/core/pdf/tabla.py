import os
from django.conf import settings

#Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


TMP_FILE = os.path.join('/tmp/', 'tmp.pdf')

doc = SimpleDocTemplate(TMP_FILE, pagesize = A4)
story=[]

#Ejemplo 01
t = Table([
    ['', 'Ventas', 'Compras'],
    ['Enero', 1000, 2000],
    ['Febrero', 3000, 100.5],
    ['Marzo', 2000, 1000],
    ['Abril', 1500, 1500],
    ['Mayo', 1500, 1500],
    ['Junio', 1500, 1500],
], colWidths=80,)
t.setStyle([
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
])
story.append(t)
story.append(Spacer(0,15))

doc.build(story)
