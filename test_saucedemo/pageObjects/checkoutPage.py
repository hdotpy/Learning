import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Checkout:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def enter_details(self):
        first_name = self.wait.until(
            EC.presence_of_element_located(self.first_name_field))
        last_name = self.wait.until(
            EC.presence_of_element_located(self.last_name_field))
        postal_code = self.wait.until(
            EC.presence_of_element_located(self.postal_code_field))

        first_name.send_keys("John")
        last_name.send_keys("Doe")
        postal_code.send_keys("12345")

        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_button))
        continue_button.click()

    def get_ss(self):
        self.driver.save_screenshot("checkout_page_screenshot.png")
