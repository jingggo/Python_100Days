"""

@Author:jyang
@Date:5/22/2019
"""
from PyPDF2 import PdfFileReader

with open('../res/Excel高手捷径：一招鲜，吃遍天.pdf', 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print("There are %d pages in the file." % reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    current_page = reader.getPage(19)
    print(current_page)
    print(current_page.extractText()) # .encode('utf-8').decode()


