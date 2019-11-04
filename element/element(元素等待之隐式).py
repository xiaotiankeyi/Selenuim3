from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,ctime

"""引入鼠标事件"""
from selenium.webdriver.common.action_chains import ActionChains
"""引入隐式等待"""
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Firefox()

"""设置隐式等待"""
driver.implicitly_wait(10)
url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.find_element(By.ID, 'ls_username').send_keys('admin')

addr = driver.find_element(By.NAME, 'password')
addr.clear()
addr.send_keys('admin')

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
sleep(0.5)

try:
    print(ctime())
    stop = driver.find_element_by_css_selector("#qmenu")
    ActionChains(driver).move_to_element(stop).perform()
    sleep(2)
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.close()