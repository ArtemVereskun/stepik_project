from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def name_of_the_product_are_correct_in_the_alert(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        msg_with_name = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_NAME).text
        assert name_of_product == msg_with_name,"в корзині не той товар що додавали"

    def price_of_the_product_are_correct_in_the_alert(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE).text
        assert price_of_product == price_in_msg, "ціна товару в алерті не = ціні на сторінці продукту"
