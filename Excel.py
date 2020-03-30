# -*- coding: utf-8 -*- 
"""
Project: test
Creator: wcm
Create time: 2020-03-28 18:01
IDE: PyCharm
Introduction:
"""

import xlrd  # 读取Excel库
import requests

# 1. 读取excel测试用例
excelDir = r'Api.xlsx'
# 打开Excel表
workbook = xlrd.open_workbook(excelDir)
# 查看所有的字表
# print(workbook.sheet_names())  # 列表格式
# workSheet=workbook.sheet_names()[1]
workSheet = workbook.sheet_by_name("Python")
# 读取一行
rows = workSheet.row_values(0)
# print(rows)
# 读取一列
cols = workSheet.col_values(1)
# print(cols)
# 读取某行某列
cellData = workSheet.cell_value(5, 4)
# print(cellData)

# print(workSheet.cell(1, 6).ctype)  # 单元数据类型 0,1：字符串,2,3,4,5
# 2. 构建接口对应请求
import json

# 2.1 获取token
token_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
token_data = {"userName": "J201903070064", "password": "362387359"}
headers = {"Content-Type": "application/json"}
resp = requests.post(token_url, data=json.dumps(token_data), headers=headers)
token = resp.json()['token']
print(token)

# 新增用户
addUser_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
addUser_data = json.load(cellData)  # 请求参数
addUser_headers = {"Content-Type": "application/json", "X-AUTH-TOKEN": token}
addUser_resp = requests.post(addUser_url, data=json.dumps(addUser_data), headers=addUser_headers)
print(addUser_resp.text)
res = addUser_resp.json()["message"]
if res == '成功':
    print("行政用户接口测试--》成功！耗时--》", addUser_resp.elapsed.total_seconds())
    excel_res = 'pass'
else:
    print("新增用户接口测试--》失败！")
    excel_res = 'fail'

# 3. 测试结果写入excel
import xlutils
from xlutils.copy import copy  # 复制函数

# 1- 首先打开Excel
# workbookWrite=xlrd.open_workbook(excelDir)
# 2- 复制Excel表副本
workbookWr = copy(workbook)
wrSheet = workbookWr.get_sheet(1)
wrSheet.write(1, 9, excel_res)  # 写单元格
workbookWr.save(r'Api1.xlsx')  # 保存
