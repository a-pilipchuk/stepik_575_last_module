from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    # добавляем конструктор — метод, который вызывается, когда мы создаем объект.
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    # Внутри конструктора сохраняем эти данные как аттрибуты нашего класса.
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

