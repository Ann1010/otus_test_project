import allure
from selenium.webdriver.common.by import By

from front_tests.helpers import help
from front_tests.pages.base_page import BasePage


class MyAccountPage(BasePage):
    TAB_BUTTONS = (By.XPATH, "//div[@id='content']//a")
    TAB_IN_GROUP = (By.XPATH, "//div[@class='list-group mb-3']//a")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    ERROR_FIRSTNAME_MESSAGE = (By.XPATH, "//div[@id='error-firstname']")
    ERROR_LASTNAME_MESSAGE = (By.XPATH, "//div[@id='error-lastname']")
    ERROR_EMAIL_MESSAGE = (By.XPATH, "//div[@id='error-email']")

    def go_to_tab(self, tab_name: str, title: str = '') -> None:
        """
        Переход в раздел со страницы My Account
        :param tab_name: Название раздела
        :param title: Название открываемого раздела, если отличается от названия вкладки
        """
        with allure.step(f'Переход в раздел {tab_name}'):
            self.click(help.locator_with_contains(self.TAB_IN_GROUP, tab_name))
            if title != '':
                self.wait_title(title)
            else:
                self.wait_title(tab_name)

    def check_my_account_tabs(self) -> None:
        """Проверка разделов на странице My account"""
        with allure.step('Проверка разделов My account'):
            tabs = ['Edit your account information', 'Change your password', 'Modify your address book entries',
                    'Modify your wish list']
            for tab in tabs:
                self.assert_element(help.locator_with_contains(self.TAB_BUTTONS, tab))

    def click_back_button(self) -> None:
        """Переход на страницу назад по кнопке Back"""
        with allure.step('Возвращение назад'):
            self.click((By.XPATH, "//a[text()='Back']"))

    def edit_personal_details(self, first_name: str, last_name: str, email: str) -> None:
        """
        Изменение персональных данных текущего аккаунта
        :param first_name: First Name
        :param last_name: Last Name
        :param email: E-Mail
        """
        with allure.step('Изменение персональных данных'):
            self.fill_input_field('First Name', first_name)
            self.fill_input_field('Last Name', last_name)
            self.fill_input_field('E-Mail', email)
            self.click(MyAccountPage.CONTINUE_BUTTON)
