from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
mouse=driver.find_element_by_link_text("设置")
sleep(3)
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)
# s=driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()
# Select(driver.find_element_by_id("nr")).select_by_value("50")
# Select(driver.find_element_by_id("nr")).select_by_index(2)
# Select(driver.find_element_by_id("nr")).select_by_visible_text("每页显示50条")
driver.find_element_by_xpath("//a[@class='prefpanelgo']").click()
alert=driver.switch_to_alert()
print(alert.text)
alert.accept()
# driver.switch_to_alert().accept()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()