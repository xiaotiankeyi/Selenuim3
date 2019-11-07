from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest

class Testloginsucceed(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "http://192.168.117.9:8080/jforum/forums/list.page"
        self.driver.get(url)

    def test_case(self):

        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('login').click()

        request = self.driver.find_element(By.ID, 'myprofile').text
        print(request)

        find_digit = self.driver.find_element_by_xpath("//table[@cellpadding='2']/tbody/tr[4]/td[4]").text
        # print(find_digit)

        """截图"""
        self.driver.save_screenshot(filename='loginSucceed.png')

    def tearDown(self):
        # sleep(2)
        self.driver.quit()