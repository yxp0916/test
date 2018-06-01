from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
sleep(2)
driver.find_element_by_link_text("地图").click()
sleep(2)
driver.back()
sleep(2)
print(driver.current_url)
print(driver.title)
driver.forward()
sleep(2)
print(driver.capabilities['version'])
print(driver.current_url)
print(driver.title)
driver.quit()


