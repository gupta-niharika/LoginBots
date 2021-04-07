from selenium import webdriver
import os
import time

class GmailBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get('https://www.gmail.com/')

        self.driver.find_element_by_name('identifier').send_keys(self.username)       #name(the name in the html page. go inspect)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(1)           #space to fill in pwd
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click() 

if __name__ == '__main__':
    ig_bot = GmailBot('username', 'pwd')      #send username and pwd 

    