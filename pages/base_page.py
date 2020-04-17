from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # добавляем конструктор — метод, который вызывается, когда мы создаем объект.
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

