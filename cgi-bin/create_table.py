import mysql.connector



db = mysql.connector.connect(

    host = "localhost",
    user = user,
    password = password,
    database = "tarea2"
)

cursor = db.cursor()