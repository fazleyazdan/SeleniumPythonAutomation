# headless testing means testing without seeing the UI
#* in other words testing is executed in the backend and you will see results on terminal
#* normally what happens is, when executing test cases we see the ui 
#! PROS: in headless mode the script is running in backend and the screen is not occupied and you can do other activities as well
#* script execution is faster in headless mode (performance is increased)
#! CONS: suppose you newly joined a company and you want to know app funvtionality....
#* now we know that there is no UI actions involved and everything is running in backend...
#* so in essence you are not learning anything specially the functionality of an app.....
#! headless testing is different in different browser

from selenium import webdriver

def headless_chrome():                      #! for chrome browser
    from selenium.webdriver.chrome.service import Service
    ser_obj= Service("C:\Drivers\chromedriver\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')      #! for headless mode
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service = ser_obj, options = options)
    return driver

# def headless_edge():                        #! for Edge browser
#     from selenium.webdriver.edge.service import Service
#     ser_obj= Service("C:\Drivers\edgedriver\chromedriver.exe")
#     options = webdriver.EdgeOptions()
#     options.add_argument('--headless')      #! for headless mode
#     # options.add_experimental_option("detach", True)
#     driver = webdriver.Edge(service = ser_obj, options = options)
#     return driver


# driver = headless_edge()
driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print("Title :", driver.title)
print("URL :", driver.current_url)

driver.close()



