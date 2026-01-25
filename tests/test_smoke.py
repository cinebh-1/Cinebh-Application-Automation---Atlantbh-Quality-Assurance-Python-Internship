import pytest
import allure

from tasks.ui_tasks import Tasks
from utilities.user_data import user

@allure.title("Smoke Test UI Cinebh")
@allure.description("This is a smoke test for Cinebh Apllication, which tests basic features like register and login")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.BLOCKER)
@allure.label("owner", "Mario Nizic")
@allure.link("http://localhost:5173/")
@allure.suite("Authentication")
@allure.feature("Registration and Login")
@allure.story("Smoke Test - Registration and Login - UI")
@allure.testcase("CAAI-93")
@pytest.mark.smoke
@pytest.mark.order(1)
def test_smoke_login(page_manager):

   Tasks.navigate_to_sign_in_modal(page_manager)

   Tasks.complete_registration(page_manager,user)

   Tasks.complete_login(page_manager,user)

   Tasks.check_logged_in_user(page_manager,user)