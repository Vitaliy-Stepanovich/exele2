import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="11111.xlsx")
# print(wb.sheetnames)
wb.active = 1

sheet = wb.active
# print(sheet["A1"].value)

for i in range(1, 2):
    print(sheet["A" + str(i)].value, sheet["B" + str(i)].value)
