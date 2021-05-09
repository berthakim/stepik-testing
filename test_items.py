"""
тест проверяет, что страница товара на сайте содержит кнопку 
добавления в корзину
"""
import time
from selenium.common.exceptions import NoSuchElementException



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_should_exist(browser):
    browser.get(link)
    # time.sleep(30)  # comment out for take more time to see the page
    buttons = len(browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket"))
    assert buttons == 1, "Button doesn't exist or There is two or more identical buttons :("
