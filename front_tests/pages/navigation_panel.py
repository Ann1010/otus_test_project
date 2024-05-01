import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class NavigationPanel(BasePage):
    MENU_CATALOG = By.XPATH, "//li[@id='menu-catalog']"

    def go_to_top_tab(self, tab_name: str) -> None:
        """
        Переход в раздел из верхней панели управления
        :param tab_name: Название раздела
        """
        with allure.step(f"Переход в раздел {tab_name} из верхней панели"):
            self.click((By.XPATH, f"//div[@id='narbar-menu']//a[text()='{tab_name}']"))
            self.wait_title(tab_name)
            self.get_elements((By.XPATH, "//div[@class='product-thumb']"))
