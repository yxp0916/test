from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(20)

mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
'''二次定位
# s=driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='20']").click()
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='50']").click()
'''
#直接定位
driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()

''' Select  模块 
# s=driver.find_element_by_id("nr")
# Select(s).select_by_index(2)
# Select(driver.find_element_by_id("nr")).select_by_index(2)
# Select(driver.find_element_by_id("nr")).select_by_value('20')
# Select(driver.find_element_by_id("nr")).select_by_visible_text("每页显示50条")
'''
driver.find_element_by_class_name("prefpanelgo").click()
#判断是否弹出alert
result=EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.accept()
else:
    print("alert未弹出")
driver.quit()