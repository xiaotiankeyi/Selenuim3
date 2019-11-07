from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
import os, multiprocessing
from selenium.webdriver import Remote

'''
grid启动不同的浏览器来执行测试用例
'''


def login_succeed(ip, browser):
    driver = Remote(command_executor=ip,
                    desired_capabilities={'platform': 'ANY',
                                          'browserName': browser,
                                          'version': '',
                                          'javascriptEnabled': True,
                                          })
    url = "http://192.168.117.9:8080/jforum/forums/list.page"
    driver.get(url)

    try:
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('password').send_keys('admin')
        driver.find_element_by_name('login').click()

        request = driver.find_element(By.ID, 'myprofile').text
        print(request)

        find_digit = driver.find_element_by_xpath("//table[@cellpadding='2']/tbody/tr[4]/td[4]").text
        print(find_digit)

        """截图"""
        driver.save_screenshot(filename='loginSucceed.png')

    except NoSuchElementException as e:
        print(e)

    finally:
        sleep(2)
        driver.quit()


if __name__ == "__main__":

    lists = {'http://127.0.0.1:5556/wd/hub': 'chrome',
             'http://127.0.0.1:5557/wd/hub': 'firefox', }

    all = []
    for ip, browser in lists.items():
        t = multiprocessing.Process(target=login_succeed, args=(ip, browser))
        all.append(t)

    for i in range(len(lists)):
        all[i].start()

    for i in range(len(lists)):
        all[i].join()
