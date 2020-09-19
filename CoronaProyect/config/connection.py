import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sp463950",
    database="corona"
    )
except:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sp463950"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE corona")
    mycursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), contrasenia VARCHAR(255))")
    mycursor.execute("CREATE TABLE actividad (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), descripcion VARCHAR(255))")
finally:
    mycursor.execute("CREATE TABLE usuario (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), contrasenia VARCHAR(255))")

print(mydb)