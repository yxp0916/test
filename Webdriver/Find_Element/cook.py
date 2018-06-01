from selenium import webdriver

from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

cks_1={"name":"BAIDUID","value":""}
cks_2={"name":"BDUSS","value":""}
driver.add_cookie(cks_1)
driver.add_cookie(cks_2)
sleep(5)
print(driver.get_cookies())
driver.refresh()
driver.quit()