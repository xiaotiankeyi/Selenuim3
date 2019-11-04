from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import os

base = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome()

url = "http://192.168.117.9:8080/jforum/forums/list.page"
driver.get(url)

try:
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    request = driver.find_element(By.ID, 'myprofile').text
    print(request)

    #登录失败
    # response = driver.find_element(By.ID,"invalidlogin").text
    # print(response)

    # tag = driver.find_element_by_css_selector("span[class='copyright']").is_displayed()
    tag = driver.find_elements_by_css_selector("[class='copyright']")
    print(tag[0].text)
    # for i in tag:
    #     print(i.text)

    find_digit = driver.find_element_by_xpath("//table[@cellpadding='2']/tbody/tr[4]/td[4]").text
    print(find_digit)

    """截图"""
    # driver.get_screenshot_as_file(r"C:/Users/admin/PycharmProjects/selenuim3/browser/error.png")
    # driver.get_screenshot_as_file(os.getcwd() + "error.png")

except NoSuchElementException as e:
    print(e)

finally:
    sleep(2)
    driver.quit()
    # driver.close()
