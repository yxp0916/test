from selenium import webdriver
from time import sleep


driver=webdriver.Firefox()
driver.get("http://mail.163.com")
sleep(3)
print(driver.title)
print(driver.page_source)
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').send_keys('yxp0916')
driver.find_element_by_name('password').send_keys('yxp_841010')
driver.find_element_by_id('dologin').click()
sleep(3)
driver.quit()