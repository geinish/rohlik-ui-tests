from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#headerLogin")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".cartHeader")


class ConcernCookiesLocators():
    ALLOW_BUTTON = (By.CSS_SELECTOR, "#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    DECLINE_BUTTON = (By.CSS_SELECTOR, "#CybotCookiebotDialogBodyButtonDecline")
    CUSTOMIZE_BUTTON = (By.CSS_SELECTOR, '#CybotCookiebotDialogBodyLevelButtonCustomize')
    MORE_BUTTON = (By.CSS_SELECTOR, '#CybotCookiebotDialogBodyEdgeMoreDetailsLink')


class CommonConstant():
    LINK = ("https://www.rohlik.cz/")
    PROFIL_LINK = ("https://www.rohlik.cz/uzivatel/profil")
    BASKET_LINK = ("https://www.rohlik.cz/objednavka/prehled-kosiku")
