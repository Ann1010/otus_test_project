import time

import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class CheckoutPage(BasePage):
    LEFT_MENU = (By.ID, "column-left")
    COMPARE_BUTTON = (By.ID, "compare-total")
    INPUT_SORT = (By.ID, "input-sort")
    INPUT_LIMIT = (By.ID, "input-limit")
    LIMITS = (By.XPATH, "//*[@id='input-limit']/option")
    PRODUCT_PRICE = (By.XPATH, "//div[@id='product-info']//span[@class='price-tax']")

    def choose_shipping_method(self, method):
        with allure.step(f'Выбор способа перевозки: {method}'):
            self.click((By.XPATH, "//div[@id='checkout-shipping-method']//button"))
            self.click((By.XPATH, f"//label[text()='{method}']"))
            self.click((By.XPATH, "//div[@class='modal-body']//button[text()='Continue']"))

    def choose_payment_method(self, method):
        with allure.step(f'Выбор способа перевозки: {method}'):
            self.click((By.XPATH, "//div[@id='checkout-payment-method']//button"))
            self.click((By.XPATH, f"//label[text()='{method}']"))
            self.click((By.XPATH, "//form[@id='form-payment-method']//button[text()='Continue']"))

    def check_total_cost(self) -> str:
        with allure.step('Получение конечной стоимости заказа'):
            total = self.get_element((By.XPATH, "//div[@id='checkout-confirm']//td/strong[text()='Total']"))
            total_row = total.find_element(By.XPATH, "ancestor::tr")
            return total_row.find_element(By.XPATH, ".//td[2]").text

    def create_order(self, address, shipping_method, payment_method, **kwargs):
        with allure.step('Создание заказа'):
            self.choose_in_select('input-shipping-address', address)
            self.choose_shipping_method(shipping_method)
            self.choose_payment_method(payment_method)
            time.sleep(1)
            total_cost = self.check_total_cost()
            self.click((By.XPATH, "//button[text()='Confirm Order']"))
            self.wait_title('Your order has been placed!')
            return total_cost


