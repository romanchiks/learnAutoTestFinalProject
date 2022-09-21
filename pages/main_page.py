from .base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.find_item('#login_link')
        login_link.click()
