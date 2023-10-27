#  Sometime you are required to right click on a button or text to perform an action        
#  for that purpose we use right click mouse action to proceed further

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
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

act = ActionChains(driver)      # create Action

act.context_click(button).perform()   # perform Right click action


# Note : uncomment this section if you want to see the extra steps in browser
# time.sleep(2)
# copy = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
# copy.click()

# driver.switch_to.alert.accept()

time.sleep(3)

driver.close()