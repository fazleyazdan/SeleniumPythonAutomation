# in this task we are going to practice data driven test cases
#* but this time i am going to use mysql to get data from the database instead of excel
#! str(row[1]): i have used str because these values have decimal data type in DB and i was encountering the error that decimal are not iterable 

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import mysql.connector

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

ser_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=ser_obj)

driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()



    #* establish connection\
conn = mysql.connector.connect(host = "localhost", port = "3306", user = "root", passwd = "777Fslfs!.", database = "sakila")
curs = conn.cursor()
curs.execute("select * from test_data")  

    #* as we know data is in cursor so we have to use a loop on the cursor to get the data from it and save it in variables 
for row in curs:
    principle_data = str(row[0])     
    #* principle_data_str = str(principle_data)
    rate_data = str(row[1])
    p1_data = str(row[2])
    p2_data = row[3]
    frequency_data = str(row[4])
    exp_maturity_value = str(row[5])
        
    #* passing data to the application
    #* to pass data to app from excel we have to capture the loc of web elements

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle_data)  
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_data)  
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(p1_data)
    p2_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    p2_dropdown.select_by_visible_text(p2_data)
    frqncy_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frqncy_dropdown.select_by_visible_text(frequency_data)

    calculate_button = driver.find_element(By.XPATH, "//div[@class='cal_div']//a[1]/img")                #! calculate button
    driver.execute_script("arguments[0].scrollIntoView(true);", calculate_button)                        #! button is not in viewport so we have to scroll to click it   
    calculate_button.click()
    actual_maturity_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text       #! result from web

    #* Validation : as the result may be in decimal form so we have to convert it to number/float

    if float(exp_maturity_value) == float(actual_maturity_value):
        print("test case passed !")
    else:
        print("test case failed !")

    #* clear the form for next iteration
    driver.find_element(By.XPATH, "//div[@class='PT25']//a[2]").click() 
                    
conn.close()                                #! close the connection after the completion of operations 

      

time.sleep(3)
driver.close()

#* driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(row[0]) ...  
#* we can also write it like this. due to which we won't have to write this : principle_data = str(row[0])     
