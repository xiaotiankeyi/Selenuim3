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

    """定位一组元素"""
    all = driver.find_elements_by_css_selector("input[type='checkbox']")
    num = 0
    for checkbox in all:
        num += 1
        if num == 2 or num == 3:
            checkbox.click()
        sleep(1)
    print('循环次数:',num)
    '''取消选择的√'''
    all.pop(-1).click()

except NoSuchElementException as e:
    print(e)

finally:
    sleep(10)
    driver.quit()