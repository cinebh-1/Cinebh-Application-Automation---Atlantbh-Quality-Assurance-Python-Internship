import pytest
import allure

from tasks.api_tasks import APITasks
from utilities.user_data import user
class TestSmokeApi(APITasks):
    @allure.title("Smoke Test API Cinebh")
    @allure.description("This is a smoke test for Cinebh Apllication, which tests basic features login")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label("owner", "Mario Nizic")
    @allure.link("http://localhost:5173/")
    @allure.suite("Authentication")
    @allure.feature("Login")
    @allure.story("Smoke Test - Login - API")
    @allure.testcase("CAAI-94")
    @pytest.mark.smoke_api
    @pytest.mark.order(1)

    def test_smoke_login_api(self):

        self.complete_login(user)

        self.check_logged_in_user(user)