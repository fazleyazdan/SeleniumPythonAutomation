# when you visit an app or site, there are some things which it remembers
#* like password , keywords etc. it is because of the cookies
#! now through automation we can find wether a site is using cookies or not and what kind of info it stores
#* there are cookie attributes and values we can also extract that. e.g cookies name, expiry date etc.
#* we can also check how many cookies are created after visiting the app
#* we can also delete specific cookies or all cookies as well
#! cookies are dynamic and they are not always the same number, every time you visit the site there is chance that a cookie is changed 
#! remember a cookie is not a web element. it is an object having attributes with key value pairs
#* so when capturing a cookie you have to store it in dictionary.one dictionary obj represents one cookie

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
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#* capturing default cookies created by the browser
cookies = driver.get_cookies()
print ("size of cookies : ", len(cookies))  #5


# for c in cookies:
    # print(c)                                                #* print all cookies
    # print(c.get('name'))                                    #* print names of cookies
    # print(c.get('name'), ":", c.get('value'))               #* print names and value of cookies
      
#! adding new cookie or user defined cookie to the browser. 
driver.add_cookie({"name" : "MyCookie", "value" : "FY777"})   #* you can add as many attributes you want
cookies = driver.get_cookies()
print ("size of cookies after adding a cookie : ", len(cookies))  #* sometimes after creating a cookie size remain the same. that means your app or site is not allowing you to create a cookie
      
#! deleting a cookie
driver.delete_cookie("MyCookie")  
cookies = driver.get_cookies()
print ("size of cookies after deleting a cookie : ", len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print ("size of cookies after deleting all cookies : ", len(cookies))


time.sleep(3)    
driver.close()