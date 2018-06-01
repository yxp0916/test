from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://news.baidu.com")
sleep(2)
for image in driver.find_elements_by_tag_name("img"):
    print(image.text)
    print(image.size)
    print(image.tag_name)
