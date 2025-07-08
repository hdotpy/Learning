from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath("/Users/sih/Downloads"),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()

file_to_download = "1.png"
download_link = driver.find_element(By.LINK_TEXT, file_to_download)
download_link.click()

time.sleep(2)  # Wait for the download to complete
download_dir = "/Users/sih/Downloads"
downloaded_file_path = os.path.join(download_dir, file_to_download)

if os.path.exists(downloaded_file_path):
    print(f"✅ File '{downloaded_file_path}' downloaded successfully!")
else:
    print(f"❌ File '{downloaded_file_path}' not found!")

time.sleep(2)  # Ensure the file is downloaded
