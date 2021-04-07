from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time
import configparser
#import pandas as pd

class InstagramBot:

    def __init__(self, username, password):
        self. username = username
        self.password = password
        self.base_url= 'https://www.instagram.com'
        self.driver = webdriver.Chrome() 

    def closeBrowser(self):         
        self.driver.close()

    def login(self):
        #pop up notifs solution
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", { 
            "profile.default_content_setting_values.notifications": 2   #1 -> 2 
        })

        self.driver = webdriver.Chrome(options=option, executable_path='chromedriver.exe')
        self.driver.get("{}/accounts/login/".format(self.base_url))

        #login autofill        
        enter_username = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        time.sleep(1)
        enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        #login
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()     
        time.sleep(1)
        
        #login successful
    
    '''
    def like_photo(self):
        #self.hashtag = hashtag
        #self.driver.get("https://www.instagram.com/explore/tags/cats/")
        self.driver.find_element_by_class_name('bqXJH')[0].click()
        time.sleep(1)
    '''

if __name__ == '__main__':

    nikkiIG = InstagramBot('usernmae', 'pwd')     # type ur insta username and pwd
    nikkiIG.login()
    #nikkiIG.like_photo('cats')
