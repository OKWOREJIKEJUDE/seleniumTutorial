
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_path = "C:\\Drivers_i_downloaded\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")

# After user input, close the browser window
driver.quit()