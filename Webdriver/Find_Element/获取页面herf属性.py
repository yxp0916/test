from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)
# for link in driver.find_elements_by_xpath("//*[@href]"):
#     print(link.get_attribute('href'))
# driver.quit()
driver.get_screenshot_as_file("D:\\yxp\\图片\\yxp.png")