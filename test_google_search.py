import pytest
from selene import be, have
from selene.support.shared import browser


@pytest.fixture(scope='session')
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')


def test_get_results(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Результаты поиска'))


def test_get_wrong_results(browser_open):
    search: str = 'dflgdf;lgkdfl;gkdfl;gk'
    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('.card-section>[style^="padding-top"]').should(have.text('Страницы, содержащие все слова запроса, не найдены.'))
    print('Значение {search} не найдено')
