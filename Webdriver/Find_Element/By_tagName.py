from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()

driver.get("Http://www.51zxw.net")

#driver.find_element_by_tag_name("input").send_keys("Selenium")
driver.find_elements_by_tag_name("input")[0].send_keys("Selenium")
sleep(3)

driver.quit()