from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, timeout=5000):
        super().__init__(page, timeout)
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.FIELD_IS_REQUIRED_MESSAGE = self.page.get_by_text('This field is required')
        self.FIELD_IS_EMAIL_MESSAGE = self.page.get_by_text('This field is email')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)
        self.LOGIN_FIELD.click(timeout=self.timeout)

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click(timeout=self.timeout)

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile', timeout=self.timeout)

    def check_empty_password(self):
        expect(self.FIELD_IS_REQUIRED_MESSAGE).to_be_visible(timeout=self.timeout)

    def check_invalid_email(self):
        expect(self.FIELD_IS_EMAIL_MESSAGE).to_be_visible(timeout=self.timeout)
