from  selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.maximize_window()
driver.get('https://news.baidu.com')
sleep(1)

driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
print(driver.current_window_handle)
print(driver.window_handles)

for hanle in driver.window_handles:
    if hanle !=driver.current_window_handle:
        print('switch to sencond window',hanle)
        driver.close()
        driver.switch_to_window(hanle)