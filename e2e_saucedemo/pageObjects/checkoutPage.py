from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckOut:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.checkout_button = (By.NAME, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def enter_checkout_info(self):
        try:
            check = self.wait.until(
                EC.element_to_be_clickable(self.checkout_button))
            check.click()
            first_name_input = self.wait.until(
                EC.presence_of_element_located(self.first_name_field))
            first_name_input.send_keys("ABC")
            last_name_input = self.wait.until(
                EC.presence_of_element_located(self.last_name_field))
            last_name_input.send_keys("EFG")
            postal_code_input = self.wait.until(
                EC.presence_of_element_located(self.postal_code_field))
            postal_code_input.send_keys("600001")
            continue_button = self.wait.until(
                EC.element_to_be_clickable(self.continue_button))
            continue_button.click()
        except Exception as e:
            print(f" ❌ Error during checkout: {e}")

    def finish(self):
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.finish_button))
        finish_button.click()

    def get_screenshot(self):
        self.driver.save_screenshot("checkout_page_screenshot.png")
