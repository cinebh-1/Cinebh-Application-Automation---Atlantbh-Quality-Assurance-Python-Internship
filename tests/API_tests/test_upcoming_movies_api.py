import pytest
import allure

from tasks.api_tasks import APITasks
from utilities.projection_data import projection

class TestUpcomingMoviesAPI(APITasks):
    @allure.title("Currently Showing Page Cinebh")
    @allure.description("This is a test for Cinebh Apllication, which tests basic features of Upcoming Movies Page")
    @allure.tag("Upcoming Movies Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Mario Nizic")
    @allure.link("http://localhost:5173/")
    @allure.suite("Upcoming Movies Page")
    @allure.feature("Selection, and Date Range Selection")
    @allure.story("Upcoming Movies Features - API")
    @allure.testcase("CAAI")
    @pytest.mark.upcoming_movies_api
    @pytest.mark.order(3)
    def test_upcoming_movies_api(self):

        self.verify_selection_and_date_range(projection)