import pytest
import allure

from tasks.api_tasks import APITasks
from utilities.projection_data import projection

class TestCurrentlyShowingApi(APITasks):
    @allure.title("Currently Showing Page")
    @allure.title("Currently Showing Page Cinebh")
    @allure.description("This is a test for Cinebh Apllication, which tests basic features of Currently Showing Page")
    @allure.tag("Currently Showing Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Mario Nizic")
    @allure.link("http://localhost:5173/")
    @allure.suite("Currently Showing Page")
    @allure.feature("Search Movie, Selection, and Date Selection")
    @allure.story("Currently Showing Features - API")
    @allure.testcase("CAAI")
    @pytest.mark.currently_showing_api
    @pytest.mark.order(2)
    def test_currently_showing_api(self):

        self.currently_showing_enter_search_term_and_verify_selection(projection)