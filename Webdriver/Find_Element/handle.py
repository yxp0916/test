from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()


driver.get("http://www.ganji.com")
driver.implicitly_wait(2)
h=driver.current_window_handle
print(h)
driver.find_element_by_link_text("全职").click()
all_h=driver.window_handles
print(all_h)

# for i in all_h:
#     if i !=h:
#         driver.switch_to_window(i)
driver.switch_to_window(all_h[1])
print(driver.title)
driver.close()
driver.switch_to_window(h)
print(driver.title)
driver.quit()