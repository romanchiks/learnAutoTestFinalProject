import time
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        find_str = 'accounts/login/'
        current_url = self.driver.current_url
        assert current_url.endswith(
            find_str), f'Current url: "{current_url}" does not end with a substring: "{find_str}"'

    def should_be_login_form(self):
        assert self.is_element_present(
            LoginPageLocators.LOGIN_FORM), f'Login form not found (locator: {LoginPageLocators.LOGIN_FORM})'

    def should_be_register_form(self):
        assert self.is_element_present(
            LoginPageLocators.REGISTRATION_FORM), 'Registration form not found (locator: ' \
            f'{LoginPageLocators.REGISTRATION_FORM})'

    def register_new_user(self, email=str(time.time())+'@fk.org', password='PaSsWoRd192837465'):
        self.find_elem(LoginPageLocators.REG_EMAIL_INPUT).send_keys(email)
        self.find_elem(
            LoginPageLocators.REG_PASSWORD_INPUT).send_keys(password)
        self.find_elem(
            LoginPageLocators.REG_PASSWORD_REPEAT_INPUT).send_keys(password)
        self.find_elem(LoginPageLocators.REG_SUBMIT_BUTTON).click()

        assert self.find_elem(
            LoginPageLocators.TEXT_SUCCESS_REGISTRATION), 'No message about successful registration'
