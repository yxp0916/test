from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://passport.jd.com/new/login.aspx")
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_id("loginname").send_keys("yxp0916")
driver.find_element_by_id("nloginpwd").send_keys("yxp@19840916")
driver.find_element_by_link_text("登    录").click()