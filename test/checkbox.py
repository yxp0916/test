from selenium import webdriver

from time import sleep
import os

dr=webdriver.Firefox()
# dr.get("file:///D:/yxp/Pythonsript/test/checkbox.html")
file_path='file:///'+os.path.abspath('checkbox.html')
dr.get(file_path)

checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
print(len(dr.find_elements_by_css_selector('input[type=checkbox]')))
sleep(2)

dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()

