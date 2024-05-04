from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL_FORM = (By.ID, "login_form")
    REGISTRATION_EMAIL_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (
        By.XPATH, '//*[@id="add_to_basket_form"]/button')
    NAME_OF_PRODUCT = (By.XPATH, '//li[@class ="active"]')
    MESSAGE_WITH_NAME = (By.CSS_SELECTOR, '#messages strong')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, '#content_inner p.price_color')
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, '#messages p>strong')
