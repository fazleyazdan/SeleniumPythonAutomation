# scenario: i visited a page and click on the register...
# normally what happens is that it open the register in the same page....
#! i want to open the registeration in a different page and then switch to it without losing the homepage
#* we have a shortchut in chrome browser ctrl+enter to open a link in a new tab
#! now this shortcut can be different for different browsers


import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(3)
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()

# newtab = Keys.CONTROL+Keys.RETURN    #* Return Refers to Enter
# driver.find_element(By.LINK_TEXT, "Register").send_keys(newtab)    #! so we are passing the keys to open this in newtab 


#* Method 2: in this method we can open a new tab through a command avail in selenium 4
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.dummyticket.com/")

#* now to open a tab in in new window specify window in place of tab
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.dummyticket.com/")


time.sleep(3)
driver.close()