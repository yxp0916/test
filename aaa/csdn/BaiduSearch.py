from selenium import webdriver
from time import sleep
import unittest

class BasiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(2)
        # print(self.driver.page_source)
        print(self.driver.title)
        print(self.driver.current_window_handle)
        print(self.driver.current_url)
        print(self.driver.name)
        print(self.driver.session_id)
        print(self.driver.find_element_by_id('kw').location)
        print(self.driver.find_element_by_id('kw').size)

        try:
            assert 'selen反反复复sium' in self.driver.title
            print('Test pass,')
        except Exception as e:
            print('Test Fail,',format(e))

if __name__=='__main__':
    unittest.main()