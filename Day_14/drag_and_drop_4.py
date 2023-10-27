# The two main thing you need to know while performing the drag and drop
# source element and target element

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

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

# source and target element for the rome element
src_ele = driver.find_element(By.XPATH, "//div[@id='box6']")
tar_ele = driver.find_element(By.XPATH, "//div[@id='box106']")

act = ActionChains(driver)

# Pass the src and trg element to the method
act.drag_and_drop(src_ele, tar_ele).perform()

# to perform it for multiple elements repeat the same process

time.sleep(3)
driver.close()