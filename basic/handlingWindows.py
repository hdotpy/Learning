from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

# Parent window handle

h3_message = driver.find_element(By.TAG_NAME, "h3").text
print(f"Message on the page: {h3_message}")

click_here_link = driver.find_element(By.LINK_TEXT, "Click Here")
click_here_link.click()

windows = driver.window_handles

# Navigate to child window
driver.switch_to.window(windows[1])
new_window_message = driver.find_element(By.TAG_NAME, "h3").text
print(f"Message in the new window: {new_window_message}")
