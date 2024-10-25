from selenium import webdriver
'''引入keys模块'''
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)
# sleep(3)

driver.find_element(By.ID, 'ls_username').send_keys('admin')
sleep(1)

addr = driver.find_element(By.NAME, 'password')
addr.clear()
addr.send_keys('admin')
sleep(1)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
sleep(3)

"""打印当前页面的url"""
now_url = driver.current_url
print(now_url)

"""打印当前页面的title"""
title = driver.title
print(title)

"""获取登入的用户名"""
login_username = driver.find_element_by_xpath("//div[@id='um']/p[1]/strong/a").text
if login_username == 'admin':
    print(login_username, "login succeed")
else:
    print("login failed")
sleep(2)

driver.close()