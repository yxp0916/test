from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("Selenium")
#driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")
#driver.find_element_by_xpath("//input[@name='wd']").send_keys("中午吃啥")
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("中午ss吃啥")

sleep(2)
driver.find_element_by_id("su").click()

driver.quit()