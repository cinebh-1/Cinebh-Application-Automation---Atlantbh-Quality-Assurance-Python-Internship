import random
from playwright.sync_api import expect
class UpcomingMoviesPage:
    def __init__(self, page):
        self.page = page
        self.cities_select = page.get_by_role("combobox").nth(0)
        self.cinemas_select = page.get_by_role("combobox").nth(1)
        self.genres_select = page.get_by_role("combobox").nth(2)
        self.date_range_dropdown = page.get_by_role("button", name="Date Range")
        self.next_month_button = page.get_by_role("button", name="Go to the Next Month")
        self.apply_button = page.get_by_role("button", name="Apply")
    def select_city(self,city):
        self.cities_select.select_option(city,force=True)
    def select_cinema(self,cinema):
        self.cinemas_select.select_option(cinema,force=True)
    def select_genre(self,genre):
        self.genres_select.select_option(genre,force=True)
    def click_on_data_range_dropdown(self):
        self.date_range_dropdown.click()
    def click_on_next_month_button(self):
        self.next_month_button.click()
    def select_random_dates_date_range(self):
        random_days = sorted(random.sample(range(1, 29), 2))
        start_date = self.page.get_by_text(str(random_days[0]),exact=True)
        end_date = self.page.get_by_text(str(random_days[1]),exact=True)
        start_date.click()
        end_date.click()
    def click_on_apply_button(self):
        self.apply_button.click()