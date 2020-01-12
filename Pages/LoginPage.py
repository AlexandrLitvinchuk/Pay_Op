from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class loginPage():
    def __init__(self,driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.pasword_textbox_id = Locators.pasword_textbox_id
        self.loginbutton_class = Locators.loginbutton_class

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)


    def enter_password(self,password):
        self.driver.find_element_by_id(self.pasword_textbox_id).clear()
        self.driver.find_element_by_id(self.pasword_textbox_id).send_keys(password)

    def click_login_buton(self):
        self.driver.find_element_by_class_name(self.loginbutton_class).click()

    def fined_fail(self):
        self.driver.find_element_by_class_name

    def check_exists_by_xpath(self):
        try:
            webdriver.find_element_by_xpath("//span[@class='ng-tns-c1-0 ng-star-inserted']")
        except NoSuchElementException:
            return False
        return True