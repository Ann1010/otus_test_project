import time

import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    CHOOSE_SHIPPING_METHOD_BUTTON = (By.XPATH, "//div[@id='checkout-shipping-method']//button")
    CHOOSE_PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[@id='checkout-payment-method']//button")
    CONTINUE_BUTTON = (By.XPATH, "//div[@class='modal-body']//button[text()='Continue']")
    CONTINUE_PAYMENT_BUTTON = (By.XPATH, "//div[@class='modal-body']//button[@id='button-payment-method']")
    TOTAL_ROW_HEADER = (By.XPATH, "//div[@id='checkout-confirm']//td/strong[text()='Total']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm Order']")

    def choose_shipping_method(self, method: str) -> None:
        """
        Выбор способа перевозки
        :param method: Способ перевозки
        """
        with allure.step(f'Выбор способа перевозки: {method}'):
            self.click(self.CHOOSE_SHIPPING_METHOD_BUTTON)
            self.click((By.XPATH, f"//label[text()='{method}']"))
            self.click(self.CONTINUE_BUTTON)

    def choose_payment_method(self, method: str) -> None:
        """
        Выбор способа перевозки
        :param method: Способ платежа
        """
        with allure.step(f'Выбор способа платежа: {method}'):
            self.click(self.CHOOSE_PAYMENT_METHOD_BUTTON)
            self.click((By.XPATH, f"//label[text()='{method}']"))
            self.click(self.CONTINUE_PAYMENT_BUTTON)

    def check_total_cost(self) -> str:
        """Получение конечной стоимости заказа"""
        with allure.step('Получение конечной стоимости заказа'):
            total = self.get_element(self.TOTAL_ROW_HEADER)
            total_row = total.find_element(By.XPATH, "ancestor::tr")
            return total_row.find_element(By.XPATH, ".//td[2]").text

    def create_order(self, address: str, shipping_method: str, payment_method: str) -> str:
        """
        Создание заказа
        :param address: Адрес заказа
        :param shipping_method: способ доставки
        :param payment_method: способ платежа
        """
        with allure.step('Создание заказа'):
            self.choose_in_select('input-shipping-address', address)
            self.choose_shipping_method(shipping_method)
            self.choose_payment_method(payment_method)
            time.sleep(1)
            total_cost = self.check_total_cost()
            self.click(self.CONFIRM_BUTTON)
            self.wait_title('Your order has been placed!')
            return total_cost
