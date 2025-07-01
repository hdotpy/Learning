from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.input_search = (
            By.XPATH, "//input[@title='Search for Products, Brands and More']")
    def load(self):
        try:
            self.driver.get("https://www.flipkart.com/")
        except Exception as e:
            print(f"Error loading Flipkart: {e}")
            raise
        self.driver.maximize_window()

    def search(self):
        search_box = self.wait.until(
            EC.presence_of_element_located(self.input_search))
        search_box.send_keys("mobile")
        search_box.send_keys(Keys.RETURN)
