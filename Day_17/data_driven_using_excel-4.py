# data driven test approach
# in this task first we will extract data from the excel sheet and then we will access the web 
# after that we will do actions needed
#! we do validation on numbers not on strings

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import excel_utils

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

file_path = "D:\\data_driven_test_data.xlsx"
noOfRows = excel_utils.getRowCount(file_path, 'test_data')

 
#* Reading data from excel
#! since we are passing only values of first row. so one for loop is enough. won't be using loop for cols

for r in range (2, noOfRows+1):                  #! first is header row that's why we are starting from 2 
    principle_data = excel_utils.readData(file_path, 'test_data', r, 1)
    rate_data = excel_utils.readData(file_path, 'test_data', r, 2)
    p1_data = excel_utils.readData(file_path, 'test_data', r, 3)
    p2_data = excel_utils.readData(file_path, 'test_data', r, 4)
    frequency_data = excel_utils.readData(file_path, 'test_data', r, 5)
    exp_maturity_value = excel_utils.readData(file_path, 'test_data', r, 6)
    
#* passing data to the application
#* to pass data to app from excel we have to capture the loc of web elements

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle_data)  
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_data)  
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(p1_data)
    p2_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    p2_dropdown.select_by_visible_text(p2_data)
    frqncy_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frqncy_dropdown.select_by_visible_text(frequency_data)

    driver.find_element(By.XPATH, "//div[@class='cal_div']//a[1]/img").click()                        #! calculate button
    actual_maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text    #! result from web

#* Validation : as the result may be in decimal form so we have to convert it to number/float

    if float(exp_maturity_value) == float(actual_maturity_value):
        print("test case passed !")
        excel_utils.writeData(file_path, 'test_data', r, 8, 'passed')
        excel_utils.fillGreenColor(file_path, 'test_data', r , 8)
    else:
        print("test case failed !")
        excel_utils.writeData(file_path, 'test_data', r, 8, 'failed')
        excel_utils.fillRedColor(file_path, 'test_data', r , 8)

#* clear the form for next iteration
    driver.find_element(By.XPATH, "//div[@class='PT25']//a[2]").click()                 


time.sleep(10)
driver.close()
