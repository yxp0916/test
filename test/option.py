from selenium import webdriver
import os
from time import sleep

driver=webdriver.Firefox()
file_path='file:///'+os.path.abspath('drop_down.html')
driver.get(file_path)
sleep(2)

m=driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("//option[@value='10.69']").click()
sleep(2)
driver.quit()