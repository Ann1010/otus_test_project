import time

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



