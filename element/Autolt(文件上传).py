from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Firefox()
driver.implicitly_wait(10)

url = "https://www.coinebtoken.com/exchange_index/index"
driver.get(url)

try:
    driver.find_element_by_link_text('登录').click()

    #登录
    driver.find_element_by_name('username').send_keys('1610205119@qq.com')
    driver.find_element_by_name('password').send_keys(123456)
    driver.find_element_by_xpath("//div[@class='submit']/button").click()

    succeed = driver.find_element_by_css_selector("[class='title']")
    print(succeed.text)
    #悬浮
    ActionChains(driver).move_to_element(succeed).perform()

    driver.find_element_by_xpath("//ul[@class='head_nav']/li[10]/ul/li[2]/a").click()
    driver.find_element_by_link_text('认证').click()


except NoSuchElementException as e:
    print(e)

finally:
    sleep(3)
    driver.quit()