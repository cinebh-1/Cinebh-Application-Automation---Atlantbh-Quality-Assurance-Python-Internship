from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signin_page import SignInPage
from pages.signup_page import SignUpPage
class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.home_page = HomePage(page)
        self.signup_page = SignUpPage(page)
        self.signin_page = SignInPage(page)