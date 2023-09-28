
# from selenium import webdriver
# import time

# # Create a WebDriver instance
# browser = webdriver.Chrome()

# # Open the website
# browser.get('https://www.jumia.com.ng/catalog/?q=shoes+men+sneackers')
# elementssList = browser.find_element(By.CSS_SELECTOR, "div.-paxs.row._no-g._4cl-3cm-shs")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.jumia.com')
assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('spagetti' + Keys.RETURN)

# Add a delay to keep the browser open (e.g., 10 seconds)
time.sleep(5000)

# Close the browser when done
browser.quit()







