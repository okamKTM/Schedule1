import os
import openpyxl
import glob

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'test'
wb.save('test_write.xlsx')


