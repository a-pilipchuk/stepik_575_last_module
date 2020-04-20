from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#lgin_link")
    VIEW_BASKET_BUTTON = (By.XPATH, "//a[@class = 'btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id = 'content_inner']/p")
    BASKET_TITLE = (By.XPATH, "//div[contains(@class, 'basket-title')]//h2")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.ID, "id_registration-email")
    REG_PASSWORD = (By.ID, "id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_FROM_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success>.alertinner")

