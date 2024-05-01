import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class CatalogPage(BasePage):
    LEFT_MENU = (By.ID, "column-left")
    COMPARE_BUTTON = (By.ID, "compare-total")
    INPUT_SORT = (By.ID, "input-sort")
    INPUT_LIMIT = (By.ID, "input-limit")
    LIMITS = (By.XPATH, "//*[@id='input-limit']/option")
    PRODUCT_PRICE = (By.XPATH, "//div[@id='product-info']//span[@class='price-tax']")

    def add_to_wish_list(self, name):
        with allure.step(f'Добавление продукта {name} в Wish List'):
            product_name = self.get_element((By.XPATH, f"//h4/a[text()='{name}']"))
            product = product_name.find_element(By.XPATH, "ancestor::div[@class='content']")
            add_wish_list_button = product.find_element(By.XPATH, ".//button[2]")
            add_wish_list_button.click()
            message = self.get_element((By.XPATH, f"//div[contains(text(), 'Success: You have added')]"))
            assert message.text == f"Success: You have added {name} to your wish list!"
            self.click((By.XPATH, "//button[@class='btn-close']"))

    def add_to_cart(self, name):
        with allure.step(f'Добавление продукта {name} в корзину'):
            product_name = self.get_element((By.XPATH, f"//h4/a[text()='{name}']"))
            product = product_name.find_element(By.XPATH, "ancestor::div[@class='content']")
            add_cart_button = product.find_element(By.XPATH, ".//button[1]")
            add_cart_button.click()
            message = self.get_element((By.XPATH, f"//div[contains(text(), 'Success: You have added')]"))
            assert message.text == f"Success: You have added {name} to your shopping cart!"
            self.click((By.XPATH, "//button[@class='btn-close']"))


