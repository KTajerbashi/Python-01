import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "123123",
    database = "faradars"
)

cursor = db.cursor()

## creating a table called 'users' in the 'faradars' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")