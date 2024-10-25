from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.set_window_size(1400, 900)

'''id定位'''
driver.find_element_by_id('ls_username').send_keys('admin')
sleep(1)

'''name定位'''
driver.find_element_by_name('password').send_keys('admin')
sleep(1)

'''css定位'''
driver.find_element_by_class_name("wp")
sleep(1)

'''link定位,专门定位文本链接'''
driver.find_element_by_link_text("论坛")
sleep(1)
driver.find_element_by_link_text("广播")

driver.quit()
