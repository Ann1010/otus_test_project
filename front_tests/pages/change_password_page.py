import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class ChangePasswordPage(BasePage):
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Continue']")
    ERROR_PASSWORD_MESSAGE = (By.XPATH, "//div[@id='error-password']")
    ERROR_CONFIRM_MESSAGE = (By.XPATH, "//div[@id='error-confirm']")

    def click_continue_button(self):
        with allure.step('Нажатие на кнопку Continue'):
            self.click(self.CONTINUE_BUTTON)

    def change_password(self, password, password_confirm) -> None:
        """
        Изменение пароля.
        :param password: Новый пароль
        :param password_confirm: Подтверждение нового пароля
        """
        with allure.step('Изменение пароля'):
            self.fill_input_field('Password', password)
            self.fill_input_field('Password Confirm', password_confirm)
            self.click_continue_button()
