import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='Checkout']")

    def go_to_checkout(self) -> None:
        """Переход к оформлению заказа"""
        with allure.step('Переход к оформлению заказа'):
            self.click(self.CHECKOUT_BUTTON)
            self.wait_title('Checkout')
