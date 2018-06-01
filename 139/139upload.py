from selenium import webdriver
from time import sleep
import os

driver=webdriver.Firefox()
driver.get("http://m.mail.10086.cn")
driver.implicitly_wait(30)
driver.find_element_by_id("label_user").send_keys("13509652016")
driver.find_element_by_id("txtPass").send_keys("yxp_19840916")
driver.find_element_by_id("loginBtn").click()
# driver.find_element_by_xpath("/html/body/div[2]/ul[1]/li[5]/a/i").click()
driver.find_element_by_id("toptab_diskdev").click()
driver.switch_to_frame("diskDev")
driver.find_element_by_xpath("//span[contains(.,'新建文件夹')]").click()
driver.find_element_by_id("uploadFileInput").click()
driver.find_element_by_id("uploadFileInput").send_keys('D:\\111.txt')
sleep(3)
driver.quit()