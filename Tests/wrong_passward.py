from selenium import webdriver
import  unittest
from Pages.LoginPage import loginPage
from Pages.Passwards import Passwords
import HtmlTestRunner

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
        login.enter_password(Passwords.wrong_password)
        login.click_login_buton()

        driver.find_element_by_xpath("//span[text()='User not found']")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/oleksandrlitvincuk/Desktop/Python/PayOp/Reports'))