import time
from typing import List

import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class WishListPage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Success')]")

    def check_wish_list(self, product_name: List) -> None:
        """
        Проверка отображения продуктов в Wish List
        :param product_name: названия продуктов
        """
        for product in product_name:
            with allure.step(f'Проверка отображения {product} в Wish List'):
                assert self.get_element((By.XPATH, f"//div[@id='wishlist']//td[2]/a[contains(text(), '{product}')]")), \
                    f"Продукт {product} не найден на странице"

    def check_delete_product(self, product_name: str) -> None:
        """
        Удаление продукта из Wish List
        :param product_name: Название продукта
        """
        with allure.step(f'Удаление {product_name} из Wish List'):
            time.sleep(2)
            product_name = self.get_element((By.XPATH,
                                             f"//div[@id='wishlist']//td[2]/a[contains(text(), '{product_name}')]"))
            product = product_name.find_element(By.XPATH, "ancestor::tr")
            remove_button = product.find_element(By.XPATH, ".//button[2]")
            remove_button.click()
            message = self.get_element(self.SUCCESS_MESSAGE)
            assert message.text == 'Success: You have removed an item from your wishlist', \
                "Не отображается уведомление об удалении продукта из Wish List"
