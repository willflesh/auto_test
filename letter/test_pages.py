from .first_page import BasePage
from .locators import TestPageLocators


class CheckPages(BasePage):
    def go_to_checkbox(self):
        link = self.browser.find_element(*TestPageLocators.LOGIN_LINK)
        link.click()
        assert self.is_element_present(*TestPageLocators.LOGIN_LINK)
