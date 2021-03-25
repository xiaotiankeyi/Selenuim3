from selenium import webdriver
from time import sleep


url = "https://s90999.com/#/home"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

driver.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/span[2]/i').click()
driver.find_element_by_id('userName').send_key('laizhitian')
driver.find_element_by_id('password').send_key('5764587a')




# sleep(5)
# driver.quit()
#1%存款倍打码

