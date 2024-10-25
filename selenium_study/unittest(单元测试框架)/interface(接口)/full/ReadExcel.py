import xlrd
from xlutils.copy import copy

'''
用于封装对Excel表的操作
'''

class HandleExcel():
    """封装操作excel的方法"""
    file_dir = r"C:/Users/jack/PycharmProjects/Selenuim3/unittest(单元测试框架)/interface(接口)/full/test_api.xlsx"
    new_file = r"C:/Users/jack/PycharmProjects/Selenuim3/unittest(单元测试框架)/interface(接口)/full/test_api_result.xlsx"

    def __init__(self, file=file_dir, sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()


    # 打开文件,获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_values(self, row, col, value):
        data = xlrd.open_workbook(self.file)
        data_copy = copy(data)
        sheet = data_copy.get_sheet(0)
        sheet.write(row, col, value)
        data_copy.save(self.new_file)       #创建新的表

    def get_apiName(self):
        """获取apiName用例名称"""
        apiName = 0
        return apiName

    def get_host(self):
        """获取url"""
        host = 1
        return host

    def get_path(self):
        """获取method请求方式"""
        path = 2
        return path

    def get_method(self):
        """获取params请求参数"""
        method = 3
        return method

    def get_opsions(self):
        """获取优先级"""
        opsions = 4
        return opsions

    def get_database(self):
        """获取请求数据"""
        re_data = 5
        return re_data

    def get_response_field(self):
        """获取响应字段"""
        response = 6
        return response

    def get_respones_result(self):
        "获取预期结果"
        result = 7
        return result

    def get_resultvalue(self):
        """获取要写入数据的单元格"""
        expect = 8
        return expect





if __name__ == '__main__':
    test = HandleExcel()
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(0, 6))
