"""

@Author:jyang
@Date:5/22/2019
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


wb = Workbook()
sheet = wb.active
data = [
    [1001, '白滚滚', '男', '123456789'],
    [1008, '糯米团子', '男', '132456789'],
]
sheet.append(['学号', '姓名', '性别', '电话'])

for row in data:
    sheet.append(row)

tab = Table(displayName='Sheet1', ref="A1:D5") #?

tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True
)
sheet.add_table(tab)

wb.save('../res/studentData.xlsx')