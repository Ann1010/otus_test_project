import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class CatalogPage(BasePage):
    SUCCESS_MESSAGE = (By.XPATH, f"//div[contains(text(), 'Success: You have added')]")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='btn-close']")

    def add_to_wish_list(self, name: str) -> None:
        """
        Добавление продукта в Wish List.
        :param product_name: Название продукта
        """
        with allure.step(f'Добавление продукта {name} в Wish List'):
            product_name = self.get_element((By.XPATH, f"//h4/a[text()='{name}']"))
            product = product_name.find_element(By.XPATH, "ancestor::div[@class='content']")
            add_wish_list_button = product.find_element(By.XPATH, ".//button[2]")
            add_wish_list_button.click()
            message = self.get_element(self.SUCCESS_MESSAGE)
            assert message.text == f"Success: You have added {name} to your wish list!", \
                (f"Текст сообщения отличается от ожидаемого\n"
                 f"ОР: Success: You have added {name}  to your wish list!\n"
                 f"ФР: {message.text}")
            self.click(self.CLOSE_BUTTON)

    def add_to_cart(self, name: str) -> None:
        """
        Добавление продукта в корзину.
        :param product_name: Название продукта
        """
        with allure.step(f'Добавление продукта {name} в корзину'):
            product_name = self.get_element((By.XPATH, f"//h4/a[text()='{name}']"))
            product = product_name.find_element(By.XPATH, "ancestor::div[@class='content']")
            add_cart_button = product.find_element(By.XPATH, ".//button[1]")
            add_cart_button.click()
            message = self.get_element(self.SUCCESS_MESSAGE)
            # self.assert_text(self.SUCCESS_MESSAGE, f"Success: You have added {product_name} to your shopping cart!")
            assert message.text == f"Success: You have added {name} to your shopping cart!", \
                (f"Текст сообщения отличается от ожидаемого\n"
                 f"ОР: Success: You have added {name} to your shopping cart!\n"
                 f"ФР: {message.text}")
            self.click(self.CLOSE_BUTTON)
