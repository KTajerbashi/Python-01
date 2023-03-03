import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "123123"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'faradars'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'faradars' database
cursor.execute("CREATE DATABASE faradars")