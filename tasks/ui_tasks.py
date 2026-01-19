import allure
from tests.conftest import page_manager
from utilities.logging import log_info
class Tasks:
    @allure.step("Navigate to Sign In Page")
    def navigate_to_sign_in_modal(page_manager):
        log_info("Navigate to Sign In Page")
        page_manager.home_page.navigate()
        page_manager.home_page.click_on_sign_in_btn()
    @allure.step("Complete Login")
    def complete_login(page_manager,user):
        log_info("Complete Login")
        page_manager.signin_page.enter_email(user.email)
        page_manager.signin_page.enter_password(user.password)
        page_manager.signin_page.click_on_sign_in_btn()
    @allure.step("Check Logged In User")
    def check_logged_in_user(page_manager):
        log_info("Check Username")
        page_manager.signin_page.check_username_button()