import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(3)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# click to open the dropdown
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

# store list of all countries
countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

print (len(countries_list))

# select a country from the country list
for country in countries_list:
    if country.text == "Palestinian Territory":
        country.click()
        break