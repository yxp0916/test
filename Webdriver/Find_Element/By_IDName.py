from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("岐山")
# driver.find_element_by_name("wd").send_keys("我日")
# sleep(2)
# driver.find_element_by_id("su").click()
# ActionChains(driver).context_click(driver.find_element_by_id("kw")).perform()
ActionChains(driver).double_click(driver.find_element_by_id("kw")).perform()






sleep(5)
driver.quit()