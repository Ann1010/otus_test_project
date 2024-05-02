import sys

import allure
import pytest

from front_tests.helpers import help
from front_tests.pages.change_password_page import ChangePasswordPage
from front_tests.pages.login_page import LoginPage
from front_tests.pages.my_account_page import MyAccountPage
from front_tests.pages.register_page import RegisterPage
from front_tests.pages.top_panel import TopPanel

sys.path.append(".")


@pytest.mark.front
@pytest.mark.change_password
@allure.epic("Front")
@allure.feature("Change Password Page")
class TestChangePasswordPage:
    first_name = 'test_user'
    last_name = 'test_lastname'
    email = help.random_email()
    password = '123456aS!'

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, browser, url):
        self.page = RegisterPage(browser)
        self.page.open(f"{url}/index.php?route=account/register")
        self.page.register_user(first_name=self.first_name, lastname=self.last_name,
                                email=self.email, password=self.password)
        self.page = TopPanel(browser)
        self.page.open_my_account_tab('My Account')
        self.page.wait_title('My Account')

    @allure.story('Проверка изменения пароля аккаунта без заполненных обязательных полей')
    def test_check_change_password_without_required_fields(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Password', title='Change Password')
        with allure.step('Проверка сохранения формы Change Password без заполненного поля Password'):
            ChangePasswordPage(browser).click_continue_button()
            assert page.get_element(
                ChangePasswordPage.ERROR_PASSWORD_MESSAGE).text == "Password must be between 4 and 20 characters!", \
                f"Для поля Password не отображается подсказка Password must be between 4 and 20 characters!"
        with allure.step('Проверка сохранения формы Change Password без заполненного поля Password Confirm'):
            page.fill_input_field('Password', '1234')
            ChangePasswordPage(browser).click_continue_button()
            assert page.get_element(
                ChangePasswordPage.ERROR_CONFIRM_MESSAGE).text == "Password confirmation does not match password!", \
                f"Для поля Password Confirm не отображается подсказка Password confirmation does not match password!"

    @allure.story('Проверка заполнения поля Password некорректными значениями')
    def test_check_change_password_with_incorrect_password(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Password', title='Change Password')
        page = ChangePasswordPage(browser)
        with allure.step('Проверка сохранения формы Change Password со значением в поле Password менее 4 символов'):
            page.change_password('123', '')
            assert page.get_element(
                ChangePasswordPage.ERROR_PASSWORD_MESSAGE).text == "Password must be between 4 and 20 characters!", \
                f"Для поля Password не отображается подсказка Password must be between 4 and 20 characters!"
        with allure.step('Проверка сохранения формы Change Password  со значением в поле Password более 20 символов'):
            page.change_password('123456789012345678901', '')
            assert page.is_element_present(ChangePasswordPage.ERROR_PASSWORD_MESSAGE), \
                f"Для поля Password не отображается подсказка Password must be between 4 and 20 characters!"

    @allure.story('Проверка заполнения поля Password Confirm несовпадающим значением')
    def test_check_change_password_with_incorrect_confirm(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Password', title='Change Password')
        ChangePasswordPage(browser).change_password('123456aS!', '123456aY!')
        assert page.get_element(
            ChangePasswordPage.ERROR_CONFIRM_MESSAGE).text == "Password confirmation does not match password!", \
            f"Для поля Password Confirm не отображается подсказка Password confirmation does not match password!"

    @allure.story('Проверка изменения пароля')
    def test_check_change_password(self, browser):
        new_password = '123456aS!'
        page = MyAccountPage(browser)
        page.go_to_tab('Password', title='Change Password')
        ChangePasswordPage(browser).change_password(new_password, new_password)
        page.wait_title('My Account')
        assert page.get_element(
            MyAccountPage.SUCCESS_MESSAGE).text == "Success: Your password has been successfully updated.", \
            (f"После изменения пароля не отображается сообщение: Success: Your password has been successfully "
             f"updated.")
        TopPanel(browser).logout()
        TopPanel(browser).open_login_form()
        LoginPage(browser).login(self.email, new_password)
