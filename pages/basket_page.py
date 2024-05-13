from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_that_present_text_the_basket_is_empty(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Ваш кошик пустий" in empty_basket_text,"кошик не пустий"
       # assert empty_basket_text == "Ваш кошик пустий.", "кошик не пустий"

    def check_that_the_basket_is_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_TOTALS),\
            "Корзина не пуста"


