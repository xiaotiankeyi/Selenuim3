from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()

url = "https://www.baidu.com"
driver.get(url)

try:
    collection = driver.find_element_by_xpath("//div[@id='u1']/a[8]")
    ActionChains(driver).move_to_element(collection).perform()
    print(collection.text)

    driver.find_element_by_css_selector(".setpref").click()


    driver.find_element_by_css_selector("[class='prefpanelgo']").click()

    '''获取弹窗里面的文本'''
    msg = driver.switch_to.alert.text
    print(msg)
    sleep(2)

    '''取消弹窗'''
    driver.switch_to.alert.dismiss()
    sleep(2)

    '''接受弹窗'''
    # driver.switch_to.alert.accept()


except NoSuchElementException as e:
    print(e)

finally:
    sleep(5)
    driver.quit()
    # driver.close()