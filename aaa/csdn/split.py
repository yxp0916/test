from selenium import webdriver
from time import sleep

class GetSubString(object):
    def get_search_result(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(8)

        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('selenium')
        sleep(1)
        search_result_string = driver.find_element_by_xpath("//*/div[@class='nums']").text
        # print(search_result_string)

        new_string=search_result_string.split('约')[1]
        # print(new_string)

        last_result=new_string.split('个')[0]
        print(last_result)
        sleep(1)
        driver.quit()
getstring = GetSubString()
getstring.get_search_result()  