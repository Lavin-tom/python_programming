#! /usr/bin/python3

# openpyxl - manage excel file using python openpyxl libraries

import openpyxl as xl
wb = xl.load_workbook("sample.xlsx")
sheet = wb['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 1)

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 6)
    corrected_age = cell.value - 5
    corrected_age_cell = sheet.cell(row, 8)
    corrected_age_cell.value = corrected_age

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 4)
    if cell.value == "Male":
        corrected_gender = "M"
    else:
        corrected_gender = "F"
    corrected_gender_cell = sheet.cell(row, 9)
    corrected_gender_cell.value = corrected_gender

wb.save('test.xlsx')
