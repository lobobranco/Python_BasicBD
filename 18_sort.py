import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cod3r",
    database="DaenerysQueimouFoiPouco"
)

mycursor = mydb.cursor()

# SELECT em ordem alfabética a partir do nome
sql = "SELECT * FROM contatos ORDER BY nome"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
