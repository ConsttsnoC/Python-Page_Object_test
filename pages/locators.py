from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")


class MainPageLocators(BasePageLocators):
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (
        By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME_IN_STORE = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info p strong")
    PRODUCT_PRICE_IN_STORE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner")