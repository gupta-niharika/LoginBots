from selenium import webdriver
import os
import time
import pandas as pd                                          #for datasets to try sending username from it (loop it later)

class GmailBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sendmail = 'sanikchar@gmail.com'
        self.subject = 'Hey! it Gbot! ;) '

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

    def login(self):
        self.driver.get('https://www.gmail.com/')

        self.driver.find_element_by_name('identifier').send_keys(self.username)       #name(the name in the html page. go inspect)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(1)           #space to fill in pwd
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click() 
        time.sleep(1)

        '''
        self.driver.find_element('T-I J-J5-Ji T-I-KE L3').click()         #compose
        time.sleep(1)
        self.driver.find_element('/html/body/div[24]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea').send_keys(self.sendmail)    #sender's mail id
        time.sleep(1) 
        self.driver.find_element('subjectbox').send_keys(self.subject)
        time.sleep(1) 
        self.driver.find_element_by_xpath('/html/body/div[24]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div').send_keys('yolo!!!')
        self.driver.find_elements_by_class_name('//*[@id=":v6"]').click()
        time.sleep(1) 
        '''


data = pd.read_csv('mail.csv')
data = pd.DataFrame(data, columns = ['username', 'password'] )

if __name__ == '__main__':
    bot = GmailBot(data.username, data.password)      #send username and pwd 
