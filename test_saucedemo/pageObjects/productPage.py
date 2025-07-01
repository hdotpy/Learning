from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.filter_container = (
            By.XPATH, "//select[@class='product_sort_container']")
        self.sauce_labs_backpack = (
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.red_shirt = (
            By.CSS_SELECTOR, "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        self.remove_sauce_labs_backpack = (
            By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
        self.shopping_cart_link = (By.CSS_SELECTOR, '#shopping_cart_container')
        self.chekout_button = (By.CSS_SELECTOR, "#checkout")

    def sort_filter(self):
        a_to_z = self.wait.until(EC.presence_of_element_located(
            self.filter_container)).text.strip().split("\n")
        print(a_to_z)

    def select_backpack(self):
        backpack = self.wait.until(
            EC.presence_of_element_located(self.sauce_labs_backpack))
        backpack.click()

    def get_cart_badge(self):
        badge = self.wait.until(
            EC.presence_of_element_located(self.cart_badge)).text
        print(badge)
        return badge

    def select_red_shirt(self):
        red_shirt = self.wait.until(
            EC.presence_of_element_located(self.red_shirt))
        red_shirt.click()

    def remove_backpack(self):
        remove_backpack = self.wait.until(
            EC.presence_of_element_located(self.remove_sauce_labs_backpack))
        remove_backpack.click()

    def products_in_cart(self):
        shopping_cart = self.wait.until(
            EC.element_to_be_clickable(self.shopping_cart_link))
        shopping_cart.click()
        return shopping_cart

    def checkout(self):
        checkout = self.wait.until(
            EC.element_to_be_clickable(self.chekout_button))
        checkout.click()
        return checkout
