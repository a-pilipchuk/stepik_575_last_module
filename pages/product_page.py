from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No success message"
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text in success_message.text, "Main product is not in the basket"

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.INFO_MESSAGE), "No info message"
        info_message = self.browser.find_element(*ProductPageLocators.INFO_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text in info_message.text, "Incorrect basket total"

