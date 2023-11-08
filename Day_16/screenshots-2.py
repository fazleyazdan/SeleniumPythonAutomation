# how to capture screenshot of a webpage through automation
# when we are performing testing and test case failed then sometimes we need to capture a screenshot ....
# so in case if the developers need it to we can capture it and store those screen shots in a folder.

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