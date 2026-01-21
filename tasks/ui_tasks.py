import os
from dotenv import load_dotenv
load_dotenv()
import allure
from tests.conftest import page_manager
from utilities.email_getter import EmailExtractor
from utilities.logging import log_info
class Tasks:
    @allure.step("Navigate to Sign In Page")
    def navigate_to_sign_in_modal(page_manager):
        log_info("Navigate to Sign In Page")
        page_manager.home_page.navigate()
        page_manager.home_page.click_on_sign_in_btn()
    @allure.step("Register and Verify via Gmail")
    def complete_registration(page_manager, user):
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        page_manager.signin_page.click_on_sign_up_link()
        log_info(f"Filling registration form for: {user.email}")
        page_manager.signup_page.enter_email(user.email)
        page_manager.signup_page.enter_password(user.password)
        page_manager.signup_page.enter_confirm_password(user.confirm_password)
        page_manager.signup_page.click_on_sign_up_button()
        log_info("Fetching verification code from Gmail...")
        verification_code = EmailExtractor.extract_verification_code(user.email,app_password)
        log_info(f"Extracted code: {verification_code}")
        log_info("Entering verification code and finalizing registration")
        page_manager.signup_page.fill_verification_code(verification_code)
        page_manager.signup_page.click_on_continue_button()
        log_info("Success message checked")
        page_manager.signup_page.check_success_message()
    @allure.step("Complete Login")
    def complete_login(page_manager,user):
        page_manager.signin_page.click_on_sign_in_btn()
        log_info("Complete Login")
        page_manager.signin_page.enter_email(user.email)
        page_manager.signin_page.enter_password(user.password)
        page_manager.signin_page.click_on_sign_in_btn()
    @allure.step("Check Logged In User")
    def check_logged_in_user(page_manager,user):
        log_info(f"Check Username: {user.email}")
        page_manager.signin_page.check_username_button()