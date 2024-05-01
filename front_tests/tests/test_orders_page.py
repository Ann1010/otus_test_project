import sys

import allure
import pytest

from front_tests.helpers import help
from front_tests.pages.address_book_page import AddressBookPage
from front_tests.pages.catalog_page import CatalogPage
from front_tests.pages.checkout_page import CheckoutPage
from front_tests.pages.my_account_page import MyAccountPage
from front_tests.pages.navigation_panel import NavigationPanel
from front_tests.pages.orders_page import OrdersPage
from front_tests.pages.register_page import RegisterPage
from front_tests.pages.shopping_cart_page import ShoppingCartPage
from front_tests.pages.top_panel import TopPanel

sys.path.append(".")


@pytest.mark.front
@allure.epic("Front")
@allure.feature('Orders Page')
class TestOrdersPage:
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

    @allure.story('Проверка создания заказа и его отображение')
    def test_check_create_order(self, browser):
        page = MyAccountPage(browser)
        page.go_to_tab('Address Book')
        page = AddressBookPage(browser)
        address = page.create_add_new_address(first_name='Петр', last_name='Петров',
                                              address_1='ул. Лесная, д. 5, кв. 1098',
                                              city='Лосака', post_code='102312', country='Zambia',
                                              region_or_state='Central')
        NavigationPanel(browser).go_to_top_tab('Phones & PDAs')
        CatalogPage(browser).add_to_cart('HTC Touch HD')
        TopPanel(browser).open_shopping_cart()
        ShoppingCartPage(browser).go_to_checkout()
        total_cost = CheckoutPage(browser).create_order(address=address, shipping_method='Flat Shipping Rate - $5.00',
                                                        payment_method='Cash On Delivery')
        customer = f"{self.first_name} {self.last_name}"
        TopPanel(browser).open_my_account_tab('Order History')
        OrdersPage(browser).check_new_order(customer, total_cost)
