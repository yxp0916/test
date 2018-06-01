from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

# driver.find_elements_by_tag_name('option')[1].click()
driver.find_element_by_css_selector('[value="3"]').click()
sleep(2)