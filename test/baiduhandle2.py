from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

search_windows=driver.current_window_handle
print(search_windows)
driver.find_element_by_link_text('登录').click()
sleep(2)
driver.find_element_by_link_text(u'立即注册').click()
all_handls=driver.window_handles
print(all_handls)
driver.switch_to_window(all_handls[1])
print(driver.title)
print(driver.current_window_handle)
driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys("222222")
driver.close()
driver.switch_to_window(search_windows)
print(driver.current_window_handle)
driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.quit()
