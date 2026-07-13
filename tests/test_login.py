import logging
import time

from pageObjects.Homepage import Home_Page
from utils.email_utils import generate_email

class TestLogin():
    # def test_valid_login(self, driver):
    #     logging.info("test_login--> test_login_valid_cred started")
    #     homepage=Home_Page(driver)
    #     login_page=homepage.navigate_to_login_page()
    #     account_page=login_page.login_with_credentials(email="Madanapalli123@gmail.com", password="neel@456")
    #     assert account_page.is_account_info_visible()
    #     logging.info("test_login--> test_login_valid_cred completed\n")

    def test_invalid_mail_and_valid_password_login(self,driver):
        logging.info("test_invalid_login--> test_invalid_login started")
        homepage=Home_Page(driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_with_credentials(email=generate_email(), password="neel@456")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed() == exp_warn_msg
        logging.info("test_invalid_login--> test_invalid_login completed\n")

    def test_valid_mail_and_invalid_password_login(self,driver):
        logging.info("test_invalid_login--> test_invalid_login started")
        homepage=Home_Page(driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_with_credentials(email="Madanapalli123@gmail.com", password="neel@123")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed() == exp_warn_msg
        logging.info("test_invalid_login--> test_invalid_login completed\n")

    def test_with_no_cred(self,driver):
        logging.info("test_with_no_cred--> test_with_no_cred started")
        homepage=Home_Page(driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_with_credentials(email="", password="")
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed() == exp_warn_msg
        logging.info("test_with_no_cred--> test_with_no_cred completed\n")
