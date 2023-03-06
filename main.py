import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'root',
        port = '8889',
        database = 'poc_ai'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erreur de login ou de mot de passe")
        exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La DB n'existe pas")
        exit()
    else:
        print(err)
        exit()

cursor = db.cursor()

# SELECT
qry = "SELECT epj, raison_sociale FROM fd LIMIT 50"
cursor.execute(qry)
for epj, raison_sociale in cursor:
    print(epj, raison_sociale)

# INSERT
qry = "INSERT INTO fd(epj, raison_sociale) VALUES('384638468346', 'toto')"
cursor.execute(qry)
db.commit()
last_id = cursor.lastrowid

# UPDATE
qry = f"UPDATE fd SET raison_sociale = 'bob' WHERE id = {last_id}"
cursor.execute(qry)
db.commit()
affected_rows = cursor.rowcount

cursor.close()
db.close()