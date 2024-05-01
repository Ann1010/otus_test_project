import sys

import allure
import pytest

from front_tests.pages.catalog_page import CatalogPage
from front_tests.pages.login_page import LoginPage
from front_tests.pages.navigation_panel import NavigationPanel
from front_tests.pages.top_panel import TopPanel
from front_tests.pages.wish_list_page import WishListPage
from front_tests.pages.register_page import RegisterPage
from front_tests.helpers import help


sys.path.append(".")


@pytest.mark.front
@allure.epic("Front")
@allure.feature('My Wishlist Page')
class TestWishListPage:
    first_name = 'test_user_firstname'
    last_name = 'test_user_lastname'
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

    @allure.story('Проверка добавления продукта в Wish List и его отображение в разделе')
    def test_add_product_to_wish_list(self, browser):
        NavigationPanel(browser).go_to_top_tab('Phones & PDAs')
        CatalogPage(browser).add_to_wish_list('HTC Touch HD')
        TopPanel(browser).open_wish_list_page()
        page = WishListPage(browser)
        page.check_wish_list(['HTC Touch HD'])

    @allure.story('Проверка удаления продукта из Wish List')
    def test_delete_product_from_wish_list(self, browser):
        product_name = 'iPhone'
        NavigationPanel(browser).go_to_top_tab('Phones & PDAs')
        CatalogPage(browser).add_to_wish_list(product_name)
        TopPanel(browser).open_wish_list_page()
        page = WishListPage(browser)
        page.check_wish_list([product_name])
        page.check_delete_product(product_name)
