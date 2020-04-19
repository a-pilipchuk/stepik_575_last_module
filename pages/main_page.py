from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators
from .login_page import LoginPage


# теперь здесь будет заглушка, т.к. метод перехода поссылке логина перенесён в BasePage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
#        return LoginPage(browser=self.browser, url=self.browser.current_url)

