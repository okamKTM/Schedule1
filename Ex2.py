import os
import openpyxl

os.getcwd()
wb=openpyxl.load_workbook('example.xlsx')
sheet = wb.sheetnames
sheet1 = wb['Sheet1']

for cell_obj in list(sheet1.columns)[1]:
    print(cell_obj.value)

cell_obj = list(sheet1.columns)[1]
print(cell_obj)
