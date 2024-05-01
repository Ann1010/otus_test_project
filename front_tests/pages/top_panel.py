import allure
from selenium.webdriver.common.by import By

from front_tests.helpers import help
from front_tests.pages.base_page import BasePage


class TopPanel(BasePage):
    USER_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-user']")
    WISH_LIST_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-heart']")
    SHOPPING_CART_BUTTON = (By.XPATH, "//i[@class='fa-solid fa-cart-shopping']")
    REGISTER_ITEM = (By.XPATH, "//a[@class='dropdown-item'][contains(text(), 'Register')]")
    LOGIN_ITEM = (By.XPATH, "//a[@class='dropdown-item'][contains(text(), 'Login')]")
    MENU_ITEM = (By.XPATH, "//a[@class='dropdown-item']")

    def open_login_form(self) -> None:
        """Открытие формы входа в аккаунт"""
        with allure.step("Открытие формы входа в аккаунт"):
            self.click(self.USER_BUTTON)
            self.click(self.LOGIN_ITEM)
            self.wait_title('Account Login')

    def open_my_account_tab(self, tab_name: str) -> None:
        """
        Переход через меню My account в раздел
        :param tab_name: Название раздела
        """
        with allure.step(f"Переход через меню My account в раздел {tab_name}"):
            self.click(self.USER_BUTTON)
            self.MENU_ITEM = help.locator_with_contains(self.MENU_ITEM, tab_name)
            self.click(self.MENU_ITEM)

    def open_wish_list_page(self) -> None:
        """Переход в Wish List"""
        with allure.step('Переход в Wish List'):
            self.click(self.WISH_LIST_BUTTON)
            self.wait_title('My Wishlist')

    def open_shopping_cart(self) -> None:
        """Переход в корзину"""
        with allure.step('Переход в корзину'):
            self.click(self.SHOPPING_CART_BUTTON)
            self.wait_title('Shopping Cart')

    def logout(self) -> None:
        """Выход из личного кабинета"""
        with allure.step('Выход из личного кабинета'):
            self.open_my_account_tab('Logout')
            self.wait_title('Account Logout')
