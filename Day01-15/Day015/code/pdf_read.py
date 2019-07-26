"""

@Author:jyang
@Date:5/22/2019
"""
from PyPDF2 import PdfFileReader

filename = r'E:\BaiduNetdiskDownload\EnglishPod 1-50\0001\englishpod_B0001.pdf'
with open(filename, 'rb') as f:
    reader = PdfFileReader(f, strict=False)
    print("There are %d pages in the file." % reader.numPages)
    if reader.isEncrypted:
        reader.decrypt('')
    content = ''
    for index in range(reader.numPages):
        current_page = reader.getPage(0)
        # print(current_page)
        # print(current_page.extractText()) # .encode('utf-8').decode()
        content += current_page.extractText() + '\n'
    with open(filename[:filename.rindex('.')+1] + '.txt', 'w') as tf:
        tf.write(content)

