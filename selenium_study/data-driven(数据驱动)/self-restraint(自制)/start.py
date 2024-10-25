class login():
    #登录
    def user_login(self, driver, username, password):
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('login').click()

    #退出登录
    def exit(self, driver):
        driver.find_element_by_id('logout').click()