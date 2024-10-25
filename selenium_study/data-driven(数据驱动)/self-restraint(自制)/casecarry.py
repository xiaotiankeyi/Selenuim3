from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from start import login

class logintest():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "http://192.168.117.9:8080/jforum/forums/list.page"
        self.driver.get(self.url)

        self.driver.implicitly_wait(10)
        self.size = self.driver.get_window_size()
        print(self.size)

    def loginhendle(self):
        try:
            with open('user.txt', 'r+') as f:
                while True:
                    data = f.readline()
                    if data is None or data == "":
                        break
                    data = data.split(',')

                    username = data[0]
                    password = data[1]
                    login().user_login(self.driver, username, password)
                    sleep(2)

                    accept = self.driver.find_element_by_xpath("//table[@cellpadding='3']/tbody/tr[3]/td/a/span")
                    print('目前在线会员:{}'.format(accept.text,))
                    accept.click()
                    sleep(2)

                    login().exit(self.driver)
                    sleep(1)
            f.close()
        except NoSuchElementException as e:
            print(e)

        finally:
            sleep(2)
            self.driver.quit()

if __name__ == "__main__":
    logintest().loginhendle()