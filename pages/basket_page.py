from .base_page import BasePage
from .locators import BasketPageLocators
from .useful_consts import empty_basket_dict


class BasketPage(BasePage):
    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def guest_can_see_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Basket is not empty"
        expected_text = empty_basket_dict[self.get_page_language()]
        page_text = self.browser.find_element(
            *BasketPageLocators.EMPTY_BASKET).text
        assert expected_text in page_text, \
            "Expected_text and page_text are different\n" \
            f"expected_text -- {expected_text}\n" \
            f"page_text -- {page_text}"