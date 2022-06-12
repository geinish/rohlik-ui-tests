from selenium.common.exceptions import NoSuchElementException

from .locators import BasePageLocators


class BasePage():
    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def get_current_url(self):
        return self.browser.current_url

    def get_value(self, how, what):
        value = self.browser.find_element(how, what).text
        return value

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_BUTTON)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), "Basket button is not presented"
