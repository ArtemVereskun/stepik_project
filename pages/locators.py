from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span [class = "btn btn-default"]')



class MainPageLocators():
   pass


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner  p')
    BASKET_TOTALS = (By.ID, 'basket_totals')
