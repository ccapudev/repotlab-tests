import os
#Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("/tmp/test.pdf", pagesize=A4)
story = []

# Ejemplo 01
t = Table([
    ['', 'Ventas', 'Compras'],
    ['Enero', 1000, 2000],
    ['Febrero', 3000, 100.5],
    ['Marzo', 2000, 1000],
    ['Abril', 1500, 1500]
], colWidths=80, rowHeights=30)
t.setStyle([
    ('TEXTCOLOR', (0, 1), (0, -1), colors.blue),
    ('TEXTCOLOR', (1, 1), (2, -1), colors.green),
    ('BACKGROUND', (1, 1), (-1, -1), colors.cyan),
    ('BOX', (1, 1), (-1, -1), 1.25, colors.yellow),
    ('INNERGRID', (1, 1), (-1, -1), 1, colors.red),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
])
story.append(t)
story.append(Spacer(0, 15))

# Ejemplo02
datos = (
    ('Nombre ciclo', 'Núm. Alumnos', 'Núm aprobados'),
    ('Desarrollo Aplic. Informáticas', 15, 5),
    ('Admin. Sist. Informáticos', 40, 25),
    ('Explotación Sist. Informáticos', 50, 20)
)
tabla = Table(data=datos,
              style=[
                  ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                  ('BOX', (0, 0), (-1, -1), 2, colors.black),
                  ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
              ]
              )
story.append(tabla)
story.append(Spacer(0, 15))

# Ejemplo 03
estiloTabla = TableStyle([
    ('LINEABOVE', (0, 0), (-1, 0), 2, colors.green),
    ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
    ('ROWBACKGROUNDS', (0, 0), (-1, -1), (colors.yellow, None)),

])
estiloTabla.add('BACKGROUND', (0, 0), (-1, 0), colors.Color(0, 0.7, 0.7))
t = Table([
    ['', 'Ventas', 'Compras'],
    ['Enero', 1000, 2000],
    ['Febrero', 3000, 100.5],
    ['Marzo', 2000, 1000],
    ['Abril', 1500, 1500]
], style=estiloTabla)

# Ejemplo 04: CELDAS COMPLEJAS
estilo = getSampleStyleSheet()
I = Image('imgs/tuxTemplario.jpg', width=100, height=100)

P1 = Paragraph('''El tux templario''', estilo["BodyText"])
P2 = Paragraph('''Viva Linux''', estilo["BodyText"])

t = Table(
    data=[
        ['A', 'B', 'C', P1, 'D'],
        ['00', '01', '02', [I, P2], '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']
    ],
    style=[
        ('GRID', (1, 1), (-2, -2), 1, colors.green),
        ('BOX', (0, 0), (1, -1), 2, colors.red),
        ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
        ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
        ('BACKGROUND', (0, 0), (0, 1), colors.pink),
        ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
        ('BACKGROUND', (2, 2), (2, 3), colors.orange),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (3, 0), (3, 0), 'BOTTOM'),
        ('BACKGROUND', (3, 0), (3, 0), colors.limegreen),
        ('BACKGROUND', (3, 1), (3, 1), colors.khaki),
        ('ALIGN', (3, 1), (3, 1), 'CENTER'),
        ('BACKGROUND', (3, 2), (3, 2), colors.beige),
        ('ALIGN', (3, 2), (3, 2), 'LEFT'),
    ]
)
story.append(t)

# Ejemplo 05: Combinación de celdas

t = Table(
    data=[
        ['Arriba\nIzquierda', '', '02', '03', '04'],
        ['', '', '12', '13', '14'],
        ['20', '21', '22', 'Abajo\nDerecha', ''],
        ['30', '31', '32', '', '']
    ],
    style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BACKGROUND', (0, 0), (1, 1), colors.palegreen),
        ('SPAN', (0, 0), (1, 1)),
        ('BACKGROUND', (-2, -2), (-1, -1), colors.pink),
        ('SPAN', (-2, -2), (-1, -1)),
    ])
story.append(Spacer(0, 10))
story.append(t)

doc.build(story)