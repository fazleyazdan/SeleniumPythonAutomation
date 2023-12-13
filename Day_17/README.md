# Notes:

# --> in general, getting data from the database and passing it to the application is called data driven testings

==> Data Driven Testing : in data driven testing , testing are driven by data:

==> meaning the same test case is run multiple times by changing the data

==> most of the times we read data for test cases from the database or excel sheet. 

==> selenium by default does not work with excel. it is solely used for automation

==> we have to install a library for that called "openpyxl"

==> this library works only with .xlsx extensions


# in Almost every Data driven test (which involve excel operations)
# Automation code
# Excel Operation ==> reading ==> writing ==> rows ==> Col ==> fill green/red
# Cons : script along with the excel code make it complex
# also repetition is there. in every data driven test case which involves excel operation there is duplication of code

# Data driven test Approach:
# so in real time application we have something called "Excel Utils" file.
# Excel Utils ==> contains every oepration related to excel
# it contains only functions and whenever it is needed they are called. (Reuseability)

# when we are capturing data from the excel it is in the string format
