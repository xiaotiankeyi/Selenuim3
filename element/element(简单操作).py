from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.find_element(By.ID, 'ls_username').send_keys('admin')
sleep(1)

addr = driver.find_element(By.NAME, 'password')
addr.clear()
addr.send_keys('admin')

"""获取元素的尺寸"""
print(addr.size)

"""获取元素的属性值"""
print(addr.get_attribute('type'))
sleep(1)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
sleep(3)

driver.find_element(By.CSS_SELECTOR, '#scbar_txt').send_keys('selenium')
driver.find_element(By.CSS_SELECTOR, '#scbar_btn').submit()
sleep(3)

"""
id_displayed(self)  检查元素是否可见
is_enabled(self)    判断元素是否被使用。。。
is_selected(self)   检查是否选择该元素
"""


driver.quit()



