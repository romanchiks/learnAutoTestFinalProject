class BasePageLocators():
    LOGIN_LINK = '#login_link'
    BASKET_LINK = '.basket-mini a.btn'
    BASKET_ITEMS = 'basket-items'
    TEXT_BASKET_IS_EMPTY = '#content_inner p:nth-child(1) a'


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = '#login_form'
    REGISTRATION_FORM = '#register_form'


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = 'button.btn-add-to-basket'
    ITEM_NAME = '.product_main h1'
    ITEMS_PRICE = 'div.basket-mini'
    NAME_ITEM_ADDED_TO_BASKET = '#messages div:first-child strong '
    PRICE_ITEMS_ADDED_TO_BASKET = '.alertinner > p > strong'
    SUCCESS_MESSAGE = '#messages div'
