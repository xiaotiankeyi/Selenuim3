from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

'''(.class)选择器'''
driver.find_element_by_css_selector(".xs0")

'''(#id)选择器'''
driver.find_element_by_css_selector("#ls_password")

'''通过属性定位[attribute=value]'''
accept = driver.find_element_by_css_selector("[title='最新回复']")
driver.find_element_by_css_selector("[class='pc']").click()
print(accept.text)
sleep(1)

driver.find_element_by_css_selector("[src='static/image/common/logo.png']")

"""标签名加属性"""
values = driver.find_element_by_css_selector("input[name='srchtxt']").get_attribute('id')
print(values)
sleep(2)

driver.quit()
