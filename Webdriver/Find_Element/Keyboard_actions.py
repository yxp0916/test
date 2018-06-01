from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("Python")

sleep(2)

driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
#driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')
driver.get("http://www.sogou.com")
sleep(2)

driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
sleep(2)

driver.find_element_by_css_selector("#stb").click()
sleep(3)
