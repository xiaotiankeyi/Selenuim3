from selenium import webdriver
import ddt
import time
import unittest

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "http://192.168.117.9:8080/jforum/forums/list.page"

    def LoginFunc(self, name, password):
        self.driver.get(self.url)
        self.driver.find_element_by_name('username').send_keys(name)
        self.driver.find_element_by_name('password').send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_name('login').click()
        time.sleep(2)
        self.driver.find_element_by_id('logout').click()

    @ddt.data(['admin', 'admin'], ['jack', '123456'], ['tom', '123456'])
    @ddt.unpack
    def test_case1(self, name, password):
        self.LoginFunc(name, password)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()