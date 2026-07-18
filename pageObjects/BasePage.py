import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# from pageObjects import Homepage


class Base_Page():
    """
    Base Page class containing common actions for all page objects.
    Uses Selenium's standard tuple locators: (By.XPATH, "value")
    """
    DEFAULT_TIMEOUT = 15
    def __init__(self, driver):
        self.driver = driver

    # ============ Explicit Waits ============

    def wait_for_element_visibility(self, locator):
        """Wait until element is visible (displayed)"""
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_for_elements_presence(self, locator):
        """Wait until all elements matching locator are present in DOM"""
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            ec.presence_of_all_elements_located(locator)
        )

    def wait_for_element_clickable(self, locator):
        """Wait until element is clickable"""
        return WebDriverWait(self.driver, self.DEFAULT_TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    # ============ Get Elements ============

    def get_element(self, locator):
        """Get single element without wait (for hidden elements)"""
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """Get list of elements matching locator"""
        return self.driver.find_elements(*locator)

    def get_element_with_wait(self, locator):
        """Get single element with explicit wait"""
        return self.wait_for_element_visibility(locator)

    # ============ Interactions ============

    def type_into_element(self, text, locator):
        """Type text into element"""
        element = self.wait_for_element_visibility(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        """Click on element"""
        element = self.wait_for_element_clickable(locator)
        element.click()

    def click_element_with_js(self, locator):
        """Click element using JavaScript (useful for hidden elements)"""
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # ============ Element Status ============

    def is_element_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.wait_for_element_visibility(locator)
            return element.is_displayed()
        except:
            return False

    def is_element_enabled(self, locator):
        """Check if element is enabled"""
        element = self.wait_for_element_visibility(locator)
        return element.is_enabled()

    # ============ Get Element Text & Attributes ============

    def get_element_text(self, locator):
        """Get text content of element"""
        element = self.wait_for_element_visibility(locator)
        return element.text

    def get_element_attribute(self, locator, attribute_name):
        """Get element attribute value"""
        element = self.wait_for_element_visibility(locator)
        return element.get_attribute(attribute_name)

    def get_elements_count(self, locator):
        """Get count of elements matching locator"""
        try:
            elements = self.get_elements(locator)
            return len(elements)
        except Exception as e:
            logging.error(f"Unable to retrieve elements count for locator: {locator}. Exception: {e}")
            return 0

    # ============ Dropdown Interactions ============

    def select_dropdown_by_index(self, locator, index):
        """Select dropdown option by index"""
        element = self.wait_for_element_visibility(locator)
        select = Select(element)
        select.select_by_index(index)

    def select_dropdown_by_text(self, locator, text):
        """Select dropdown option by visible text"""
        element = self.wait_for_element_visibility(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def select_dropdown_by_value(self, locator, value):
        """Select dropdown option by value attribute"""
        element = self.wait_for_element_visibility(locator)
        select = Select(element)
        select.select_by_value(value)

    # ============ File Upload ============

    def upload_file_using_send_keys(self, locator, file_path):
        """Upload file using send_keys (for visible file inputs)"""
        abs_file_path = os.path.abspath(file_path)
        element = self.wait_for_element_visibility(locator)
        element.send_keys(abs_file_path)

    def upload_file_using_hidden_locator(self, locator, file_path):
        """Upload file to hidden input element using JavaScript"""
        abs_file_path = os.path.abspath(file_path)
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, abs_file_path)

    # ============ Navigation ============

    def get_page_title(self):
        """Get current page title"""
        return self.driver.title

    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url

    def refresh_page(self):
        """Refresh the page"""
        self.driver.refresh()