from selenium.webdriver.common.by import By
from pageObjects.BasePage import Base_Page
from pageObjects.ProductsPage import Product_Details


class Accounts_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)

    ACCOUNT_INFO_LINK = (By.LINK_TEXT, "Edit your account information")
    DESKTOPS_CATEGORY_LINK = (By.LINK_TEXT, "Desktops")
    SHOW_ALL_OPTION_LINK = (By.LINK_TEXT, "Show AllDesktops")
    SHOPPING_CART_BUTTON = (By.XPATH, "//span[text()='Shopping Cart']")

    def is_account_info_visible(self) -> bool:
        """Return True if 'Edit your account information' link is visible."""
        return self.is_element_displayed(self.ACCOUNT_INFO_LINK)

    def click_on_desktops_catg(self):
        self.click_element(self.DESKTOPS_CATEGORY_LINK)

    def show_all_option(self):
        self.click_element(self.SHOW_ALL_OPTION_LINK)
        return Product_Details(self.driver)

    # def click_on_shopping_cart_button(self):
    #     self.click_element(self.SHOPPING_CART_BUTTON)
    #     return CartPage(self.driver)

    # methods for high level actions
    def navigate_to_product_page(self):
        self.click_on_desktops_catg()
        return self.show_all_option()
