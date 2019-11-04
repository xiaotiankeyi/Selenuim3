import os, sys
import unittest
from BSTestRunner import BSTestRunner
import time

Base_dir = os.getcwd()

# 测试用例执行路径
run_dir = os.path.join(Base_dir + '\\Testcase')


# 报告存放路径及报告名
result_dir = os.path.join(Base_dir + '\\result')
now_date = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime())


discover = unittest.defaultTestLoader.discover(run_dir, pattern='test*.py')

if __name__ == "__main__":
    report_file = result_dir + '\\report' + now_date + '.html'

    with open(report_file, 'ab+') as f:
        runner = BSTestRunner(stream=f,
                              title='接口自动化测试',
                              description='结果如下....')

        runner.run(discover)
    f.close()
