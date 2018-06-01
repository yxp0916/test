from time import sleep
from selenium import webdriver

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://m.mail.10086.cn")
sleep(2)
driver.find_element_by_id("label_user").send_keys("13509652016")
driver.find_element_by_id("txtPass").send_keys("yxp_19840916")
driver.find_element_by_id("loginBtn").click()
sleep(3)
driver.quit()