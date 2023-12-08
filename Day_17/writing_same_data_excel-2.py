#  In this task we are going to write same data into excel file
#* there is one additional thing we have to do after writing the data we have to save it.
#! Note : specify the file path with double slash "\\". sometimes the python cant read file path with single slash
import openpyxl

file_path = "D:\\for_writing_data.xlsx"            #! save file path 
workbook = openpyxl.load_workbook(file_path)       #! load workbook
sheet = workbook.active                         
# sheet = workbook["data"]                         #! This can also be used                         


#* writing data into number of rows and col

for r in range(1,6):            #* 1-5 rows 
    for c in range(1,4):        #* 1-3 col
        sheet.cell(r,c).value="Muslim"
        
workbook.save(file_path)


