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
    @allure.step("Navigate to Currently Showing Page")
    def navigate_to_currently_showing_page(page_manager):
        log_info("Navigate to Currently Showing Page")
        page_manager.home_page.navigate()
        page_manager.home_page.click_on_currently_showing_menu_item()
    @allure.step("Search movie, select city,cinema, genre and time")
    def search_movie_and_verify_selection(page_manager,projection):
        log_info(f"Search Movie - {projection.search_term}")
        page_manager.currently_showing_page.enter_search_term(projection.search_term)
        log_info(f"Select City - {projection.city} ")
        page_manager.currently_showing_page.select_city(projection.city)
        log_info(f"Select Cinema - {projection.cinema} ")
        page_manager.currently_showing_page.select_cinema(projection.cinema)
        log_info(f"Select Genre - {projection.genre} ")
        page_manager.currently_showing_page.select_genre(projection.genre)
        log_info(f"Select Time - {projection.time} ")
        page_manager.currently_showing_page.select_time(projection.time)
    @allure.step("Select random date from date tabs on Currently Showing Page")
    def select_random_date(page_manager):
        log_info("Select Random Date - date tabs - currently showing page")
        page_manager.currently_showing_page.select_date()
    @allure.step("Navigate to Upcoming Movies Page")
    def navigate_to_upcoming_movies_page(page_manager):
        log_info("Navigate to Upcoming Movies Page")
        page_manager.home_page.navigate()
        page_manager.home_page.click_on_upcoming_movies_menu_item()
    @allure.step("Select city, cinema and genre")
    def selection_city_cinema_genre(page_manager,projection):
        log_info(f"Select City - {projection.city} ")
        page_manager.upcoming_movies_page.select_city(projection.city)
        log_info(f"Select Cinema - {projection.cinema} ")
        page_manager.upcoming_movies_page.select_cinema(projection.cinema)
        log_info(f"Select Genre - {projection.genre} ")
        page_manager.upcoming_movies_page.select_genre(projection.genre)
    @allure.step("Select date range for upcoming movies")
    def select_date_range_upcoming_movies(page_manager):
        log_info("Select date range for upcoming movies")
        page_manager.upcoming_movies_page.click_on_data_range_dropdown()
        log_info("Click on next month button on Date Range datepicker")
        page_manager.upcoming_movies_page.click_on_next_month_button()
        log_info("Select random start date and end date for upcoming movies")
        page_manager.upcoming_movies_page.select_random_dates_date_range()
        log_info("Click on apply buttom")
        page_manager.upcoming_movies_page.click_on_apply_button()
        log_info("Check if movie is displayed after applying date range dates")
        page_manager.upcoming_movies_page.check_movie_displayed()
