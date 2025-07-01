# login.py

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
        self.credential_box = (By.ID, "login_credentials")
        self.password_box = (By.CLASS_NAME, "login_password")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def get_usernames(self):
        text = self.driver.find_element(*self.credential_box).text
        return text.replace("Accepted usernames are:", "").strip().split("\n")

    def get_password(self):
        text = self.driver.find_element(*self.password_box).text
        return text.replace("Password for all users:", "").strip()

    def login(self, username, password):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
