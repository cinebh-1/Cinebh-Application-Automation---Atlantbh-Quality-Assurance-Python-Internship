import random
from datetime import datetime, timedelta

import requests
import allure
from test_data.common_data import BASE_URL
from utilities.logging import log_info
header_content_type = "application/json"
time_seconds = 1
class APITasks:
    @allure.step("User Login")
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
    def currently_showing_enter_search_term_and_verify_selection(self,projection):
        log_info("Enter search term and verify selection!")
        today= datetime.now()
        random_days = random.randint(1, 9)
        new_date = today + timedelta(days=random_days)
        selected_date = new_date.strftime("%Y-%m-%d")
        log_info(f"Selected date: {selected_date}")
        currently_showing_payload = {"date": selected_date,"search": projection.search_term,"city": projection.city,"genre": projection.genre,"time":projection.time}
        response_currently_showing = requests.post(f"{BASE_URL}/movies/currently", json=currently_showing_payload)
        assert response_currently_showing.status_code == 200
        assert response_currently_showing.reason == ""
        assert response_currently_showing.elapsed.total_seconds() < time_seconds
        assert response_currently_showing.headers["Content-Type"] == header_content_type
        log_info(f"{BASE_URL}/movies/currently/  Status code, time elapsed and header content-type checked successfully!")
        response_currently_showing_body = response_currently_showing.json()
        log_info(f"{BASE_URL}/movies/currently/ response: {response_currently_showing_body}")