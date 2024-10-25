from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = "http://192.168.117.9:8080/jforum/forums/list.page"
driver.get(url)
try:
    #登录
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    test_forum = driver.find_element_by_css_selector("[href='/jforum/forums/show/1.page']")
    print(test_forum.text)
    test_forum.click()

    driver.find_element_by_xpath("//a[@class='icon_new_topic']/img").click()

    driver.find_element_by_xpath("//div[@id='tabs10']/ul/li[3]/a/span").click()
    sleep(1)

    '''定位上传按钮,添加本地文件'''
    driver.find_element_by_name("file_0").send_keys(r"C:\Users\admin\Pictures\小橘子.jpg")
    sleep(2)
except NoSuchElementException as e:
    print(e)

finally:
    sleep(3)
    driver.quit()