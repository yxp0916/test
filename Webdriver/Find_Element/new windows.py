from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(1)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'a')
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# driver.find_element_by_id('kw').send_keys("Selenium automation")
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL+'a')
# driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)

# driver.execute_script("window.alert('这是一个alert弹框。');")

driver.get("https://tieba.baidu.com/index.html")
# sleep(1)
# target_elem = driver.find_element_by_link_text("地区")
# driver.execute_script("return arguments[0].scrollIntoView();",target_elem)



aaa=driver.find_element_by_link_text("游戏")
driver.execute_script("return arguments[0].scrollIntoView();",aaa)