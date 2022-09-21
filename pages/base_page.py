from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, driver, url, implicitly_wait=1):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(implicitly_wait)

    def find_elem(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, f'{css_selector}')

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, css_selector):
        try:
            self.find_elem(css_selector)
        except NoSuchElementException:
            return False
        return True
