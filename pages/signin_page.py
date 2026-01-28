from playwright.sync_api import expect
class SignInPage:
    def __init__(self, page):
        self.page = page
        self.email = page.get_by_role("textbox", name="Email Address")
        self.password = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In").nth(1)
        self.sign_up_link = page.get_by_role("button", name="Sign Up")
        self.username_button = page.get_by_role("button", name="marionizic.ecom")
    def check_sign_in_title(self):
        expect(self.sign_in_title).to_be_visible()
    def enter_email(self,email):
        self.email.fill(email)
    def enter_password(self,password):
        self.password.fill(password)
    def click_on_sign_in_btn(self):
        self.sign_in_button.click()
    def click_on_sign_up_link(self):
        self.sign_up_link.click()
    def check_username_button(self):
        expect(self.username_button).to_be_visible(timeout=10000)