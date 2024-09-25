from fpdf import FPDF
from fpdf.enums import Align

name = input("Name: ").strip().title()

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

pdf.set_font('Helvetica', 'B', 40)
pdf.cell(0, 30, 'CS50 Shirtificate', align='C')

pdf.image('shirtificate.png', x=Align.C, y=70, w=180)

pdf.set_font('Helvetica', 'B', 24)
pdf.set_text_color(255, 255, 255)
pdf.text(x=55, y=150, text=f'{name} took CS50')

pdf.output('shirtificate.pdf')
