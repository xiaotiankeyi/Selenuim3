from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.gdhuida1688.com/crm_index/index")
sleep(2)
driver.find_element_by_id('username').send_keys('huida')
driver.find_element_by_id('password').send_keys('huida168')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/form/div[3]/button').click()
sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[3]/div[3]/span[2]").click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/a[1]').click()
sleep(3)

# iframe = driver.find_element_by_css_selector('#my_iframe')
'''切换进第一个iframe'''
driver.switch_to.frame('my_iframe')

driver.find_element_by_xpath("//div[@class='body_header']/form/div[3]/div[1]/a").click()
sleep(3)

'''切换进第二个iframe'''
driver.switch_to.frame('layui-layer-iframe1')
driver.find_element_by_css_selector("input[name='name']").send_keys('project')

'''切换回第一个iframe'''
driver.switch_to.parent_frame()

'''切换回主文档'''
driver.switch_to.default_content()

sleep(2)
driver.quit()
