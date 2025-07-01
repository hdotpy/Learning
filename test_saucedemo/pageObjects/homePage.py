import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self):
        try:
            self.driver.get("https://www.saucedemo.com/")
        except Exception as e:
            print(f"Error loading SauceDemo: {e}")
            raise
        self.driver.maximize_window()

    def get_title(self):
        try:
            title = self.driver.title
            print(title)
            return title
        except Exception as e:
            print(f"Error getting title: {e}")
            raise

    def login(self):
        username = self.wait.until(
            EC.presence_of_element_located(self.username_field))
        password = self.wait.until(
            EC.presence_of_element_located(self.password_field))
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        
