from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

class QQ_mail(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        print("正在访问QQ邮箱")

    def test_mail_login(self):
        driver=self.driver
        driver.get("https://mail.qq.com")

        driver.switch_to_frame("login_frame")
        # driver.find_element_by_id("switcher_plogin").click()

        driver.find_element_by_id("u").send_keys("402081019")
        driver.find_element_by_id("p").send_keys("Yxp_045489")
        driver.find_element_by_id("login_button").click()
        print("QQ邮箱登录成功")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()