from selenium import webdriver
import time

#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   # Ensure the `chromedriver` is installed and in PATH

# Open a browser
driver.get("https://google.com")

#Wait for results to load
time.sleep(180)

# Perform an action (e.g., find the search box)
#el = driver.find_element(By.NAME, "q")
#el.send_keys("Selenium Python")
#el.submit()


el = driver.find_element(By.NAME, "q")
query = "Selenium WebDriver Python"

el.send_keys("query")
el.submit()


# Close the browser
#driver.quit()


