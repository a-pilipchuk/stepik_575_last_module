import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url:
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()  # переключаемся на алерт и решаем задачу
    #time.sleep(2)
    # проверяем ожидаемый результат
    page.should_be_success_message()
    page.should_be_basket_total()
