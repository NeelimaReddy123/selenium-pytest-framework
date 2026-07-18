from pageObjects.AccountsPage import Accounts_Page
from pageObjects.BasePage import Base_Page
from selenium.webdriver.common.by import By

class LoginPage(Base_Page):
    def __init__(self,driver):
        super().__init__(driver)

    # inside class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    ERROR_MESSAGE = (By.XPATH, "//div[@id='account-login']/div[1]")

    # methods for basic actions
    def enter_email_address(self, email):
        self.type_into_element(email, self.EMAIL_INPUT)

    def enter_password(self, password):
        self.type_into_element(password, self.PASSWORD_INPUT)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
        return Accounts_Page(self.driver)

    def is_error_message_displayed(self):
        return self.get_element_text(self.ERROR_MESSAGE)

    # methods for high level actions
    def login_with_credentials(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        return self.click_login_button()
