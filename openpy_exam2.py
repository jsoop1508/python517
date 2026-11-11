from openpyxl import *

# == 시트 생성 ==
w2 = load_workbook('openpyxl/test.xlsx')

# 새로운 시트 하나 생성
new_ws = w2.create_sheet()

new_ws.title = '마지막_시트'

# 새로운 시트 하나 생성
new_ws = w2.create_sheet()

