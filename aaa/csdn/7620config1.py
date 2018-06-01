from selenium import webdriver

driver=webdriver.Firefox()
#打开网页
driver.get("http://192.168.19.1/login.html")
#输入升级地址
driver.find_element_by_id("updateUrl").clear()
driver.find_element_by_id("updateUrl").send_keys("http://120.27.48.117/update/update.bin")

#设置ssid3
driver.find_element_by_id("updateBtn").click()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
print("恭喜您,设置成功啦!")
driver.quit()