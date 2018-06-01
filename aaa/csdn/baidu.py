from selenium import webdriver
# import logging
# logging.basicConfig(level=logging.DEBUG)
driver=webdriver.Firefox()
driver.get("http://www.youdao.com")
print(driver.title)
assert "有ff道" in driver.title
driver.quit()