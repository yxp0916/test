from selenium import webdriver
from time import sleep
import os

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('js.html')
driver.get(file_path)

button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()',button)
sleep(3)