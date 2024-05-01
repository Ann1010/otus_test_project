import datetime

import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class OrdersPage(BasePage):
    MENU_CATALOG = By.XPATH, "//li[@id='menu-catalog']"

    def check_new_order(self, customer: str, total_cost: str) -> None:
        """
        Проверка отображения нового заказа
        :param customer: Заказчик (Имя Фамилия)
        :param total_cost: Сумма заказа
        """
        with allure.step('Проверка отображения нового заказа'):
            current_date = datetime.datetime.now().strftime('%d/%m/%Y')
            new_order_row = self.get_element((By.XPATH, "//div[@class='table-responsive']//tbody//tr[1]"))
            actual_customer = new_order_row.find_element(By.XPATH, ".//td[2]").text
            actual_total_cost = new_order_row.find_element(By.XPATH, ".//td[5]").text
            actual_date = new_order_row.find_element(By.XPATH, ".//td[6]").text
            assert customer == actual_customer, \
                (f"У созданного заказа отличается значение в колонке Customer:\n"
                 f"ОР: {customer}\n"
                 f"ФР: {actual_customer}")
            assert total_cost == actual_total_cost, \
                (f"У созданного заказа отличается значение в колонке Total:\n"
                 f"ОР: {total_cost}\n"
                 f"ФР: {actual_total_cost}")
            assert current_date == actual_date, \
                (f"У созданного заказа отличается значение в колонке Date Added:\n"
                 f"ОР: {current_date}\n"
                 f"ФР: {actual_date}")
