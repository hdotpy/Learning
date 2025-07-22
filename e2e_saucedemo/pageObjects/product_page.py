from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_button = (
            By.XPATH, ".//button[contains(text(), 'Add to cart')]")
        self.cart_badge = (
            By.CSS_SELECTOR, "span[class='shopping_cart_badge']")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        try:
            items = self.wait.until(
                EC.presence_of_all_elements_located(self.inventory_items)
            )
            for item in items:
                item_name = item.find_element(
                    By.CLASS_NAME, "inventory_item_name").text
                item_price = item.find_element(
                    By.CLASS_NAME, "inventory_item_price").text
                add_button = item.find_element(*self.add_to_cart_button)
                add_button.click()
                print(f" ✅ {item_name} with price {item_price} added to cart.")
        except Exception as e:
            print(f" ❌ Error while adding items to cart: {e}")

    def cart_badge_locator(self):
        badge = self.wait.until(
            EC.presence_of_element_located(self.cart_badge))
        return badge.text

    def cart_link_click(self):
        try:
            cart_link = self.wait.until(
                EC.presence_of_element_located(self.cart_link))
            cart_link.click()
        except Exception as e:
            print(f" ❌ Error while clicking on cart link: {e}")
