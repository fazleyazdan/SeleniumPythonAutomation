# Mouse operation
# when we want to double click or do something in by mouse in automation it is called mouse operartion
# for that we use a class called 'ActionChains'
# 1: Mouse hover
# 2: Right click
# 3: Double click
# 4: Drag & Drop

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
driver.get("https://practice.expandtesting.com/hovers")
hover1 = driver.find_element(By.XPATH, "//div[@class='container']//div[1]//img[1]")
hover2 = driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[1]/a[1]")

# To perform Mouse Operations we have to import a class 'ActionChains' & make its objects
# ActionChains require 'driver' instance to be passed to it

act_obj = ActionChains(driver)

# move_to_element is used for mouse hover operation
# upto click it is only action making. perform is used to execute that action
act_obj.move_to_element(hover1).move_to_element(hover2).click().perform() 

print("Test case Passed !")

time.sleep(3)
driver.close()
