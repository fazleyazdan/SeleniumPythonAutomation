# in database we have two things
# 1: Database server :  it is the location in which the data will be stored in the form of tables. all the database will be saved here
# 2: database client :  it is a software through which we will connect with the database from different locations
# in the database client you have to provide the connection details required for connecting

# those details contains
# --> Hostname
# --> port no  [as every database runs on a specific port no]
# --> username
# --> password

# SQL : through SQL queries we will be able to communicate with our database
# there are many sub languages comes under the SQL. They and their operation are listed below:

# 1 : DDL --> create, alter , drop, truncate
# 2 : DML --> insert, update,  delete
# 3 : DRL --> select
# 4 : TCL --> commit, rollback 
# 5 : DCL --> grant, revoke

# NOTE : Developer or designers of the database uses DDL and DML most of the times 
# NOTE : Testers will use DML and DRL commands most of the times because they are not going to create a new database

# ABBREVIATIONS :
# DDL --> data definition language
# DML --> data manipulation language
# DRL --> data retrival language
# TCL --> transaction control language.
# DCL --> data control language.

# NOTE:
# testing with the database is also called greybox testing...
# you are testing some part of the backend and some part of the frontend.
# login to database, looking into tables etc comes under blackbox testing.

# 80% of the database testing we do it manually. because we do not have the tools to fully automate it