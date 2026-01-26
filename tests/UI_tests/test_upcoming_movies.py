import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.projection_data import projection

@allure.title("Currently Showing Page Cinebh")
@allure.description("This is a test for Cinebh Apllication, which tests basic features of Upcoming Movies Page")
@allure.tag("Upcoming Movies Page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Mario Nizic")
@allure.link("http://localhost:5173/")
@allure.suite("Upcoming Movies Page")
@allure.feature("Selection, and Date Range Selection")
@allure.story("Upcoming Movies Features - UI")
@allure.testcase("CAAI")
@pytest.mark.upcoming_movies_ui
@pytest.mark.order(3)
def test_upcoming_movies(page_manager):

    Tasks.navigate_to_upcoming_movies_page(page_manager)

    Tasks.selection_city_cinema_genre(page_manager,projection)

    Tasks.select_date_range_upcoming_movies(page_manager)