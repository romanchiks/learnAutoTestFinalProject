import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, MainPage.MAIN_PAGE_LINK)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link(driver):
    page = MainPage(driver, MainPage.MAIN_PAGE_LINK)
    page.open()
    page.should_be_login_link()


def test_quest_should_be_login_page(driver):
    test_guest_can_go_to_login_page(driver)
    login_page = LoginPage(driver)
    login_page.should_be_login_url()


def test_quest_should_be_login_form(driver):
    page = LoginPage(driver, LoginPage.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_form()


def test_quest_should_be_registration_form(driver):
    page = LoginPage(driver, LoginPage.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_register_form()
