# double click operation

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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")

# text = "Hello World"

# as the element is in Iframe so we have to switch to the frame
driver.switch_to.frame("iframeResult")

button = driver.find_element(By.XPATH, "//button[normalize-space()='Double-click me']")

act = ActionChains(driver)

act.double_click(button).perform()

# p = driver.find_element(By.XPATH, "//p[@id='demo']")

# if p.text == text:
#     print("test case passed")
# else:
#     print("test case failed")
    

time.sleep(3)
driver.close()