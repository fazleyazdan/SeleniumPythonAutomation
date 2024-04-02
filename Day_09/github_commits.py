# Ignore this task, as it is for my own practice

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
options.add_argument('--headless=new')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--window-size=1920,1080")
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
# options.add_argument(f'user-agent={user_agent}')
# options.headless = True

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)
driver.implicitly_wait(7)
driver.get('https://github.com/supermamon/Reposi3')
driver.get_screenshot_as_file("screenshot.png")

# Wait for a specific element to be present on the page
time.sleep(3)
# noofcommits = driver.find_element(By.XPATH, "//span[@class='Text-sc-17v1xeu-0 dALsKK']")   #! for white BG
noofcommits = driver.find_element(By.XPATH, "//span[@class='Text-sc-17v1xeu-0 UrHoN']")      #! for dark  BG

#! For white BG
# date_time = driver.find_element(By.XPATH, "//a[@class='Link__StyledLink-sc-14289xe-0 dheQRw Link--secondary']/following-sibling::relative-time")
#! For dark  BG 
date_time = driver.find_element(By.XPATH, "//a[@class='Link__StyledLink-sc-14289xe-0 elltiT Link--secondary']/following-sibling::relative-time")

date_time_value = date_time.get_attribute('title')
print(noofcommits.text)
print(date_time_value)



