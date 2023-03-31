from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/"

class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME = (By.CSS_SELECTOR, '.product_main h1')
    ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')


