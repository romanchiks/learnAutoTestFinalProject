import time
from unicodedata import name
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def add_item_to_basket(self, insert_code=False):
        self.find_elem(ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
        if insert_code:
            self.solve_quiz_and_get_code()
        item_name = self.find_elem(ProductPageLocators.ITEM_NAME).text
        name_item_added_to_basket = self.find_elem(
            ProductPageLocators.NAME_ITEM_ADDED_TO_BASKET).text
        items_price_text = self.find_elem(ProductPageLocators.ITEMS_PRICE).text
        items_price = self.get_number_from_text(
            str=items_price_text, type='float')
        price_items_added_to_basket_text = self.find_elem(
            ProductPageLocators.PRICE_ITEMS_ADDED_TO_BASKET).text
        price_items_added_to_basket = self.get_number_from_text(
            str=price_items_added_to_basket_text, type='float')

        assert item_name == name_item_added_to_basket, f'The name of the product added to basket: "{item_name}" ' +\
            f'does not match the name of the product: "{name_item_added_to_basket}"'

        assert items_price == price_items_added_to_basket, 'The price of the products added to the basket: ' +\
            f'{price_items_added_to_basket} does not match the price of the products: {items_price}'

    def should_not_be_success_message(self):
        assert self.is_element_not_present(
            css_selector=ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def success_message_disappears(self):
        assert self.is_disappeared(
            css_selector=ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'
