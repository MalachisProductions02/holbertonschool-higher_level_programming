#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Recibe los argumentos: usuario, contraseña, base de datos
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Imprimir los resultados
    for row in cursor.fetchall():
        print(row)

    # Cerrar cursor y conexión
    cursor.close()
    db.close()
