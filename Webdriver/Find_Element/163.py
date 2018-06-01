from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver=webdriver.Firefox()
driver.get("http://music.163.com")
driver.maximize_window()
driver.switch_to_frame("g_iframe")
driver.find_element_by_xpath("//a[@class='icon-play f-fr']").click()
sleep(2)
driver.switch_to_default_content()
above=driver.find_element_by_xpath("//a[@class='btn']")
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath("//a[@data-action='share']").click()
driver.find_element_by_link_text("QQ登录").click()
all_l=driver.window_handles
driver.switch_to_window(all_l[1])

driver.switch_to_frame("ptlogin_iframe")
driver.find_element_by_xpath("//span[@id='img_out_402081019']").click()