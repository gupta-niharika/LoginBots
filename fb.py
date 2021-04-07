from selenium import webdriver
import os
import time

class Facebookbot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get('https://www.facebook.com/login')
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()
        #logged in


if __name__ == '__main__':
    loginbot = Facebookbot('username', 'pwd')
