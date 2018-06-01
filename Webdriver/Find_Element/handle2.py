from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://news.baidu.com/")
print(driver.current_window_handle)
sleep(2)
driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
print(driver.window_handles)

for handle in driver.window_handles:
    if handle!=driver.current_window_handle:
        print('switch to second window',handle)
        sleep(2)
        driver.close()
        driver.switch_to_window(handle)