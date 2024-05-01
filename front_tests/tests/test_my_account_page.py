import sys

import allure
import pytest

from front_tests.helpers import help
from front_tests.pages.address_book_page import AddressBookPage
from front_tests.pages.my_account_page import MyAccountPage
from front_tests.pages.register_page import RegisterPage
from front_tests.pages.top_panel import TopPanel

sys.path.append(".")


@pytest.mark.front
@allure.epic("Front")
@allure.feature('My Account Page')
class TestAccountPage:
    first_name = 'test_user'
    last_name = 'test_lastname'
    email = help.random_email()
    print(email)
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

    @allure.story('Проверка раздела на странице My Account')
    def test_check_my_account_page(self, browser):
        page = MyAccountPage(browser)
        page.check_my_account_tabs()

    @allure.story('Проверка перехода по разделам из раздела My Accounts и возвращение по кнопке Back')
    @pytest.mark.parametrize('tab_name, title', [('Edit Account', 'My Account Information'),
                                                 ('Password', 'Change Password'),
                                                 ('Address Book', ''),
                                                 ('Newsletter', 'Newsletter Subscription')])
    def test_check_go_to_tabs(self, browser, tab_name, title):
        page = MyAccountPage(browser)
        page.go_to_tab(tab_name, title)
        page.click_back_button()
        page.wait_title('My Account')

    @allure.story('Проверка изменения данных в профиле c пустыми обязательными полями')
    def test_check_update_personal_details(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Edit Account', title='My Account Information')
        page.edit_personal_details(first_name='', last_name=self.last_name, email=self.email)
        assert page.get_element(MyAccountPage.ERROR_FIRSTNAME_MESSAGE).text == ('First Name must be between 1 and 32 '
                                                                                'characters!'), \
            "При не заполненном поле First Name не отображается ошибка First Name must be between 1 and 32 characters!"
        page.edit_personal_details(first_name=self.first_name, last_name='', email=self.email)
        assert page.get_element(
            MyAccountPage.ERROR_LASTNAME_MESSAGE).text == 'Last Name must be between 1 and 32 characters!', \
            "При не заполненном поле Last Name не отображается ошибка Last Name must be between 1 and 32 characters!"
        page.edit_personal_details(first_name=self.first_name, last_name=self.last_name, email='')
        assert page.get_element(
            MyAccountPage.ERROR_EMAIL_MESSAGE).text == 'E-Mail Address does not appear to be valid!', \
            "При не заполненном поле E-Mail не отображается ошибка E-Mail Address does not appear to be valid!"

    @allure.story("Проверка изменения данных с некорректными значениями - диапазон больше 32 символов")
    def test_check_update_personal_details_with_incorrect_value(self, browser):
        incorrect_value = '1234567890123456789012345678901234'
        page = MyAccountPage(browser)
        page.go_to_tab('Edit Account', title='My Account Information')
        page.edit_personal_details(first_name=incorrect_value, last_name=self.last_name, email=self.email)
        assert page.get_element(MyAccountPage.ERROR_FIRSTNAME_MESSAGE).text == ('First Name must be between 1 and 32 '
                                                                                'characters!'), \
            "При не заполненном поле First Name не отображается ошибка First Name must be between 1 and 32 characters!"
        page.edit_personal_details(first_name=self.first_name, last_name=incorrect_value, email=self.email)
        assert page.get_element(
            MyAccountPage.ERROR_LASTNAME_MESSAGE).text == 'Last Name must be between 1 and 32 characters!', \
            "При не заполненном поле Last Name не отображается ошибка Last Name must be between 1 and 32 characters!"

    @allure.story("Проверка изменения данных Имени и Фамилии")
    def test_check_update_personal_details_with_incorrect_value(self, browser):
        new_first_name = 'new_first_name'
        new_last_name = 'new_last_name'
        page = MyAccountPage(browser)
        page.go_to_tab('Edit Account', title='My Account Information')
        page.edit_personal_details(first_name=new_first_name, last_name=new_last_name, email=self.email)
        page.wait_title('My Account')
        assert page.get_element(MyAccountPage.SUCCESS_MESSAGE).text == ('Success: Your account has been successfully '
                                                                        'updated.'), \
            "После обновления данных не отображается сообщение: Success: Your account has been successfully updated."

    @allure.story('Проверка создания нового адреса')
    def test_check_add_address(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Address Book')
        page = AddressBookPage(browser)
        page.create_add_new_address(first_name='Иван', last_name='Иванов', address_1='ул. Лесная, д. 5, кв. 1098',
                                    city='Лосака', post_code='102312', country='Zambia', region_or_state='Central')
