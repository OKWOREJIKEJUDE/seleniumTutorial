from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()
myDriver.get("https://demo.nopcommerce.com")

# todo SCENARIOS OF FIND ELEMENT TO CHECK
# todo 1. Locator matching with single web element
element = myDriver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
element.send_keys("Apple MacBook Pro 13-inch")

# todo 2. Locator matching with multiple web element
# todo in this example, we used a keyword say "footer" to capture all the links we want.Type "//div[@class='footer']//a" on the selector hub space to highlight them
element = myDriver.find_element(By.XPATH, "//div[@class='footer']//a") # this will return multiple web elements. among the elements returned, the first one only will display b/c of our keyword element
print(element.text)

# todo 3. Element not available, then throw NoSuchElementException
# todo findElement throws an exception once the key is wrong(LINK_TEXT is not complete)
element = myDriver.find_element(By.LINK_TEXT, "Log")
element.click()









input("click any key to terminate...")
myDriver.quit()

