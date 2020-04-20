from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "No info message"
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text in basket_total.text, f"Product price {product_price.text} does not match " \
                                                        f"basket total {basket_total.text} "

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.NAME_FROM_SUCCESS_MESSAGE), "No success message"
        success_message = self.browser.find_element(*ProductPageLocators.NAME_FROM_SUCCESS_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == success_message.text, f"Should be bought {product_name.text}, " \
                                                          f"product name in success message is {success_message.text}"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappeared during 4 seconds"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


