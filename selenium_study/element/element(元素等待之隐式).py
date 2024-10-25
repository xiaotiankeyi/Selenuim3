from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep,ctime
from selenium.webdriver.common.action_chains import ActionChains    #引入鼠标操作
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

driver = webdriver.Firefox()

"""设置隐式等待"""
driver.implicitly_wait(10)
url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.find_element(By.ID, 'ls_username').send_keys('admin')

"""设置显示等待"""
element = WebDriverWait(driver, 10, 0.5).until(ES.presence_of_element_located((By.ID, 'KW')))   #自定义
ele = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId"))     #官方提供

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