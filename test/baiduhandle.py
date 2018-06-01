from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

search_windows=driver.current_window_handle
print(search_windows)
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text(u'立即注册').click()

all_handls=driver.window_handles
print(all_handls)
for handle in all_handls:
    if handle!=search_windows:
        driver.switch_to_window(handle)
        print(driver.current_window_handle)
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys("222222")

        sleep(2)
for handle in all_handls:
    if handle==search_windows:
        driver.switch_to_window(handle)
        print(driver.current_window_handle)
        sleep(2)
        driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(2)
driver.quit()