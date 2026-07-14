
from selenium.webdriver.common.by import By
from pageObjects.BasePage import Base_Page


class SearchPage(Base_Page):

    VALID_MACBOOK_PRODUCT_LINK = (By.LINK_TEXT, "MacBook Air")
    NO_PRODUCT_MESSAGE = (By.XPATH, "//input[@id='button-search']/following-sibling::p")

    def __init__(self, driver):
        super().__init__(driver)

    def display_status_of_valid_product(self):
        return self.is_element_displayed(self.VALID_MACBOOK_PRODUCT_LINK)

    def retrieve_no_product_message(self):
        return self.get_element_text(self.NO_PRODUCT_MESSAGE)