import random
from datetime import datetime, timedelta, date
import requests
import allure
import os
from dotenv import load_dotenv
from utilities.email_getter import EmailExtractor
from utilities.logging import log_info
header_content_type = "application/json"
time_seconds = 3
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
class APITasks:
    @allure.step("User Login")
    def complete_registration(self, user):
        register_payload = {"email": user["email"], "password": user["password"]}
        app_password = os.getenv("GMAIL_APP_PASSWORD")
        log_info(f"Register payload: {register_payload}")
        response_register = requests.post(f"{BASE_URL}/auth/register", json=register_payload)
        assert response_register.status_code == 200
        assert response_register.reason == ""
        assert response_register.elapsed.total_seconds() < time_seconds
        log_info(f"{BASE_URL}/auth/register: Status code, time elapsed checked successfully!")
        log_info("Fetching verification code from Gmail...")
        verification_code = EmailExtractor.extract_verification_code(user["email"], app_password)
        log_info(f"Extracted code: {verification_code}")
        confirm_payload = {"email": user["email"], "code": verification_code}
        response_verify = requests.post(f"{BASE_URL}/auth/confirm", json=confirm_payload)
        assert response_verify.status_code == 200
        assert response_verify.reason == ""
        assert response_verify.elapsed.total_seconds() < time_seconds
        log_info(f"{BASE_URL}/auth/confirm: Status code, time elapsed checked successfully!")
    @allure.step("User Login")
    def complete_login(self,user):
        login_payload = {"email": user["email"], "password": user["password"]}
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
        assert response_user_id == user["email"]
        log_info(f"{BASE_URL}/auth/me Email: {user['email']}")
        log_info(f"{BASE_URL}/auth/me Request completed successfully!")
    def currently_showing_enter_search_term_and_verify_selection(self,projection):
        log_info("Enter search term and verify selection!")
        today= datetime.now()
        random_days = random.randint(1, 9)
        new_date = today + timedelta(days=random_days)
        selected_date = new_date.strftime("%Y-%m-%d")
        log_info(f"Selected date: {selected_date}")
        currently_showing_payload = {"date": selected_date,"search": projection['search_term'],"city": projection['city'],"genre": projection['genre'],"time":projection['time']}
        response_currently_showing = requests.post(f"{BASE_URL}/movies/currently", json=currently_showing_payload)
        assert response_currently_showing.status_code == 200
        assert response_currently_showing.reason == ""
        assert response_currently_showing.elapsed.total_seconds() < time_seconds
        assert response_currently_showing.headers["Content-Type"] == header_content_type
        log_info(f"{BASE_URL}/movies/currently/  Status code, time elapsed and header content-type checked successfully!")
        response_currently_showing_body = response_currently_showing.json()
        log_info(f"{BASE_URL}/movies/currently/ response: {response_currently_showing_body}")
    def verify_selection_and_date_range(self,projection):
        log_info("Verify Upcoming Movies selection and Date Range")
        year = 2026
        start_day = random.randint(1, 27)
        end_day = random.randint(start_day + 1, 28)
        start_date = date(year, 2, start_day)
        end_date = date(year, 2, end_day)
        log_info(f"Start date: {start_date}, End date: {end_date}")
        upcoming_movies_payload = {"city": projection['city'],"genre": projection['genre'],"time":projection['time'],"startDate": start_date.strftime("%Y-%m-%d"),"endDate": end_date.strftime("%Y-%m-%d")}
        response_upcoming_movies = requests.post(f"{BASE_URL}/movies/upcoming", json=upcoming_movies_payload)
        assert response_upcoming_movies.status_code == 200
        assert response_upcoming_movies.reason == ""
        assert response_upcoming_movies.elapsed.total_seconds() < time_seconds
        assert response_upcoming_movies.headers["Content-Type"] == header_content_type
        log_info(f"{BASE_URL}/movies/upcoming/  Status code, time elapsed and header content-type checked successfully!")
        response_upcoming_movies_body = response_upcoming_movies.json()
        log_info(f"{BASE_URL}/movies/upcoming/ response: {response_upcoming_movies_body}")
        movie_id = response_upcoming_movies_body[0].get("movieId")
        title = response_upcoming_movies_body[0].get("title")
        assert response_upcoming_movies_body[0].get("movieId") == movie_id
        assert response_upcoming_movies_body[0].get("title") == title
        log_info(f"{BASE_URL}/movies/upcoming/ Movie id: {movie_id}, Title: {title}")
    def delete_user(self,user):
        log_info(f"Delete user - {user['email']}")
        delete_user_payload = {"email": user["email"]}
        response_delete = requests.delete(f"{BASE_URL}/auth/test/delete-user", json=delete_user_payload, headers={"X-Test-Secret": os.getenv("TEST_DELETE_USER_SECRET")})
        assert response_delete.status_code == 204
        assert response_delete.elapsed.total_seconds() < time_seconds
        log_info(f"{BASE_URL}/auth/test/delete-user - Deleted user: {user['email']}")