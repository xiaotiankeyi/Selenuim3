"""处理下拉框"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


def elementFind(driver, way, str):
    """
    封装具有等待时间加判断的定位方法
    :param driver:
    :param way: 定位方式
    :param str: 要定位的元素
    :return:
    """
    try:
        element = WebDriverWait(driver, 5, 0.5).until(ES.presence_of_element_located((way, str)))
        return element
    except:
        return False


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

el = elementFind(driver, By.LINK_TEXT, '设置')
ActionChains(driver).move_to_element(el).perform()

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.setpref').click()

"""
1 select_by_index          # 通过索引定位
2 select_by_value          # 通过value值定位
3 select_by_visible_text   # 通过文本值定位
"""
time.sleep(1)
s = driver.find_element_by_css_selector("#nr")
Select(s).select_by_value('50')

# 二次定位方式
time.sleep(1)
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='20']").click()

time.sleep(3)
driver.quit()
