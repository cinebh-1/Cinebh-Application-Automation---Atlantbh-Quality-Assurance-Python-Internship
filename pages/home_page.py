class HomePage:
    def __init__(self, page):
        self.page = page
        self.sign_in_btn = page.get_by_role("button", name="Sign In")
        self.currently_showing_menu_item = page.get_by_role("link", name="Currently Showing")
        self.upcoming_movies_menu_item= page.get_by_role("link", name="Upcoming Movies")
    def navigate(self):
        self.page.goto("/")
    def click_on_sign_in_btn(self):
        self.sign_in_btn.click()
    def click_on_currently_showing_menu_item(self):
        self.currently_showing_menu_item.click()
    def click_on_upcoming_movies_menu_item(self):
        self.upcoming_movies_menu_item.click()