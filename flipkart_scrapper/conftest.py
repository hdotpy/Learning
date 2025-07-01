import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    )


@pytest.fixture(scope="function")
def setup_browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--incognito")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(4)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(4)

    else:
        raise ValueError("Unsupported browser: Choose 'chrome' or 'firefox'")

    yield driver
    driver.quit()
