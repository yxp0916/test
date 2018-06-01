from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")
driver.find_element_by_link_text("平面设计").click()
sleep(1)
driver.find_element_by_partial_link_text(" CC的工作界面(2)").click()
sleep(2)
driver.quit()