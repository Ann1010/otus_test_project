import time
from typing import List

from selenium.webdriver.common.by import By
import allure

from front_tests.pages.base_page import BasePage
from front_tests.helpers import help


class WishListPage(BasePage):
    TAB_BUTTONS = (By.XPATH, "//div[@id='content']//a")
    TAB_IN_GROUP = (By.XPATH, "//div[@class='list-group mb-3']//a")

    def check_wish_list(self, product_name: List):
        for product in product_name:
            with allure.step(f'Проверка отображения {product} в Wish List'):
                assert self.get_element((By.XPATH, f"//div[@id='wishlist']//td[2]/a[contains(text(), '{product}')]")), \
                    f"Продукт {product} не найден на странице"

    def check_delete_product(self, product_name):
        with allure.step(f'Удаление {product_name} из Wish List'):
            time.sleep(2)
            product_name = self.get_element((By.XPATH, f"//div[@id='wishlist']//td[2]/a[contains(text(), '{product_name}')]"))
            product = product_name.find_element(By.XPATH, "ancestor::tr")
            remove_button = product.find_element(By.XPATH, ".//button[2]")
            remove_button.click()
            message = self.get_element((By.XPATH, "//div[contains(text(), 'Success')]"))
            assert message.text == 'Success: You have removed an item from your wishlist', \
                "Не отображается уведомление об удалении продукта из Wish List"