from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
        assert button, \
            "Find add_product_to_basket_button error"

    def product_name_is_correct(self):
        product_name_in_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        product_name_in_store = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_STORE).text
        is_product_name_correct = product_name_in_basket == product_name_in_store
        assert is_product_name_correct, \
            f"The names of the products in the basket and store are different\n" \
            f"Name in basket -- '{product_name_in_basket}'\n" \
            f"Name in store -- '{product_name_in_store}'"

    def product_price_is_correct(self):
        product_price_in_basket = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        product_price_in_store = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_STORE).text
        is_product_price_correct = product_price_in_basket == product_price_in_store
        assert is_product_price_correct, \
            f"The prices of the products in the basket and store are different\n" \
            f"Price in basket -- '{product_price_in_basket}'\n" \
            f"Price in store -- '{product_price_in_store}'"

    def check_message_about_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"