from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_FROM_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success>.alertinner")

