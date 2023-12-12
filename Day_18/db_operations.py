# DB operations which are going to be practiced
#! to work with the database we need to install mysql-connector-python
#* Insert, Update , Delete (these opeartions are going to do changes to the tables)
#* Select command will fetch data from the tables and return those data
#* in this case our python code is acting as a client because we are sending queries through python code to the db server

import mysql.connector

insert_query = "insert into language values (7, 'urdu', '2023-12-12')"           #! 'language' is a table inside the sakila database
update_query = "update language set name= 'pashto' where language_id= 7"         #! set is a keyword. 'name' & 'language_id' are attributes inside the language table
delete_query = "delete from language where language_id= 7"


#* sometimes the connection details is incorrect or database is down. other reasons can also occur. that's why use try catch
#* we have to provide connection details to the the connector and store it in a variable which is the object
try:
    conn = mysql.connector.connect(host = "localhost", port = "3306", user = "root", passwd = "777Fslfs!.", database = "sakila")

#! now we have to make a cursor to send the queries
#! cursor act as a buffer (a temporary memory)
    curs = conn.cursor()
#   curs.execute(insert_query)
#   curs.execute("insert into language values (7, 'urdu', '2023-12-12')")     #* we can also use this 
#   curs.execute(update_query)
    curs.execute(delete_query)


#* after executing the query it will temporary update the db, however if you want to make changes permanant you have to commit it.
    conn.commit()                   #! commit the transaction [insert, update, delete everything is a transaction]
    conn.close()                    #! close the connection
except:
    print("connection unsuccessfull")
    
    