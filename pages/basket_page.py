from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def should_be_no_items_in_guest_cart(self):
        self.go_to_basket_page()
        assert self.should_be_login_link(), 'The current user is not a guest'
        assert self.is_element_not_present(
            BasePageLocators.BASKET_ITEMS), 'Guest user has products on first login'
        assert self.is_element_present(
            BasePageLocators.TEXT_BASKET_IS_EMPTY), 'There is no text that the cart is empty'
