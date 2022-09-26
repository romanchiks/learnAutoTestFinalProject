import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

xfail_url_param_num = [7]


@pytest.mark.reg
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        page = LoginPage(
            driver=driver, url=LoginPage.LOGIN_PAGE_LINK, implicitly_wait=5)
        page.open()
        page.register_new_user(email=str(time.time())+'qw@fk.org')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(
            driver=driver, url=ProductPage.PRODUCT_PAGE_LINK, implicitly_wait=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(
            driver=driver, url=ProductPage.PRODUCT_PAGE_LINK, )
        page.open()
        page.add_item_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('url_param_num', [n if n not in xfail_url_param_num
                                           else pytest.param(n, marks=pytest.mark.xfail)
                                           for n in range(0, 10)])
def test_guest_can_add_product_to_basket(driver, url_param_num):
    page = ProductPage(
        driver=driver, url=ProductPage.PRODUCT_PAGE_LINK+f'?promo=offer{url_param_num}', implicitly_wait=10)
    page.open()
    page.add_item_to_basket(insert_code=True)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(
        driver=driver, url=ProductPage.PRODUCT_PAGE_LINK, implicitly_wait=0)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    page = ProductPage(
        driver=driver, url=ProductPage.PRODUCT_PAGE_LINK, implicitly_wait=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(
        driver=driver, url=ProductPage.PRODUCT_PAGE_LINK, implicitly_wait=1)
    page.open()
    page.add_item_to_basket()
    page.success_message_disappears()


def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, ProductPage.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, ProductPage.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = ProductPage(driver, ProductPage.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_no_items_in_guest_cart()
