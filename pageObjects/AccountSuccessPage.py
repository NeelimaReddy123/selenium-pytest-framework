from selenium.webdriver.common.by import By

from pageObjects.BasePage import Base_Page



class Account_Success_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    ACCOUNT_CREATION_MESSAGE = (By.XPATH, "//div[@id='content']/h1")
    def get_account_created_message(self):
        """Get account creation success message"""
        return self.get_element_text(self.ACCOUNT_CREATION_MESSAGE)
