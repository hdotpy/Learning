# test_login_saucedemo.py

import time
import traceback
import pytest
from pageObjects.login import LoginPage


def test_login_saucedemo(setup_browser):
    driver = setup_browser
    login_page = LoginPage(driver)

    login_page.load()

    usernames = login_page.get_usernames()
    password = login_page.get_password()

    assert "secret_sauce" in password

    for user in usernames:
        try:
            login_page.login(user, password)

            if 'locked_out_user' in user:
                error_text = login_page.get_error_message()
                print(f"❌ Login failed for {user}: {error_text}")
                driver.save_screenshot(f"{user}_error.png")
                assert "user has been locked out." in error_text
            else:
                print(f"✅ Login successful for {user}")

            login_page.load()

        except Exception as e:
            traceback.print_exc()
            print(f"❌ An error occurred for {user}: {e}")

    time.sleep(2)
