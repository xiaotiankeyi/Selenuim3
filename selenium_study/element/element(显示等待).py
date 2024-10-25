from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

driver = webdriver.Chrome()

def findElement(driver, way, obj):
    """显示等待,是针对于某个特定的元素设置的等待时间"""
    try:
        WebDriverWait(driver, 5, 0.5).until(ES.presence_of_element_located((way, obj)))
        WebDriverWait(driver, 10).until(lambda x:x.presence_of_element_located(way, obj))
        return True
    except:
        return False