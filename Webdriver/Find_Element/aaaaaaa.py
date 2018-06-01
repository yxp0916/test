import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://www.sohu.com')
        print(self.browser.title)
        self.assertIn('搜狐', self.browser.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)