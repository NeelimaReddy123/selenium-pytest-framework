import logging
import time

import pytest
from pageObjects.Homepage import Home_Page
from tests.base_test import BaseTest
from utils.email_utils import generate_email
from utils.excel_utils import get_data_from_excel


@pytest.mark.order(2)
class TestLogin(BaseTest):
    @pytest.mark.parametrize("email,password", get_data_from_excel("test_data_excel.xlsx", "valid_login"))
    def test_valid_login(self,email,password):
        logging.info("test_login--> test_login_valid_cred started")
        homepage=Home_Page(self.driver)
        login_page=homepage.navigate_to_login_page()
        account_page=login_page.login_with_credentials(email, password)
        assert account_page.is_account_info_visible()
        logging.info("test_login--> test_login_valid_cred completed\n")

    @pytest.mark.parametrize("email,password", get_data_from_excel("test_data_excel.xlsx", "Invalid_Login"))
    def test_invalid_login(self, email, password):
        logging.info("test_invalid_login--> test_invalid_login started")
        homepage=Home_Page(self.driver)
        login_page=homepage.navigate_to_login_page()
        login_page.login_with_credentials(email, password)
        exp_warn_msg = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.is_error_message_displayed() == exp_warn_msg
        logging.info("test_invalid_login--> test_invalid_login completed\n")


