import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.category_relevance = (
            By.XPATH, "//div[contains(text(),'Relevance')]")
        self.max_filter_option = (By.XPATH, "(//select[@class='Gn+jFg'])[2]")
        self.brand_search = (By.XPATH, "//input[@class='XPD6hh']")
        self.filter_samsung = (
            By.XPATH, "//div[@class='_6i1qKy' and contains(text(),'Samsung')]")
        self.products = (By.XPATH, "//div[@class='tUxRFH']")
        self.name = (By.XPATH, ".//div[@class='KzDlHZ']")
        self.price = (By.XPATH, ".//div[contains(@class, '_4b5DiR')]")

    def filter_action(self):
        relevance = self.wait.until(
            EC.element_to_be_clickable(self.category_relevance))
        relevance.click()
        time.sleep(2)

        max_filter = self.wait.until(
            EC.presence_of_element_located(self.max_filter_option))
        max_filter_select = Select(max_filter)
        max_filter_select.select_by_value("10000")
        time.sleep(2)

        brand = self.wait.until(
            EC.presence_of_element_located(self.brand_search))
        brand.clear()
        brand.send_keys("Samsung")

        samsung_filter = self.wait.until(
            EC.element_to_be_clickable(self.filter_samsung))
        samsung_filter.click()

        # ✅ Wait for product list to update after clicking Samsung
        self.wait.until(EC.presence_of_all_elements_located(self.products))
        time.sleep(3)  # Give time for filtered results to load

        return samsung_filter

    def get_products(self):
        product_details = self.wait.until(
            EC.presence_of_all_elements_located(self.products))
        top_10 = product_details[:10]
        for i, product in enumerate(top_10):
            try:
                product_name = product.find_element(
                    *self.name).text
                product_price = product.find_element(
                    *self.price).text

                print(f"{i + 1}: {product_name} - {product_price}")
            except Exception as e:
                print(f"Error retrieving product {i + 1}: {e}")
