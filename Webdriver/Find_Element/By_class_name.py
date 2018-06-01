from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("Http://www.baidu.com")
assert "百度一下"in driver.title
print(driver.title)
print(driver.name)
print(driver.session_id)
print(driver.current_url)
print(driver.current_window_handle)
print(driver.window_handles)
print(driver.get_window_position())
print(driver.get_window_size())

print(driver.find_element_by_id("kw").is_displayed())
print(driver.find_element_by_id("kw").location)
print(driver.find_element_by_id("kw").size)

driver.find_element_by_class_name("s_ipt").send_keys("Selenium")
sleep(3)

driver.find_element_by_id("su").click()
sleep(2)

driver.quit()