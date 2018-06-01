from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://news.baidu.com')
news_link = driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a")
page1_title_string=news_link.text
print(page1_title_string)
news_link.click()
sleep(2)
for handle in driver.window_handles:
    if handle!=driver.current_window_handle:
        print('switch to second window',handle)
        driver.close()
        driver.switch_to_window(handle)
page2_title_string = driver.find_element_by_xpath("//div[@class='h-title']").text  # 详情页有一个原标题

try:
    assert page1_title_string in page2_title_string  # 判断页面B标题是否包含页面A标题
    print('Test Pass.')
except Exception as e:
    print('Test Fail')