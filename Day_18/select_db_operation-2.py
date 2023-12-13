

import mysql.connector

insert_query = "insert into language values (7, 'urdu', '2023-12-12')"           
update_query = "update language set name= 'pashto' where language_id= 7"         
delete_query = "delete from language where language_id= 7"



try:
    conn = mysql.connector.connect(host = "localhost", port = "3306", user = "root", passwd = "777Fslfs!.", database = "sakila")
    curs = conn.cursor()
    
    curs.execute("select * from language")      #! SQL is not case sensitive you can use upper and lower case both

#* we have to use for loop because we don't know how much data is in the cusror

    for row in curs:
        print(row[0], row[1], row[2])           
        #! there are three columns in the table. number in square brackets represents different columns of the same row
        #! after printing values of the mentioned columns there will be another iteration and values of another row will be printed
                
    conn.close()                    
except:
    print("connection unsuccessfull")
    
    