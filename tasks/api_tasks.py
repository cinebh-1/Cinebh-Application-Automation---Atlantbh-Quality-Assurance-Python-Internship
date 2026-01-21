import os
import time
from dotenv import load_dotenv
from utilities.email_getter import EmailExtractor
load_dotenv()
import requests
import allure
from test_data.common_data import BASE_URL
from utilities.logging import log_info
header_content_type = "application/json"
time_seconds = 1
class APITasks:
    @allure.step("User Login")
    def complete_registration(self,user):
        register_payload = {"email": user.email, "password": user.password}
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        log_info(f"Register payload: {register_payload}")
        response_register = requests.post(f"{BASE_URL}/auth/register", json=register_payload)
        assert response_register.status_code == 200
        assert response_register.reason == ""
        assert response_register.elapsed.total_seconds() < time_seconds
        log_info(f"{BASE_URL}/auth/register: Status code, time elapsee checked successfully!")
        log_info("Sleeping 10s for email delivery...")
        time.sleep(10)
        log_info("Fetching verification code from Gmail...")
        verification_code = EmailExtractor.extract_verification_code(user.email, app_password)
        log_info(f"Extracted code: {verification_code}")
        confirm_payload = {"email": user.email, "code": verification_code}
        response_verify = requests.post(f"{BASE_URL}/auth/confirm", json=confirm_payload)
        assert response_verify.status_code == 200
        assert response_verify.reason == ""
        assert response_verify.elapsed.total_seconds() < time_seconds
        log_info(f"{BASE_URL}/auth/confirm: Status code, time elapsed checked successfully!")
    def complete_login(self,user):
        login_payload = {"email": user.email, "password": user.password}
        log_info(f"Login payload: {login_payload}")
        response_login = requests.post(f"{BASE_URL}/auth/login", json=login_payload)
        assert response_login.status_code == 200
        assert response_login.reason == ""
        assert response_login.elapsed.total_seconds() < time_seconds
        assert response_login.headers["Content-Type"] == header_content_type
        log_info(f"{BASE_URL}/auth/login: Status code, time elapsed and header content-type checked successfully!")
        log_info(f" {BASE_URL}/auth/login Response:{response_login.json()}")
        token = response_login.json().get("accessToken")
        log_info(f" {BASE_URL}/auth/login Token:{token}")
        log_info(f"{BASE_URL}/auth/login Request completed successfully!")
        return token
    @allure.step("Check Logged In User")
    def check_logged_in_user(self,user):
        token = self.complete_login(user)
        log_info("Check user is correctly logged in!")
        response_user = requests.get(f"{BASE_URL}/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert response_user.status_code == 200
        assert response_user.reason == ""
        assert response_user.elapsed.total_seconds() < time_seconds
        assert response_user.headers["Content-Type"] == header_content_type
        log_info(f"{BASE_URL}/auth/me: Status code, time elapsed and header content-type checked successfully!")
        response_user_id = response_user.json().get("email")
        assert response_user_id == user.email
        log_info(f"{BASE_URL}/auth/me Email: {user.email}")
        log_info(f"{BASE_URL}/auth/me Request completed successfully!")