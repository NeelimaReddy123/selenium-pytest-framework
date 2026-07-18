import time

from selenium.webdriver.common.by import By

from pageObjects.AccountSuccessPage import Account_Success_Page
from pageObjects.BasePage import Base_Page


class Register_Page(Base_Page):
    """
    Register Page Object Model
    Handles user account registration
    """
    # ============ Locators ============
    FIRST_NAME_INPUT = (By.ID, "input-firstname")
    LAST_NAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, "input-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "input-confirm")
    AGREE_CHECKBOX = (By.NAME, "agree")
    CONTINUE_BUTTON = (By.XPATH, "//input[@value='Continue']")
    NEWSLETTER_CHECKBOX = (By.XPATH, "//input[@name='newsletter'][1]")
    WARNING_MESSAGE = (By.XPATH, "//div[contains(@class,'alert-danger')]")
    FIRST_NAME_WARNING = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    LAST_NAME_WARNING = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    EMAIL_WARNING = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
    TELEPHONE_WARNING = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    PASSWORD_WARNING = (By.XPATH, "//input[@id='input-password']/following-sibling::div")
    ACCOUNT_CREATION_MESSAGE = (By.XPATH, "//div[@id='content']/h1")

    # ============ Basic Actions ============

    def enter_first_name(self, first_name):
        """Enter first name"""
        self.type_into_element(first_name, self.FIRST_NAME_INPUT)

    def enter_last_name(self, last_name):
        """Enter last name"""
        self.type_into_element(last_name, self.LAST_NAME_INPUT)

    def enter_email(self, email):
        """Enter email"""
        self.type_into_element(email, self.EMAIL_INPUT)

    def enter_telephone(self, telephone):
        """Enter telephone number"""
        self.type_into_element(telephone, self.TELEPHONE_INPUT)

    def enter_password(self, password):
        """Enter password"""
        self.type_into_element(password, self.PASSWORD_INPUT)

    def enter_confirm_password(self, confirm_password):
        """Enter confirm password"""
        self.type_into_element(confirm_password, self.CONFIRM_PASSWORD_INPUT)

    def subscribe_to_newsletter(self):
        """Subscribe to newsletter"""
        self.click_element(self.NEWSLETTER_CHECKBOX)

    def agree_to_privacy_policy(self):
        """Agree to privacy policy"""
        self.click_element(self.AGREE_CHECKBOX)

    def click_continue(self):
        """Click continue button"""
        self.click_element(self.CONTINUE_BUTTON)


    # ============ Warning Messages ============

    def get_general_warning_message(self):
        """Get general warning message"""
        return self.get_element_text(self.WARNING_MESSAGE)

    def get_first_name_warning(self):
        """Get first name field warning"""
        return self.get_element_text(self.FIRST_NAME_WARNING)

    def get_last_name_warning(self):
        """Get last name field warning"""
        return self.get_element_text(self.LAST_NAME_WARNING)

    def get_email_warning(self):
        """Get email field warning"""
        return self.get_element_text(self.EMAIL_WARNING)

    def get_telephone_warning(self):
        """Get telephone field warning"""
        return self.get_element_text(self.TELEPHONE_WARNING)

    def get_password_warning(self):
        """Get password field warning"""
        return self.get_element_text(self.PASSWORD_WARNING)


    # ============ High-level Actions ============

    def register_new_account(self, first_name, last_name, email, telephone,
                             password, confirm_password, subscribe_newsletter=False,
                             agree_privacy=False):
        """
        Register a new account
        Returns AccountSuccessPage object
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

        if subscribe_newsletter:
            self.subscribe_to_newsletter()
        time.sleep(1)
        if agree_privacy:
            self.agree_to_privacy_policy()
        self.click_continue()
        return Account_Success_Page(self.driver)

    def verify_all_warning_messages(self, expected_warnings):
        """
        Verify all warning messages match expected messages
        Returns list of boolean values
        """
        actual_warnings = [
            self.get_general_warning_message(),
            self.get_first_name_warning(),
            self.get_last_name_warning(),
            self.get_email_warning(),
            self.get_telephone_warning(),
            self.get_password_warning()
        ]

        result = []
        for i in range(len(expected_warnings)):
            result.append(expected_warnings[i] == actual_warnings[i])

        return result