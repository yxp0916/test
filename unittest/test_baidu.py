'''
Created on 2018-1-22
@author:yxp
Project:登陆百度测试用例
'''


from selenium import webdriver
import unittest
from time import sleep

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.dirver=webdriver.Firefox()
        self.dirver.implicitly_wait(30)
        self.dirver.get("http://www.baidu.com")

    def test_baidu(self):
        driver=self.dirver
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        sleep(3)
        title=driver.title
        print(title)
        self.assertEqual(title,u"unittest_百度搜索")

    def test_baidu_search(self):
        self.dirver.find_element_by_id("kw").send_keys('selenium')
        sleep(3)
        print(self.dirver.title)
        try:
            assert 'selenium' in self.dirver.title
            print('Test Pass')
        except Exception as e:
            print('Test Fail.',format(e))

    def tearDown(self):
        self.dirver.quit()

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')

# suite=unittest.TestSuite()
# suite.addTest(BaiduTest('test_baidu'))
# suite.addTest(BaiduTest('test_baidu_search'))
#
# runner=unittest.TextTestRunner()
# runner.run(suite)