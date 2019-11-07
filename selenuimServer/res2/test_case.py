from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, os, sys
from driver import is_Browser

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Testloginfailed(is_Browser):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     url = "http://192.168.117.9:8080/jforum/forums/list.page"
    #     self.driver.get(url)

    def test_case(self):
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin234234')
        self.driver.find_element_by_name('login').click()

        # 登录失败
        response = self.driver.find_element(By.ID,"invalidlogin").text
        print(response)

        """截图"""
        self.driver.save_screenshot(filename='loginFailed.png')

    # def tearDown(self):
    #     # sleep(5)
    #     self.driver.quit()