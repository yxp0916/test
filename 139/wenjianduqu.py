from time import sleep
from selenium import webdriver

username_file=open("D:\\yxp\\Pythonsript\\username.txt")
username=username_file.read()
password_fiel=open("D:\\yxp\\Pythonsript\\password.txt")
password=password_fiel.read()
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://m.mail.10086.cn")
sleep(2)
driver.find_element_by_id("label_user").send_keys(username)
driver.find_element_by_id("txtPass").send_keys(password)
driver.find_element_by_id("loginBtn").click()
sleep(3)
driver.quit()