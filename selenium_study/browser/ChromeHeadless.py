'''chrome无头浏览器'''
from selenium.webdriver.chrome.options import Options  # 导入相应的类
from selenium import webdriver
from time import sleep

chrome_options = Options()
chrome_options.add_argument('- -headless')
chrome_options.add_argument('- -disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(800, 800)
driver.get("http://www.baidu.com")
sleep(2)
driver.quit()
