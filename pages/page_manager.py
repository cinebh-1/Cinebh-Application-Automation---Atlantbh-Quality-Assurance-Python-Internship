from playwright.sync_api import Page
from pages.currently_showing_page import CurrentlyShowingPage
from pages.home_page import HomePage
from pages.signin_page import SignInPage
class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.home_page = HomePage(page)
        self.signin_page = SignInPage(page)
        self.currently_showing_page = CurrentlyShowingPage(page)