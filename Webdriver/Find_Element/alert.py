from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)
driver.execute_script("window.alert('这是一个测试alert弹窗');")
sleep(2)
driver.switch_to_alert().accept()
