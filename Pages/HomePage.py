from Locators.locators import Locators

class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.email_link_xpath = Locators.email_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath

    def clik_on_email(self):
        self.driver.find_element_by_xpath(self.email_link_xpath).click()

    def clik_on_exit(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()