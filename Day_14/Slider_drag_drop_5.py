# in the slider drag and drop we have two ends
# one is called minimum and the other is called maximum
# first we have to find the position/location of those elements (ends)
# if the elements are located on X-axis we have to change their values for changing the position of sliders
# same process will be repeated if the elements are located on y-axis 
# to the minimum side on axis we will add values and for the maximum we will substract values to change their poisition/location

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
driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")

min_slider = driver.find_element(By.XPATH, "//span[1]")
max_slider = driver.find_element(By.XPATH, "//span[2]")

print("location before moving the sliders")
print(min_slider.location)   # {'x': 152, 'y': 47}
print(max_slider.location)   # {'x': 611, 'y': 47}

# now as it is horizontal slider and we are moving on x_axis so y_axis is will not change
# we will only increase or decrease values for the x-axis and y-axis values will be zero

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 70 , 0).perform()  # pass the element, X-offset and y-offset value
act.drag_and_drop_by_offset(max_slider, -60 , 0).perform()


print("location after moving the sliders")
print(min_slider.location)   # {'x': 224, 'y': 47}
print(max_slider.location)   # {'x': 552, 'y': 47}

# as we can see that i have added 70 to the x-offset and it should be 222 but it is 224
# the differnce is always there because the resolution of the screens are different that is why

time.sleep(3)
driver.close()
