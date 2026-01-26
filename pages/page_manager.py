from playwright.sync_api import Page
from pages.currently_showing_page import CurrentlyShowingPage
from pages.home_page import HomePage
from pages.signin_page import SignInPage
from pages.upcoming_movies_page import UpcomingMoviesPage
class PageManager:
    def __init__(self, page: Page):
        self.page = page
        self.home_page = HomePage(page)
        self.signin_page = SignInPage(page)
        self.currently_showing_page = CurrentlyShowingPage(page)
        self.upcoming_movies_page = UpcomingMoviesPage(page)