import xlsxwriter
import sys

# 測試過可以寫入到sheet1
XLSXTempPath = "c:\\euls\\Excel_Test1.xlsx"
xlswrWbk = xlsxwriter.Workbook(XLSXTempPath)
worksheet = xlswrWbk.add_worksheet("jacky_sheet_test1")
merge_format_all = xlswrWbk.add_format({'border': 1, 'border_color': 'black', 'bold': True})
merge_format = xlswrWbk.add_format({'border': 1, 'border_color': 'black', 'bold': True, "align" : "center"})
worksheet.set_column("B:B", 20)
worksheet.set_column("D:D", 50)
worksheet.merge_range("A1:" + "C1", "111", merge_format)
worksheet.merge_range("A2:" + "C2", "222", merge_format_all)
worksheet.merge_range("A3:" + "C3", "333", merge_format_all)
worksheet.merge_range("A4:" + "C4", "444", merge_format_all)
worksheet.merge_range("A5:" + "C5", "555", merge_format_all)
worksheet.merge_range("A6:" + "C6", "666", merge_format_all)
worksheet.write("D1", "DDD許", merge_format)
worksheet.write(5, 5, "55",merge_format)
xlswrWbk.close()