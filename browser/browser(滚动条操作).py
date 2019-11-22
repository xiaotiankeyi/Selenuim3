from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = "https://www.baidu.com"
driver.get(url)

# driver.minimize_window()

try:
    driver.find_element_by_id('kw').send_keys('selenium3')
    sleep(5)
    driver.find_element_by_id('su').click()
    sleep(2)

    '''操作滚动条'''
    js = "window.scrollTo(100,500);"
    driver.execute_script(js)
    sleep(3)

except NoSuchElementException as e:
    print(e)

finally:
    driver.quit()

#通过js操作元素
js = 'document.getElementById("元素").click()'
driver.execute_script(js)