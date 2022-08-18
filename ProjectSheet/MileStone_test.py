import os
import glob
import openpyxl
from openpyxl.styles.fonts import Font
#Excel = glob.glob("*.xlsx")


wb = openpyxl.load_workbook("Project.xlsx")
print(wb.sheetnames)
sheet = wb['Main']

cell = sheet['A1']
print(cell.value)