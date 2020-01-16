from selenium import webdriver
import time
import  unittest
from Pages.LoginPage import loginPage
from Pages.HomePage import HomePage
from Pages.Passwards import Passwords
import HtmlTestRunner
import sys
sys.path.append("/Users/oleksandrlitvincuk/Desktop/Python/PayOp")

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/oleksandrlitvincuk/Downloads/chromedriver2")
        cls.driver.implicitly_wait(10)
    def test_login_valid(self):
        driver = self.driver

        driver.get('https://payop.com/ru/auth/login')


        login = loginPage(driver)
        login.enter_username(Passwords.corect_username)
        login.enter_password(Passwords.corect_password)
        login.click_login_buton()
        #time.sleep(0.9)
        assert self.driver.title == "PayOp - Merchant Panel"

        homepage = HomePage(driver)
        homepage.clik_on_email()
        homepage.clik_on_exit()




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/oleksandrlitvincuk/Desktop/Python/PayOp/Reports'))
