from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
print(driver.title)
title=EC.title_contains("百度一下")
print(title(driver))
title1=EC.title_is("百度一下，你就知道")
print(title1(driver))
driver.quit()