from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

url = "http://192.168.117.9/bbs/upload/forum.php"
driver.get(url)

driver.set_window_size(1300, 900)

# driver.refresh()

'''元素属性定位,如果不想指定标签名,用(*)号,使用xpath不局限于id,name,class三个属性值,
   元素的任意属性值都可以使用,只要它能唯一的标识一个元素。。'''
driver.find_element_by_xpath("//div[@id='category_lk']")
sleep(1)

driver.find_element_by_xpath("//img[@alt='官方论坛']")
sleep(1)

'''层级与属性结合'''
character = driver.find_element_by_xpath("//div[@class='lk_content z']/p")
print(character.text)
sleep(1)

string = driver.find_element_by_xpath("//dl[@id='onlinelist']/dd/ul/li")
print(string.text)
sleep(1)

choice = driver.find_element_by_xpath("//dl[@class='bm_c']/dt/img[2]")
print(choice.text)
sleep(1)

'''使用逻辑运算符(and)'''
request = driver.find_element_by_xpath("//button[@name='searchsubmit' and @id='scbar_btn']/strong")

driver.quit()
