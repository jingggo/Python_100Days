"""

@Author:jyang
@Date:5/24/2019
"""
from docx import Document
from docx.oxml.ns import qn

file = Document()
file.styles['Normal'].font.name=u'微软雅黑'
file.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'微软雅黑')

transfer_file = '../../Day011/code/CNDaily_20190529.txt'
with open(transfer_file, 'r', encoding='utf-8') as f:
    file.add_paragraph(f.read().strip())

file.save(transfer_file[:transfer_file.rindex('.')+1] + 'docx')