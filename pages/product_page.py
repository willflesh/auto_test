from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_product_name_in_message(self):
        product_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        message_name = self.browser.find_element(*BasketPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_name

    def should_be_correct_basket_price(self):
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_price

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(BasketPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should be"
