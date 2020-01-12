from selenium import webdriver
import time
import  unittest
from Pages.LoginPage import loginPage
from Pages.HomePage import HomePage
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
        login.enter_password(Passwords.corect_password)
        login.click_login_buton()

        homepage = HomePage(driver)
        homepage.clik_on_email()
        homepage.clik_on_exit()
    #    time.sleep(2)

#        self.driver.find_element_by_id("email").send_keys("litvinchucksasha@gmail.com")
 #       self.driver.find_element_by_id("password").send_keys("sasha1990")
  #      self.driver.find_element_by_class_name("submit-btn").click()
   #     self.driver.find_element_by_xpath("//div[@class='account-info__email']").click()
#        time.sleep(2)
  #      self.driver.find_element_by_xpath("//label[@class='account-actions__action mat-ripple']").click()
#        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ =='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/oleksandrlitvincuk/Desktop/Python/PayOp/Reports'))