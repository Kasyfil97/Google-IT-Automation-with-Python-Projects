#!/usr/bin/env python3
#file for generating pdf file

from reportlab.platypus import SimpleDocTemplate #making simple template
from reportlab.platypus import Paragraph, Spacer, Table, Image #import paragraph, space, table, image
from reportlab.lib.styles import getSampleStyleSheet #import sheet
from reportlab.lib import colors #import color

def generate(filename, title, additional_info):
  """function for generating pdf file with title, additional info parameter"""
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["Normal"])
#  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black), #for generating table with outline
#                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
#                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
#  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])#build pdf
