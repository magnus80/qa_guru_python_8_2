from selene import be, have
from selene.support.shared import browser


def test_get_results(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_get_wrong_results(browser_open):
    string_to_search: str = 'dflgdf;lgkdfl;gkdfl;gk'
    browser.element('[name="q"]').should(be.blank).type(string_to_search).press_enter()
    browser.element('#botstuff').should(have.text("По запросу {0} ничего не найдено".format(string_to_search)))
    print(f"Значение {string_to_search} не найдено")
