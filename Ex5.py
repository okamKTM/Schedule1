import os
import openpyxl
import glob

wb=openpyxl.load_workbook('test_write.xlsx')
sheet = wb.active
sheet['A1'] = 'fixed'
wb.save('test_write.xlsx')

