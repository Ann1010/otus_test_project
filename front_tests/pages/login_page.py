import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Login')]")

    def login(self, email: str, password: str) -> None:
        """
        Вход в личный кабинет
        :param email: E-Mail
        :param password: Пароль
        """
        with allure.step(f"Вход в личный кабинет"):
            self.input_value(self.EMAIL_INPUT, email)
            self.input_value(self.PASSWORD_INPUT, password)
            self.click(self.LOGIN_BUTTON)
            self.wait_title('My Account')
