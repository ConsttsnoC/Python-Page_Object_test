from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    # Добавляем товар в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    add_to_basket_button.click()
    # Проверяем, что нет сообщения об успехе
    assert WebDriverWait(browser, 4).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    # Проверяем, что нет сообщения об успехе
    assert WebDriverWait(browser, 4).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))), \
        "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    # Добавляем товар в корзину
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    add_to_basket_button.click()
    # Проверяем, что сообщение об успехе исчезает
    assert WebDriverWait(browser, 4, 0.1).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))), \
        "Success message did not disappear"