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
            LoginPageLocators.REGISTRATION_FORM), f'Registration form not found (locator: {LoginPageLocators.REGISTRATION_FORM})'
