from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.find_element(By.ID, 'ls_username').send_keys('admin')
sleep(1)

addr = driver.find_element(By.NAME, 'password')
addr.clear()
addr.send_keys('admin')
sleep(1)

driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
sleep(3)

"""鼠标悬浮事件"""
stop = driver.find_element_by_css_selector("#qmenu")
ActionChains(driver).move_to_element(stop).perform()
sleep(2)

"""鼠标双击事件"""
# double_click = driver.find_element_by_link_text('日志')
# ActionChains(driver).double_click(double_click).perform()
# sleep(2)

"""鼠标右击事件"""
# context_click = driver.find_element_by_id("")
# ActionChains(driver).context_click(context_click).perform()
# sleep(2)

driver.find_element_by_xpath("//div[@class='avt y']/a/img").click()
sleep(3)
driver.find_element_by_link_text('记录').click()
sleep(3)
driver.find_element_by_css_selector('.moodfm_input').click()
sleep(1)

"""鼠标拖放事件"""
text = driver.find_element_by_css_selector("[id='message']").send_keys("values")
sleep(1)
change = driver.find_element_by_xpath("//div[@id='message_menu']/ul/li[3]/img")
sleep(1)
ActionChains(driver).drag_and_drop(change, text).perform()
sleep(3)

driver.quit()
