from selenium import webdriver
from time import sleep


url = "http://192.168.117.9:8080/jforum/user/login.page"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

c1 = {
    '3A3g_2132_editormode_e':'1',
    '3A3g_2132_forum_lastvisit':'D_36_1571259668D_37_1571269925',
    '3A3g_2132_lastvisit':'1571254505',
    '3A3g_2132_nofavfid':1,
    '3A3g_2132_saltkey':'yJ8jUWfJ',
    '3A3g_2132_smile':'1D1',
    '3A3g_2132_ulastactivity':'82a6Q335otiUZSnb1sjBEzK%2FnNWLCQ1gkouJQqyjLRchnRE19IB4',
    '3A3g_2132_visitedfid':'37D36',
    'jforumUserId':'2',
    'JSESSIONID':'AAF51B2D17B2E14333D56CDE9EA4B8E1'
}

driver.add_cookie(c1)

driver.get(url)
sleep(5)
driver.quit()