from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.homePage import HomePage
from pageObjects.productPage import ProductPage


def test_top10(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 25)

    home_page = HomePage(driver, wait)
    home_page.load()
    home_page.search()

    product_page = ProductPage(driver, wait)
    samsung_filter_element = product_page.filter_action()

    assert "samsung" in samsung_filter_element.text.lower(), "Samsung filter not applied"
    product_page.get_products()
