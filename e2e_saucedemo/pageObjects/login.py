from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        user_name = self.wait.until(
            EC.presence_of_element_located(self.username_field))
        user_name.send_keys("standard_user")
        password = self.wait.until(
            EC.presence_of_element_located(self.password_field))
        password.send_keys("secret_sauce")
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button))
        login_button.click()
