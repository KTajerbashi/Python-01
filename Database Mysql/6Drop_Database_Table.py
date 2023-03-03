import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123123",
  database="Shop1"
)

mycursor = mydb.cursor()

sql = "DROP TABLE teachers"

mycursor.execute(sql)