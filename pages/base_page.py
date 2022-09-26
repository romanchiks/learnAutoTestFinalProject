import re
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException

from .locators import BasePageLocators


class BasePage():

    def __init__(self, driver, url='', implicitly_wait=1):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(implicitly_wait)

    def find_elem(self, selector, search_method=By.CSS_SELECTOR):
        return self.driver.find_element(search_method, selector)

    def find_elems(self, selector, search_method=By.CSS_SELECTOR):
        return self.driver.find_elements(search_method, selector)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, css_selector):
        try:
            self.find_elem(css_selector)
        except NoSuchElementException:
            return False
        return True

    def is_element_not_present(self, css_selector, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, css_selector, timeout=2):
        try:
            WebDriverWait(self.driver, timeout, ignored_exceptions=TimeoutException).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
        except TimeoutException:
            return False
        return True

    def get_number_from_text(self, str, type='int'):
        if type == 'int':
            return [int(s) for s in re.findall(r'-?\d+\.?\d*', str)][0]
        elif type == 'float':
            return [float(s) for s in re.findall(r'-?\d+\.?\d*', str)][0]
        else:
            raise pytest.UsageError(
                f'Invalid number type specified: "{type}". Available: "int", "float"')

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(
            BasePageLocators.LOGIN_LINK), "Login link is not presented"
        return True

    def go_to_login_page(self):
        self.find_elem(BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        self.find_elem(BasePageLocators.BASKET_LINK).click()

    def should_be_no_items_in_guest_cart(self):
        self.go_to_basket_page()
        assert self.should_be_login_link(), 'The current user is not a guest'
        assert self.is_element_not_present(
            BasePageLocators.BASKET_ITEMS), 'Guest user has products on first login'
        assert self.is_element_present(
            BasePageLocators.TEXT_BASKET_IS_EMPTY), 'There is no text that the cart is empty'
