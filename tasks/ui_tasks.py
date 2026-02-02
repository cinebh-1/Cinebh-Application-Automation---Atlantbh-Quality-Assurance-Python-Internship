import allure
import os
from dotenv import load_dotenv
from tests.conftest import page_manager
from utilities.email_getter import EmailExtractor
from utilities.logging import log_info
load_dotenv()

class Tasks:
    _page_manager = None

    @classmethod
    def set_page_manager(cls, page_manager):
        cls._page_manager = page_manager

    @staticmethod
    @allure.step("Navigate to Sign In Page")
    def navigate_to_sign_in_modal():
        log_info("Navigate to Sign In Page")
        Tasks._page_manager.home_page.navigate()
        Tasks._page_manager.home_page.click_on_sign_in_btn()

    @staticmethod
    @allure.step("Register and Verify via Gmail")
    def complete_registration(user):
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        Tasks._page_manager.signin_page.click_on_sign_up_link()
        log_info(f"Filling registration form for: {user['email']}")
        Tasks._page_manager.signup_page.enter_email(user["email"])
        Tasks._page_manager.signup_page.enter_password(user["password"])
        Tasks._page_manager.signup_page.enter_confirm_password(user["confirm_password"])
        Tasks._page_manager.signup_page.click_on_sign_up_button()
        log_info("Fetching verification code from Gmail...")
        verification_code = EmailExtractor.extract_verification_code(user["email"], app_password)
        log_info(f"Extracted code: {verification_code}")
        log_info("Entering verification code and finalizing registration")
        Tasks._page_manager.signup_page.fill_verification_code(verification_code)
        Tasks._page_manager.signup_page.click_on_continue_button()
        log_info("Success message checked")
        Tasks._page_manager.signup_page.check_success_message()

    @staticmethod
    @allure.step("Complete Login")
    def complete_login(user):
        log_info("Complete Login")
        Tasks._page_manager.signin_page.click_on_sign_in_btn()
        Tasks._page_manager.signin_page.enter_email(user["email"])
        Tasks._page_manager.signin_page.enter_password(user["password"])
        Tasks._page_manager.signin_page.click_on_sign_in_btn()

    @staticmethod
    @allure.step("Check Logged In User")
    def check_logged_in_user():
        log_info("Check Username")
        Tasks._page_manager.signin_page.check_username_button()

    @staticmethod
    @allure.step("Navigate to Currently Showing Page")
    def navigate_to_currently_showing_page():
        log_info("Navigate to Currently Showing Page")
        Tasks._page_manager.home_page.navigate()
        Tasks._page_manager.home_page.click_on_currently_showing_menu_item()

    @staticmethod
    @allure.step("Search movie, select city,cinema, genre and time")
    def search_movie_and_verify_selection(projection):
        log_info(f"Search Movie - {projection['search_term']}")
        Tasks._page_manager.currently_showing_page.enter_search_term(projection['search_term'])
        log_info(f"Select City - {projection['city']} ")
        Tasks._page_manager.currently_showing_page.select_city(projection['city'])
        log_info(f"Select Cinema - {projection['cinema']} ")
        Tasks._page_manager.currently_showing_page.select_cinema(projection['cinema'])
        log_info(f"Select Genre - {projection['genre']} ")
        Tasks._page_manager.currently_showing_page.select_genre(projection['genre'])
        log_info(f"Select Time - {projection['time']} ")
        Tasks._page_manager.currently_showing_page.select_time(projection['time'])
        log_info("Select Random Date - date tabs - currently showing page")
        Tasks._page_manager.currently_showing_page.select_date()

    @staticmethod
    @allure.step("Navigate to Upcoming Movies Page")
    def navigate_to_upcoming_movies_page():
        log_info("Navigate to Upcoming Movies Page")
        Tasks._page_manager.home_page.navigate()
        Tasks._page_manager.home_page.click_on_upcoming_movies_menu_item()

    @staticmethod
    @allure.step("Select city, cinema and genre")
    def selection_city_cinema_genre(projection):
        log_info(f"Select City - {projection['city']} ")
        Tasks._page_manager.upcoming_movies_page.select_city(projection['city'])
        log_info(f"Select Cinema - {projection['cinema']} ")
        Tasks._page_manager.upcoming_movies_page.select_cinema(projection['cinema'])
        log_info(f"Select Genre - {projection['genre']}")
        Tasks._page_manager.upcoming_movies_page.select_genre(projection['genre'])

    @staticmethod
    @allure.step("Select date range for upcoming movies")
    def select_date_range_upcoming_movies():
        log_info("Select date range for upcoming movies")
        Tasks._page_manager.upcoming_movies_page.click_on_data_range_dropdown()
        log_info("Select random start date and end date for upcoming movies")
        Tasks._page_manager.upcoming_movies_page.select_random_dates_date_range()
        log_info("Click on apply button")
        Tasks._page_manager.upcoming_movies_page.click_on_apply_button()