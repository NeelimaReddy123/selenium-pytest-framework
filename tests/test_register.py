import time
from datetime import datetime
import logging
import pytest

from pageObjects.Homepage import Home_Page
from utils.email_utils import generate_email


@pytest.mark.order(3)  # Set the desired order for this test file
class TestRegister():
    def test_register_mandatory_fields(self,driver):
        logging.info("test_register--> test_register_mandatory_fields started")

        home_page = Home_Page(driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_new_account("test_11", "test", generate_email(), "8898898987", "qwerty456", "qwerty456", False, True)
        print(account_success_page)
        exp_txt = "Your Account Has Been Created!"
        assert account_success_page.get_account_created_message() == exp_txt

        logging.info("test_register--> test_register_mandatory_fields completed\n")

    def test_register_all_fields(self,driver):
        logging.info("test_register--> test_register_all_fields started")

        home_page = Home_Page(driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_new_account("Arjun", "reddy", generate_email(), "32423", "Arjun@456", "Arjun@456", True, True)
        exp_txt = "Your Account Has Been Created!"
        assert account_success_page.__eq__(exp_txt)
        logging.info("test_register--> test_register_all_fields completed\n")

    def test_register_existing_mail(self,driver):
        logging.info("test_register--> test_register_existing_mail started")

        home_page = Home_Page(driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_new_account("Neelima", "Reddy", "Madanapalli123@gmail.com", "8723456781", "neel@456", "neel@456", False, True)
        exp_txt = "Warning: E-Mail Address is already registered!"
        assert register_page.get_general_warning_message().__contains__(exp_txt)

        logging.info("test_register--> test_register_existing_mail completed\n")

    def test_register_without_anyfields(self,driver):
        logging.info("test_register--> test_register_without_anyfields started")

        home_page = Home_Page(driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_new_account("", "", "", "", "", "", False, False)
        exp_privacy_policy_msg = "Warning: You must agree to the Privacy Policy!"
        exp_frs_name_warn_msg = "First Name must be between 1 and 32 characters!"
        exp_lst_name_warn_msg = "Last Name must be between 1 and 32 characters!"
        exp_email_warn_msg = "E-Mail Address does not appear to be valid!"
        exp_phone_warn_msg = "Telephone must be between 3 and 32 characters!"
        exp_pswd_warn_msg = "Password must be between 4 and 20 characters!"

        expected_warning_msgs = [exp_privacy_policy_msg, exp_frs_name_warn_msg,
                                 exp_lst_name_warn_msg, exp_email_warn_msg,
                                 exp_phone_warn_msg, exp_pswd_warn_msg]
        msg_compare_results = register_page.verify_all_warning_messages(expected_warning_msgs)
        for x in range(len(msg_compare_results)):
            assert msg_compare_results[x], f"expected warning message not coming:{expected_warning_msgs[x]}"

        logging.info("test_register--> test_register_without_anyfields completed\n")

