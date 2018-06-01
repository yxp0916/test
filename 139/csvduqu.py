from time import sleep
from selenium import webdriver
import os
import csv

list_username=[]
list_password=[]
data=csv.reader(file('D:\\yxp\\Pythonsript\\139\\userconfig.csv','rb'))
for user in data:
    print(user[0])
    list_username.append(user[0])
    print(user[1])
    list_password.append(user[1])

def login_139_by_csv():
    for i in range(len(list_username)):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get("http://m.mail.10086.cn")
        driver.find_element_by_id("label_user").send_keys(str(list_username[i]))
        driver.find_element_by_id("txtPass").send_keys(str(list_password[i]))
        driver.find_element_by_id("loginBtn").click()
        sleep(3)
        driver.quit()


