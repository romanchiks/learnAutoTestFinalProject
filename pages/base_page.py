from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_item(self, css_selector):
        return self.driver.find_element(By.CSS_SELECTOR, f'{css_selector}')
