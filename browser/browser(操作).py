from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

width = 1500
height = 1100
driver.set_window_size(width, height)
print('set_window_size 自空浏览器窗口大小宽度为{},高度为{}'.format(width, height))

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)
sleep(2)

driver.get("http://www.baidu.com")
sleep(2)

print('back() 后退<--------')
driver.back()
sleep(2)

print('forward() 前进------>')
driver.forward()
sleep(2)

print('refresh() 刷新当前页面')
driver.refresh()
sleep(2)

print('quit() 退出')
driver.quit()