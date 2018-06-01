from selenium import webdriver
from time import sleep

class ClassA():
    def open_baidu(self):
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://www.baidu.com")
        sleep(2)
        driver.quit()