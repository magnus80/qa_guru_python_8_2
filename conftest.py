import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')
    yield
    browser.quit()
