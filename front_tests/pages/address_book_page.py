import allure
from selenium.webdriver.common.by import By

from front_tests.pages.base_page import BasePage


class AddressBookPage(BasePage):
    SUCCESS_ALERT = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    NEW_ADDRESS = (By.XPATH, "//div[@id='address']//tr[last()]/td")

    def open_create_new_address_form(self) -> None:
        """Открытие формы Add address"""
        with allure.step('Открытие формы Add address'):
            self.click((By.XPATH, "//a[text()='New Address']"))

    def create_add_new_address(self, first_name: str, last_name: str, address_1: str,
                               city: str, post_code: str, country: str, region_or_state: str) -> str:
        """
        Создание нового адреса (по обязательным полям)
        :param first_name: First Name
        :param last_name: Last Name
        :param address_1: Address 1
        :param city: City
        :param post_code: post_code
        :param country: Country
        :param region_or_state: Region / State.
        """
        with allure.step('Создание нового адреса'):
            self.open_create_new_address_form()
            self.fill_input_field('First Name', first_name)
            self.fill_input_field('Last Name', last_name)
            self.fill_input_field('Address 1', address_1)
            self.fill_input_field('City', city)
            self.fill_input_field('Post Code', post_code)
            self.choose_in_select('input-country', country)
            self.choose_in_select('input-zone', region_or_state)
            self.click((By.XPATH, "//button[text()='Continue']"))
        new_address = self.get_element(self.NEW_ADDRESS).text
        expected_address = (f'{first_name} {last_name}\n'
                            f'{address_1}\n'
                            f'{city}, {region_or_state} {post_code}\n'
                            f'{country}')
        self.assert_text(self.SUCCESS_ALERT, 'Your address has been successfully added')
        assert new_address == expected_address, \
            (f"Созданный адрес отличается от ожидаемого\n"
             f"ОР: {expected_address}\n"
             f"ФР: {new_address}")
        return f"{first_name} {last_name}, {address_1}, {city}, {region_or_state}, {country}"
