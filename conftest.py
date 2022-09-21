import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: for example ru or en')


@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser_name')
    language_code = request.config.getoption('language')
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language_code})
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language_code)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(
            f'--browser_name should be chrome or firefox and use {browser_name}')
    yield driver
    driver.quit()
