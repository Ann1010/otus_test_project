from selenium.webdriver.common.by import By
import allure

from front_tests.pages.base_page import BasePage


class NavigationPanel(BasePage):
    MENU_CATALOG = By.XPATH, "//li[@id='menu-catalog']"

    def expand_menu(self, menu: str):
        with allure.step(f"Раскрытие списка подразделов для {menu}"):
            self.logger.info("Expand tab in menu")
            self.click((By.XPATH, f"//li[@id='menu-{menu}']"))

    def go_to_tab(self, menu, tab):
        with allure.step(f"Переход на вкладку {tab} раздела {menu}"):
            self.logger.info("Click tab in menu")
            self.expand_menu(menu)
            self.click((By.XPATH, f"//a[contains(@href, '{menu}/{tab}')]"))

    def go_to_top_tab(self, tab_name):
        with allure.step(f"Переход в раздел {tab_name} из верхней панели"):
            self.click((By.XPATH, f"//div[@id='narbar-menu']//a[text()='{tab_name}']"))
            self.wait_title(tab_name)
            self.assert_elements((By.XPATH, "//div[@class='product-thumb']"))
