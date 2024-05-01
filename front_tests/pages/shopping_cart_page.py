import time
from typing import List

from selenium.webdriver.common.by import By
import allure

from front_tests.pages.base_page import BasePage
from front_tests.helpers import help


class ShoppingCartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='Checkout']")

    def go_to_checkout(self):
        with allure.step('Проверка к оформлению заказа'):
            self.click(self.CHECKOUT_BUTTON)
            self.wait_title('Checkout')