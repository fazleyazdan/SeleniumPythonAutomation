import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(7)
driver.get('https://practice-automation.com/form-fields/')

# capturing multiple xpaths of the 'milk' checkbox
#! the first xpath is wrong, just to check methode is working in case of multiple xpaths

xpaths = [
    "//wrongxpath",
    "//input[@type = 'checkbox'][2]",
    "//input[@id='drink2']"
]

# Loop through each XPath and try to find the element
element = None
for xpath in xpaths:
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        break  # Exit the loop if element is found successfully
    except:
        pass  # Try the next XPath if current one fails

if element:
    element.click()
    print("Element found successfully.")
else:
    print("Element not found.")

