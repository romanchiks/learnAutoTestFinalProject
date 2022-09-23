import pytest
import time
from .pages.product_page import ProductPage

xfail_url_param_num = [7]


@pytest.mark.parametrize('url_param_num', [n if n not in xfail_url_param_num
                                           else pytest.param(n, marks=pytest.mark.xfail)
                                           for n in range(0, 10)])
def test_guest_can_product_to_basket(driver, url_param_num):
    page = ProductPage(
        driver=driver, url=ProductPage.PRODUCT_PAGE_LINK+f'?promo=offer{url_param_num}', implicitly_wait=10)
    page.open()
    page.add_item_to_basket()
