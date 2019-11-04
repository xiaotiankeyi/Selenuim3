import xlrd
from xlutils.copy import copy

'''
xlutils用于向Excel文件中写入测试结果
'''
def text_write():
    file_dir = r"C:\Users\admin\Desktop\showdata.xlsx"
    data = xlrd.open_workbook(file_dir)
    # print(type(data))

    data_copy = copy(data)          #复制表
    # print(type(data_copy))

    sheet_copy = data_copy.get_sheet(0)     #取得复制文件的sheet对象

    sheet_copy.write(1, 9, '写入测试内容')    #在某一单元格写入数据

    data_copy.save(file_dir)       #保存
