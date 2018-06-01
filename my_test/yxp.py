'''
print("hello.51zxw")
print("are","you","OK?")
#打印整数
print(300)
print(300+200)
#打印变量
name='yxp'
print("Hello,%s"%name)

width=30
print("width is %d "%width)
'''
# con=input("please input Content")
# print("Content is %r"%con)
# coding=utf-8
import time
from selenium import webdriver


class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("selenium")
        time.sleep(1)
        print(self.driver.title)
        try:
            assert 'selenium_百度搜索' is self.driver.title
            print('Test pass.')

        except Exception as e:
            print('Test fail.')
        self.driver.quit()


baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()