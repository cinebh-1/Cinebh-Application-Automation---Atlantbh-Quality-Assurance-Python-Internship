import pytest
import allure

from tasks.api_tasks import APITasks
from tasks.ui_tasks import Tasks
from test_data.projection_data import projection
from utilities.user_data import user

@allure.title("Smoke Test UI Cinebh")
@allure.description("This is a smoke test for Cinebh Apllication, which tests basic features like register,login, currently showing and upcoming movies")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Mario Nizic")
@allure.suite("Smoke Test")
@allure.link("http://localhost:5173/")
@allure.feature("Registration,Login, Currently Showing, Upcoming Movies")
@allure.story("Smoke Test - Basic Features - UI")
@allure.testcase("CAAI-93")
@pytest.mark.smoke_ui
@pytest.mark.order(1)
def test_smoke(page_manager):

   Tasks.navigate_to_sign_in_modal(page_manager)

   Tasks.complete_registration(page_manager,user)

   Tasks.complete_login(page_manager,user)

   Tasks.check_logged_in_user(page_manager)

   Tasks.navigate_to_currently_showing_page(page_manager)

   Tasks.search_movie_and_verify_selection(page_manager, projection)

   Tasks.navigate_to_upcoming_movies_page(page_manager)

   Tasks.selection_city_cinema_genre(page_manager, projection)

   Tasks.select_date_range_upcoming_movies(page_manager)

   APITasks.delete_user(APITasks,user)