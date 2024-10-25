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

    # test_forum = driver.find_element_by_css_selector("[href='/jforum/forums/show/1.page']")
    # print(test_forum.text)
    # test_forum.click()

    # driver.find_element_by_xpath("//a[@class='icon_new_topic']/img").click()

    '''获取cookie'''
    cookie = driver.get_cookies()
    print(cookie)

    '''向cookie增加会话信息'''
    # driver.add_cookie({'name':'key-project', 'value':'value-teacher'})

    '''遍历cookie信息中的name和value'''
    for item in driver.get_cookies():
        print('key为:',item['name'],  '\tvalue为:',item['value'])

    '''清楚cookie'''
    # driver.delete_all_cookies()
    
except NoSuchElementException as e:
    print(e)

finally:
    driver.quit()