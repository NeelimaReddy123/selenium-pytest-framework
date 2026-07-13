from selenium.webdriver.common.by import By
from pageObjects.BasePage import Base_Page
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import Register_Page


class Home_Page(Base_Page):
    """

    Home Page Object Model
    Represents the landing page of TutorialsNinja e-commerce application
    """
    # ============ Locators  ============
    def __init__(self, driver):
        super().__init__(driver)

    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-default')]")
    MYACCOUNT_DROPDOWN = (By.XPATH, "//span[normalize-space()='My Account']")
    LOGIN_LINK = (By.LINK_TEXT, "Login")
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    # ============ Basic Actions (Single interactions) ============

    def click_on_myaccount_dropdown_menu(self):
        self.click_element(self.MYACCOUNT_DROPDOWN)

    def click_register_link(self):
        """Click on Register link"""
        self.click_element(self.REGISTER_LINK)
        return Register_Page(self.driver)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)
        return LoginPage(self.driver)

    # ============ High-level Actions (Business workflows) ============

    def navigate_to_register_page(self):

        """
        Navigate to Register page via My Account dropdown
        Returns RegisterPage object
        """
        self.click_on_myaccount_dropdown_menu()
        return self.click_register_link()

    def navigate_to_login_page(self):
        self.click_on_myaccount_dropdown_menu()
        return self.click_login_link()
