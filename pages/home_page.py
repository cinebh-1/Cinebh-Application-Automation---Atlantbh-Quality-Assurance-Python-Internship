class HomePage:
    def __init__(self, page):
        self.page = page
        self.sign_in_btn = page.get_by_role("button", name="Sign In")
    def navigate(self):
        self.page.goto("/")
    def click_on_sign_in_btn(self):
        self.sign_in_btn.click()
