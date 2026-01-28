import pytest
import allure

from tasks.api_tasks import APITasks
from test_data.projection_data import projection
from utilities.user_data import user
class TestSmokeApi(APITasks):
    @allure.title("Smoke Test API Cinebh")
    @allure.description("This is a smoke test for Cinebh Apllication, which tests basic features like registration, login, currently showing and upcoming movies")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label("owner", "Mario Nizic")
    @allure.suite("Smoke Test")
    @allure.link("http://localhost:5173/")
    @allure.feature("Registration, Login, Currently Showing, Upcoming API")
    @allure.story("Smoke Test - Features - API")
    @allure.testcase("CAAI-94")
    @pytest.mark.smoke_api
    @pytest.mark.order(1)

    def test_smoke_api(self):

        self.complete_registration(user)

        self.complete_login(user)

        self.check_logged_in_user(user)

        self.currently_showing_enter_search_term_and_verify_selection(projection)

        self.verify_selection_and_date_range(projection)