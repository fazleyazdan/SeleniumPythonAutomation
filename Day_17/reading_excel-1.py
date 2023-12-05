
#* so we have an Excel file then inside we have workbooks then we have sheets inside it are multiple rows and inside rows we have multiple cells
#! File --> Workbooks --> Sheets --> Rows --> Cells
 
import openpyxl

file_path = "D:\Automation_practice.xlsx"          #! save file path 
workbook = openpyxl.load_workbook(file_path)       #! load workbook
sheet = workbook["Books"]                          #! save sheet 

#* now we can print number of rows and columns 

rows = sheet.max_row                      
col = sheet.max_column

print("number of rows:", rows)
print("number of col:", col)
