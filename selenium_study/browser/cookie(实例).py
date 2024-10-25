from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://192.168.117.9/bbs/upload/forum.php")

cok = driver.get_cookies()
print(cok)
sleep(2)


driver.find_element(By.ID, 'ls_username').send_keys('admin')
driver.find_element(By.ID, 'ls_password').send_keys('admin')
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

sleep(5)
now_cookie = driver.get_cookies()
print('登录后cookies',now_cookie)

driver.delete_all_cookies()
driver.refresh()

sleep(3)
driver.quit()


if __name__ == "__main__":
    pass