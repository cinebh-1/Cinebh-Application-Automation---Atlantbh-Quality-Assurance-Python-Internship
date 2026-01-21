from playwright.sync_api import expect
class SignUpPage:
    def __init__(self, page):
        self.page = page
        self.sign_up_title = page.get_by_role("heading", name="Sign Up")
        self.email = page.get_by_role("textbox", name="Email Address")
        self.password = page.locator("//input[@placeholder='Password']")
        self.confirm_password = page.get_by_role("textbox", name="Retype Password")
        self.sign_up_button = page.get_by_role("button", name="Sign Up")
        self.vc_code_inputs = page.get_by_role("textbox")
        self.continue_button = page.get_by_text("Continue", exact=True)
        self.success_message = page.get_by_role("heading", name="You’re all set! ")
    def enter_email(self,email):
        self.email.fill(email)
    def enter_password(self,password):
        self.password.fill(password)
    def enter_confirm_password(self,confirm_password):
        self.confirm_password.fill(confirm_password)
    def click_on_sign_up_button(self):
        self.sign_up_button.click()
    def fill_verification_code(self, verification_code):
        for i, digit in enumerate(verification_code):
            self.vc_code_inputs.nth(i).fill(digit)
    def click_on_continue_button(self):
        self.continue_button.click()
    def check_success_message(self):
        expect(self.success_message).to_be_visible()