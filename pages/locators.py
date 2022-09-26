class BasePageLocators():
    LOGIN_LINK = '#login_link'
    BASKET_LINK = '.basket-mini a.btn'
    BASKET_ITEMS = 'basket-items'
    TEXT_BASKET_IS_EMPTY = '#content_inner p:nth-child(1) a'
    USER_ICON = '.icon-user'


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = '#login_form'
    REGISTRATION_FORM = '#register_form'
    REG_EMAIL_INPUT = '#register_form input[type="email"]'
    REG_PASSWORD_INPUT = '#id_registration-password1'
    REG_PASSWORD_REPEAT_INPUT = '#id_registration-password2'
    REG_SUBMIT_BUTTON = 'button[name="registration_submit"]'
    TEXT_SUCCESS_REGISTRATION = '#messages .alert-success'


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = 'button.btn-add-to-basket'
    ITEM_NAME = '.product_main h1'
    ITEMS_PRICE = 'div.basket-mini'
    NAME_ITEM_ADDED_TO_BASKET = '#messages div:first-child strong '
    PRICE_ITEMS_ADDED_TO_BASKET = '.alertinner > p > strong'
    SUCCESS_MESSAGE = '#messages div'
