"""
тест проверяет, что страница товара на сайте содержит кнопку 
добавления в корзину.
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/
"""
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_exist(browser):
    browser.get(link)

    time.sleep(5)

    button_is_here = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")

    assert len(button_is_here) > 0, "Button doesn't exist :("
