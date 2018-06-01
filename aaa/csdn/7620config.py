from selenium import webdriver

driver=webdriver.Firefox()
#打开网页
driver.get("http://192.168.19.1/login.html")
#设置ssid1
driver.find_element_by_id("ssid1").clear()
driver.find_element_by_id("ssid1").send_keys("11111")
#设置ssid2
driver.find_element_by_id("ssid2").clear()
driver.find_element_by_id("ssid2").send_keys("2222")
#设置ssid3
driver.find_element_by_id("ssid3").clear()
driver.find_element_by_id("ssid3").send_keys("3333")
#设置ShopId
driver.find_element_by_id("shopId").clear()
driver.find_element_by_id("shopId").send_keys("594751")
#设置appId
driver.find_element_by_id("appId").clear()
driver.find_element_by_id("appId").send_keys("wx7c9fa144b23f8c61")
#设置"secretKey
driver.find_element_by_id("secretKey").clear()
driver.find_element_by_id("secretKey").send_keys("5bf0dac9035404e051f4f1d714eb3ed9")
#设置ssid3
driver.find_element_by_xpath("//button[@class='ui primary button center aligned']").click()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
print("恭喜您,设置成功啦!")
driver.quit()