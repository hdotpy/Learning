import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()

file_path = os.path.abspath("/Users/sih/Downloads/Test.txt")

choose_file = driver.find_element(By.ID, "file-upload")
choose_file.send_keys(file_path)

upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

time.sleep(2)

success_text = driver.find_element(By.XPATH, "//div[@class='example']/h3").text
assert "File Uploaded!" in success_text, "File upload failed!"
print("✅ File upload successful!")

driver.quit()
