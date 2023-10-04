
from selenium import webdriver
import time

# Create a WebDriver instance
browser = webdriver.Chrome()

# Open the website
browser.get('http://selenium.dev/')

# Add a delay to keep the browser open (e.g., 10 seconds)
time.sleep(5000)

# Close the browser when done
browser.quit()









