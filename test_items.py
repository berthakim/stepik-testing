"""
тест проверяет, что страница товара на сайте содержит кнопку 
добавления в корзину
"""
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_should_exist(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket"), \
        "Button doesn't exist :("

    # if list will be empty function return [] which is False. Else --> True
