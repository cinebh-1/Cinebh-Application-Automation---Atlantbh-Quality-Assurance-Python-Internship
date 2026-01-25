import pytest
import allure
from tasks.ui_tasks import Tasks
from utilities.projection_data import projection

@allure.title("Currently Showing Page Cinebh")
@allure.description("This is a test for Cinebh Apllication, which tests basic features of Currently Showing Page")
@allure.tag("Currently Showing Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("http://localhost:5173/")
@allure.suite("Currently Showing Page")
@allure.feature("Search Movie, Selection, and Date Selection")
@allure.story("Currently Showing Features - UI")
@allure.testcase("CAAI")
@pytest.mark.currently_showing_ui
@pytest.mark.order(3)
def test_currently_showing(page_manager):

    Tasks.navigate_to_currently_showing_page(page_manager)

    Tasks.search_movie_and_verify_selection(page_manager,projection)

    Tasks.select_random_date(page_manager)