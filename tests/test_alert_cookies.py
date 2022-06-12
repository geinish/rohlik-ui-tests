import pytest

from pages.base_page import BasePage
from pages.locators import CommonConstant


@pytest.mark.regression
@pytest.mark.smoke
class TestAlertCookies():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, CommonConstant.LINK)
        page.open()
