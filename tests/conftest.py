import pytest
import logging
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize Chrome WebDriver.
    Reads application URL from config.ini.
    """

    logging.info("Initializing Chrome WebDriver...")

    # Read configuration
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__),   "..",   "utils", "config.ini")
    config.read(config_path)

    base_url = config.get("basic info", "url")

    # Chrome Options
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    # Local Chrome Driver
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)

    logging.info(f"Opening URL : {base_url}")
    driver.get(base_url)

    time.sleep(3)

    yield driver

    logging.info("Closing browser...")
    driver.quit()