from selenium import webdriver
from time import sleep
import os

browser=webdriver.Firefox()
file_path='file:///'+os.path.abspath('frame.html')
browser.get(file_path)

browser.implicitly_wait(30)

browser.switch_to_frame("f1")
browser.switch_to_frame("f2")

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
browser.quit()