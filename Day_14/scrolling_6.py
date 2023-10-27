# scrolling is also mouse operation but we can't perform it using actionchains
# it is because when content of the web page can't be showed on one page then scroll bar is added by the browser
# so scroll bar is not from the application it is from the browser hence can't be handled by actionchains
# as scoll bar is designed using javascript so we have to write some script to handle it
# there are four ways in which we can perform scrolling 
# Note : uncomment the option you want to test

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
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# 1 : scoll down page by pixels 

# driver.execute_script("window.scrollBy(0,3000)")  # inside the execute we passed javascript statement and passed a window methode
# # we use execute_script for executing javascript statements

# value = driver.execute_script("return window.pageYOffset;")  # semicolon will also be added since it is JS
# print("number of pixel scrollbar moved: ", value)     #   2999

# 2 : scoll down page till the element is visible/found
# for that we have to first capture that element

# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Pakistan']")
# driver.execute_script("arguments[0].scrollIntoView()",flag)  # passed two arguments  


# now if you want to know how much the scroll bar is moved use this statement
# value = driver.execute_script("return window.pageYOffset;") 
# print("number of pixel scrollbar moved: ", value)    

# 3 : scroll down till the end page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "") 

# now if you want to know how much the scroll bar is moved use this statement
value = driver.execute_script("return window.pageYOffset;") 
print("number of pixel scrollbar moved: ", value)   #   9560.7548828125

time.sleep(4)

# 4 : scroll up the page to the start
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)", "")   # here we have added the substract sign 

time.sleep(3)
driver.close()