from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(20)

mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
driver.find_element_by_class_name("prefpanelgo").click()
sleep(3)
result=EC.alert_is_present()(driver)
if result:
    print(result.text)
    result.accept()
else:
    print("alert未弹出")
sleep(3)
driver.quit()