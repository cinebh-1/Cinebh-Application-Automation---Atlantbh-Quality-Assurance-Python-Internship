import random
from playwright.sync_api import expect
from utilities.logging import log_info
class CurrentlyShowingPage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.get_by_role("textbox", name="Search Movies")
        self.cities_select = page.get_by_role("combobox").nth(0)
        self.cinemas_select = page.get_by_role("combobox").nth(1)
        self.genres_select = page.get_by_role("combobox").nth(2)
        self.times_select = page.get_by_role("combobox").nth(3)
        self.date_tabs = page.locator(".grid.gap-3.min-w-full button")
    def enter_search_term(self,search_term):
        self.search_box.fill(search_term)
    def select_city(self,city):
        self.cities_select.select_option(city,force=True)
    def select_cinema(self,cinema):
        self.cinemas_select.select_option(cinema,force=True)
    def select_genre(self,genre):
        self.genres_select.select_option(genre,force=True)
    def select_time(self,time):
        self.times_select.select_option(time,force=True)
    def select_date(self):
        count = self.date_tabs.count()
        log_info(f"Found {count} date tabs.")
        if count > 0:
            random_index = random.randint(0, count - 1)
            random_date_tab = self.date_tabs.nth(random_index)
            date_tab_text = random_date_tab.inner_text()
            log_info(f"Selecting and clicking date tab at index {random_index}: '{date_tab_text}'")
            random_date_tab.click()
            expect(random_date_tab).to_have_css("background-color", "rgb(178, 34, 34)")
            log_info(f"Date tab {date_tab_text} clicked.")
        else:
            log_info("No dates found to click.")