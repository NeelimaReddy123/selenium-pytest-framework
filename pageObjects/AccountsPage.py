from selenium.webdriver.common.by import By
from pageObjects.BasePage import Base_Page

class Accounts_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    ACCOUNT_INFO_LINK = (By.LINK_TEXT, "Edit your account information")

    def is_account_info_visible(self) -> bool:
        """Return True if 'Edit your account information' link is visible."""
        return self.is_element_displayed(self.ACCOUNT_INFO_LINK)

