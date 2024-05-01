import time

from selenium.webdriver.common.by import By
import allure

from front_tests.pages.base_page import BasePage
from front_tests.helpers import help


class AddressBookPage(BasePage):
    TAB_BUTTONS = (By.XPATH, "//div[@id='content']//a")
    TAB_IN_GROUP = (By.XPATH, "//div[@class='list-group mb-3']//a")

    def open_create_new_address_form(self):
        with allure.step('Открытие формы Add address'):
            self.click((By.XPATH, "//a[text()='New Address']"))

    def create_add_new_address(self, first_name:str, last_name: str, address_1: str,
                           city: str, post_code:str, country: str, region_or_state: str, **kwargs):
        self.open_create_new_address_form()
        self.fill_input_field('First Name', first_name)
        self.fill_input_field('Last Name', last_name)
        self.fill_input_field('Address 1', address_1)
        self.fill_input_field('City', city)
        self.fill_input_field('Post Code', post_code)
        self.choose_in_select('input-country', country)
        self.choose_in_select('input-zone', region_or_state)
        self.click((By.XPATH, "//button[text()='Continue']"))
        new_address = self.get_element((By.XPATH, "//div[@id='address']//tr[last()]/td")).text
        expected_address = (f'{first_name} {last_name}\n'
                            f'{address_1}\n'
                            f'{city}, {region_or_state} {post_code}\n'
                            f'{country}')
        assert self.get_element((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")).text == 'Your address has been successfully added', \
            "После создания не отображается сообщение Your address has been successfully added"
        assert new_address == expected_address, \
            (f"Созданный адрес отличается от ожидаемого\n"
             f"ОР: {expected_address}\n"
             f"ФР: {new_address}")
        return f"{first_name} {last_name}, {address_1}, {city}, {region_or_state}, {country}"

    def go_to_tab(self, tab_name):
        with allure.step(f'Переход в раздел {tab_name}'):
            self.click(help.locator_with_contains(self.TAB_IN_GROUP, tab_name))
            self.wait_title(tab_name)

    def check_my_account_tabs(self):
        with allure.step('Проверка разделов My account'):
            tabs = ['Edit your account information', 'Change your password', 'Modify your address book entries',
                    'Modify your wish list']
            for tab in tabs:
                self.assert_element(help.locator_with_contains(self.TAB_BUTTONS, tab))
