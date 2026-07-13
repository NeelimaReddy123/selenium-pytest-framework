import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
from configparser import ConfigParser
import os
import time


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that creates and provides a Selenium WebDriver instance.
    Navigates to the base URL from config.ini before the test.
    Includes evasion measures for bot protection.
    """
    logging.info("Initializing Chrome WebDriver...")

    # Read URL from config.ini
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), "..", "utils", "config.ini")
    config.read(config_path)
    base_url = config.get("basic info", "url")

    # Configure Chrome options with evasion measures
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to run headless
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Evasion measures to avoid bot detection
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Create WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    # Execute script to hide automation indicators
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
        '''
    })

    # Implicit wait
    driver.implicitly_wait(10)

    # Navigate to base URL
    logging.info(f"Navigating to {base_url}")
    driver.get(base_url)
    

    # Wait for page to load and bot check to pass
    logging.info("Waiting for page to load...")
    time.sleep(3)

    yield driver

    # Teardown: close browser after test
    logging.info("Closing WebDriver...")
    driver.quit()