import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.login import LoginPage
from pageObjects.product_page import ProductPage
from pageObjects.checkoutPage import CheckOut


def test_e2e_saucedemo(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 25)

    loginpage = LoginPage(driver, wait)
    loginpage.load_page()
    loginpage.login()

    productpage = ProductPage(driver, wait)
    productpage.add_items_to_cart()
    assert productpage.cart_badge_locator() == '6', "Cart number mismatch"
    productpage.cart_link_click()

    checkout = CheckOut(driver, wait)
    checkout.enter_checkout_info()
    checkout.finish()
    checkout.get_screenshot()
