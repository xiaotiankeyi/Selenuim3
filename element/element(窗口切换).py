from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.implicitly_wait(10)
url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

try:
    """清除cookies"""
    driver.delete_all_cookies()

    """登录"""
    driver.find_element(By.ID, 'ls_username').send_keys('admin')
    addr = driver.find_element(By.NAME, 'password')
    addr.clear()
    addr.send_keys('admin')
    '''提交登录'''
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    sleep(2)

    """获取首页窗口句柄"""
    home_windows = driver.current_window_handle
    print(home_windows)

    """进入管理中心"""
    driver.find_element_by_css_selector("[href='admin.php']").click()
    sleep(2)

    """获取所有窗口句柄"""
    all_windows = driver.window_handles
    print(all_windows)

    """切换窗口"""
    for i in all_windows:
        if i != home_windows:
            """切换到指定的window_name页签"""
            driver.switch_to.window(i)
            now_url = driver.current_url
            print(now_url)
            sleep(5)

    """返回首页窗口"""
    for v in all_windows:
        if v == home_windows:
            driver.switch_to.window(v)
            print(driver.current_url)

except NoSuchElementException as e:
    print(e)

finally:
    """关闭当前窗口"""
    # driver.close()
    """关闭浏览器"""
    sleep(5)
    driver.quit()
