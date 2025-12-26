import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",   
    user="root",
    password="Sayani@16",
)

cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS url_shortener")
cursor.execute("USE url_shortener")
cursor.execute("CREATE TABLE IF NOT EXISTS urls(id INT AUTO_INCREMENT PRIMARY KEY, long_url VARCHAR(2083) NOT NULL,short_url VARCHAR(10) UNIQUE NOT NULL)")
mydb.commit()
cursor.close()
mydb.close()

