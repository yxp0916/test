from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()

    def  sousuo(self):
        driver=self.driver
        driver.get("http://www.baidu.com")
        self.assertIn("百度一下",driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()