# import pytest
# import logging
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from utils import read_configurations as rc
#
#
# # Ensure you have your other fixtures (log_on_failure, etc.) above this
#
# @pytest.fixture()
# def setup_and_teardown(request, worker_id):
#     global driver
#     browser = None
#     options = None
#
#     # 1. Read configurations from config.ini
#     exec_mode = rc.read_configuration("basic info", "execution")
#     run_env = rc.read_configuration("basic info", "run_environment")
#     browser_mode = rc.read_configuration("basic info", "browser_mode")
#     url = rc.read_configuration("basic info", "url")
#
#     # 2. Determine which browser to use
#     if exec_mode == 'standalone':
#         browser = rc.read_configuration("basic info", "browser")
#         logging.info(f"Running standalone on '{browser}' in '{run_env}' environment")
#     elif exec_mode == 'parallel':
#         browsers = ["chrome", "firefox", "edge"]
#         # Dynamically assign a browser based on the worker ID (gw0 -> chrome, gw1 -> firefox)
#         browser = browsers[int(worker_id.lstrip("gw")) % len(browsers)]
#         logging.info(f"Worker '{worker_id}' running parallel on '{browser}' in '{run_env}'")
#
#     # 3. Configure Browser Options
#     if browser == 'chrome':
#         options = ChromeOptions()
#     elif browser == 'firefox':
#         options = FirefoxOptions()
#     elif browser == 'edge':
#         options = EdgeOptions()
#     else:
#         raise ValueError(f"Browser '{browser}' is not supported.")
#
#     if browser_mode == 'headless':
#         options.add_argument("--headless")
#
#     # 4. Initialize the WebDriver
#     if run_env == 'local':
#         if browser == 'chrome':
#             driver = webdriver.Chrome(options=options)
#         elif browser == 'firefox':
#             driver = webdriver.Firefox(options=options)
#         elif browser == 'edge':
#             driver = webdriver.Edge(options=options)
#     elif run_env == 'remote':
#         # Connect to your Docker Selenium Grid
#         driver = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             options=options
#         )
#
#     # 5. Setup test environment
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     driver.get(url)
#
#     # 6. Attach driver to the BaseTest class so your tests can use 'self.driver'
#     request.cls.driver = driver
#
#     # 7. Pause fixture here while the test runs
#     yield
#
#     # 8. Teardown: Close the browser after the test finishes
#     driver.quit()
#
#
#
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

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
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