from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_not_be_products_added()
        self.should_be_empty_basket_text()

    def should_be_basket_url(self):
        current_url = self.browser.current_url
        assert "/basket" in str(current_url), "not basket URL"

    def should_not_be_products_added(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "Basket contains some products"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text not found"
