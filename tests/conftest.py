import pytest
import logging
from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utils import read_configurations as rc


# ----------------------------
# Add custom command line option
# Example:
# pytest --browser firefox
# ----------------------------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store")
    parser.addoption("--env", action="store")
    parser.addoption("--execution", action="store")
    parser.addoption("--mode", action="store")


@pytest.fixture()
def setup_and_teardown(request):

    # ===========================
    # Read values from config.ini
    # ===========================
    execution = rc.read_configuration("basic info", "execution")
    run_environment = rc.read_configuration("basic info", "run_environment")
    browser_mode = rc.read_configuration("basic info", "browser_mode")
    url = rc.read_configuration("basic info", "url")

    # Browser from config.ini
    browser = request.config.getoption("--browser") \
              or rc.read_configuration("basic info", "browser")

    run_environment = request.config.getoption("--env") \
                      or rc.read_configuration("basic info", "run_environment")

    execution = request.config.getoption("--execution") \
                or rc.read_configuration("basic info", "execution")

    browser_mode = request.config.getoption("--mode") \
                   or rc.read_configuration("basic info", "browser_mode")

    logging.info(f"Execution Mode : {execution}")
    logging.info(f"Environment    : {run_environment}")
    logging.info(f"Browser        : {browser}")
    logging.info(f"Browser Mode   : {browser_mode}")

    # ===========================
    # Browser Options
    # ===========================

    if browser == "chrome":
        options = ChromeOptions()

    elif browser == "firefox":
        options = FirefoxOptions()


    elif browser == "edge":
        options = EdgeOptions()

    else:
        raise Exception(f"Unsupported browser : {browser}")

    # Headless

    if browser_mode == "headless":
        if browser in ["chrome", "edge"]:
            options.add_argument("--headless=new")

        elif browser == "firefox":
            options.add_argument("--headless")

    # Chrome & Edge specific

    if browser in ["chrome", "edge"]:
        options.add_argument("--disable-notifications")

    # ===========================
    # Driver Initialization
    # ===========================

    if run_environment.lower() == "local":

        if browser == "chrome":
            driver = webdriver.Chrome(options=options)

        elif browser == "firefox":
            driver = webdriver.Firefox(options=options)

        elif browser == "edge":
            driver = webdriver.Edge(options=options)

    elif run_environment.lower() == "remote":

        # FIXED: Routed via 127.0.0.1 and removed the legacy '/wd/hub' path for Selenium 4 Grid compatibility
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4444",
            options=options
        )

    else:
        raise Exception(f"Invalid run environment : {run_environment}")

    # ===========================
    # Browser Setup
    # ===========================

    driver.implicitly_wait(10)

    if browser_mode.lower() != "headless":
        driver.maximize_window()
    driver.get(url)

    # Make driver available to BaseTest
    request.cls.driver = driver

    yield

    logging.info("Closing Browser")

    driver.quit()