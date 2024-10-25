import csv
import codecs
import unittest
from itertools import islice
import time, os
from selenium import webdriver
import HTMLTestRunner


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.url = "http://192.168.117.9:8080/jforum/forums/list.page"
        cls.test_data = []
        with codecs.open('user.csv', 'r', encoding='utf8') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                # print(line)
                cls.test_data.append(line)

    def login_collect(self, name, password):
        self.driver.get(self.url)
        self.driver.find_element_by_name('username').send_keys(name)
        self.driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_name('login').click()
        time.sleep(2)
        self.driver.find_element_by_id('logout').click()

    def test_case1(self):
        """
        admin登录成功
        :return:
        """
        self.login_collect(self.test_data[0][0], self.test_data[0][1])

    def test_case2(self):
        """
        jack登录成功
        :return:
        """
        self.login_collect(self.test_data[1][0], self.test_data[1][1])

    def test_case3(self):
        """
        tom登录成功
        :return:
        """
        self.login_collect(self.test_data[2][0], self.test_data[2][1])

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()