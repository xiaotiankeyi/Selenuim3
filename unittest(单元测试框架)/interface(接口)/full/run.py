from ReadExcel import HandleExcel
from RequestsWay import RunMain

import unittest


class Testapitext(unittest.TestCase):
    # def __init__(self):
    #     self.data = HandleExcel()

    def test_run(self):
        self.data = HandleExcel()

        rows = self.data.get_rows()  # 获取有效行数

        for i in range(1, rows):  # 对行数进行循环遍历
            host = self.data.get_value(i, self.data.get_host())  # 获取ip地址

            path = self.data.get_value(i, self.data.get_path())  # 获取请求路径

            method = self.data.get_value(i, self.data.get_method())  # 获取请求方式

            select = self.data.get_value(i, self.data.get_opsions())  # 获取优先级


            data = self.data.get_value(i, self.data.get_database())            #获取请求参数
            if "=" in data:
                pass
                # print(data, type(data))
            else:
                data = eval(data)
                # print(data, type(data))

            assert_field = self.data.get_value(
                i, self.data.get_response_field())  # 获取断言字段
            # print(assert_field)

            assert_result = self.data.get_value(
                i, self.data.get_respones_result())  # 获取断言字段
            # print(assert_result)

            run = RunMain()
            url = host+path
            if select == "H":
                data = run.run_main(url, method, data,)
                if data.get(assert_field) == assert_result:
                    print('测试成功....\n', data)

                    self.data.write_values(i, self.data.get_resultvalue(), 'success')
                else:
                    print('测试失败......\n', data)

                    self.data.write_values(
                        i, self.data.get_resultvalue(), 'Failed')
            else:
                continue

if __name__ == "__main__":
    # run = apitext()
    # run.go_run()
    unittest.main()
