from selenium import webdriver
from time import sleep


driver=webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
driver.implicitly_wait(30)
driver.find_element_by_id("label_user").send_keys("13509652016")
driver.find_element_by_id("txtPass").send_keys("yxp_19840916")
driver.find_element_by_id("loginBtn").click()
print(driver.get_cookies())
driver.find_element_by_xpath("//li[@id='toptab_welcome']").click()
driver.switch_to_frame("welcome")
driver.find_element_by_xpath("//a[@id='smsSend']").click()
driver.switch_to.parent_frame()
driver.switch_to_frame("sms")
driver.find_element_by_xpath("//input[@class='addrText-input']").clear()
driver.find_element_by_xpath("//input[@class='addrText-input']").send_keys("18702934255")
driver.find_element_by_xpath("//textarea[@id='txtContent']").clear()
driver.find_element_by_xpath("//textarea[@id='txtContent']").send_keys("sss")
driver.find_element_by_xpath("//ul[@class='toolBarUl_v3']/li[2]").click()
sleep(3)
driver.quit()