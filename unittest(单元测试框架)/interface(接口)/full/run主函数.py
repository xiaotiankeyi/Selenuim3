from ReadExcel import HandleExcel
import requests
from RequestsWay import RunMain

import unittest

class Testapitext(unittest.TestCase):
    # def __init__(self):
    #     self.data = HandleExcel()

    def test_run(self):
        self.data = HandleExcel()

        rows = self.data.get_rows()  # 获取有效行数
        # print(rows)

        for i in range(1, rows):    #对行数进行循环遍历
            # print(i)
            url = self.data.get_value(i, self.data.get_url())       #获取url
            # print(url)

            method = self.data.get_value(i, self.data.get_method())     #获取请求方式
            # print(method)

            data = eval(self.data.get_value(i, self.data.get_params()))     #获取请求数据
            # print(data, type(data))

            assertID = self.data.get_value(i, self.data.get_verifyID())         #请求断言数据ID
            # print(assertID)

            assertName = self.data.get_value(i, self.data.get_verifyName())         #请求断言数据name
            # print(assertName)

            run = RunMain()
            data = run.run_main(url, method, data,)
            if assertID and assertName in data:
                print('测试成功....\n', data)
                self.data.write_values(i, self.data.get_resultvalue(), 'pass')
            else:
                print('测试失败......\n', data)
                self.data.write_values(i, self.data.get_resultvalue(), 'Failed')



if __name__ == "__main__":
    # run = apitext()
    # run.go_run()
    unittest.main()