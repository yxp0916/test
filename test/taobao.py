from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("https://www.taobao.com/")
driver.maximize_window()
sleep(2)
driver.find_element_by_link_text("亲，请登录").click()
driver.find_element_by_link_text("密码登录").click()
sleep(2)
driver.find_element_by_id("TPL_username_1").click()
driver.find_element_by_id("TPL_username_1").send_keys("yxp0916")
driver.find_element_by_id("TPL_password_1").clear()
driver.find_element_by_id("TPL_password_1").send_keys("yxp841010")
sleep(2)
driver.find_element_by_id("J_SubmitStatic").click()