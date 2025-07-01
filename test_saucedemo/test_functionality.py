from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.homePage import HomePage
from pageObjects.productPage import ProductPage
from pageObjects.checkoutPage import Checkout
import pytest


def test_add_to_cart(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 25)

    home_page = HomePage(driver, wait)
    home_page.load()
    home_page.get_title()
    home_page.login()

    product_page = ProductPage(driver, wait)
    product_page.sort_filter()
    product_page.select_backpack()
    assert product_page.get_cart_badge() == "1"
    product_page.select_red_shirt()
    product_page.remove_backpack()
    product_page.products_in_cart()
    product_page.checkout()

    checkout_page = Checkout(driver, wait)
    checkout_page.enter_details()
    checkout_page.get_ss()
