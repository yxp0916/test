from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector("#kw").send_keys("Python")
element=driver.find_element_by_css_selector("#kw")
sleep(2)

ActionChains(driver).double_click(element).perform()
sleep(2)
ActionChains(driver).context_click(element).perform()
sleep(2)
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()
