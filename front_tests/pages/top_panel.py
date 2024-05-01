import time

import allure
from selenium.webdriver.common.by import By
import allure

from front_tests.pages.base_page import BasePage
from front_tests.helpers import help


class TopPanel(BasePage):
    CURRENCY_SELECT = (By.XPATH, "//form[@id='form-currency']//span")
    CURRENCY_ITEMS = (By.XPATH, "//form[@id='form-currency']//li/a")
    USER_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    WISH_LIST_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-heart']")
    SHOPPING_CART_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-cart-shopping']")
    MY_ACCOUNT_ITEM = (By.XPATH, "//a[@class='dropdown-item'][contains(text(), 'My Account')]")
    REGISTER_ITEM = (By.XPATH, "//a[@class='dropdown-item'][contains(text(), 'Register')]")
    LOGIN_ITEM = (By.XPATH, "//a[@class='dropdown-item'][contains(text(), 'Login')]")
    MENU_ITEM = (By.XPATH, "//a[@class='dropdown-item']")
    CURRENCY_ICON = (By.XPATH, "//*[@id='form-currency']//a")

    def change_currency(self, currency: str):
        with allure.step(f"Выбор валюты: {currency}"):
            self.click(self.CURRENCY_SELECT)
            currency = self.assert_element((By.XPATH, f"//form[@id='form-currency']//li/a[contains(text(), '{currency}')]"))
            self.click_el(currency)

    def open_register_form(self):
        with allure.step("Открытие формы регистрации аккаунта"):
            self.click(self.USER_BUTTON)
            self.click(self.REGISTER_ITEM)
            self.wait_title('Register Account')

    def open_login_form(self):
        with allure.step("Открытие формы входа в аккаунт"):
            self.click(self.USER_BUTTON)
            self.click(self.LOGIN_ITEM)
            self.wait_title('Account Login')

    def open_my_account_tab(self, tab_name: str):
        with allure.step(f"Переход через меню My account в раздел {tab_name}"):
            self.click(self.USER_BUTTON)
            self.MENU_ITEM = help.locator_with_contains(self.MENU_ITEM, tab_name)
            self.click(self.MENU_ITEM)

    def open_wish_list_page(self):
        with allure.step('Переход в Wish List'):
            self.click(self.WISH_LIST_BUTTON)
            self.wait_title('My Wishlist')

    def open_shopping_cart(self):
        with allure.step('Переход в корзину'):
            self.click(self.SHOPPING_CART_BUTTON)
            self.wait_title('Shopping Cart')

    def logout(self):
        with allure.step('Выход из личного кабинета'):
            self.open_my_account_tab('Logout')
            self.wait_title('Account Logout')







