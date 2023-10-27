# through action chains we can also perform keybaordactions

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(3)
driver.get("https://gotranscript.com/text-compare")
driver.maximize_window()

# we will send text from one input box to another for that we will perform following keyboard actions
# Ctrl+a ----> ctrl+c ----> tab ----> ctrl+v

# first capture the input boxes
input1 = driver.find_element(By.XPATH, "//textarea[@name='text1']")
input2 = driver.find_element(By.XPATH, "//textarea[@name='text2']")
input1.send_keys("Free Palestine")


act = ActionChains(driver)     

time.sleep(3)
act.key_down(Keys.CONTROL)     # now for holding the ctrl
act.send_keys("a")               # ctrl + a  for selecting all text
act.key_up(Keys.CONTROL)         # for releasing the ctrl key
act.perform()

# you can also write the above statement like this
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# now switch to the other box
act.send_keys(Keys.TAB).perform()


# now paste it to the other box
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# compare1 = "100%"
# driver.find_element(By.XPATH, "//button[@id='recaptcha']").click()
# compare2 = driver.find_element(By.XPATH, "//div[@class='s-text-compare']//div[@class='col']//div[3]/child::b").text


# if compare1 == compare2:
#     print("test case passed !")
# else:
#     print("test case failed !")

time.sleep(3)
driver.close()