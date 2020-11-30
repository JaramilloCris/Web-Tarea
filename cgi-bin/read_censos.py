#!C:\Users\groso\AppData\Local\Programs\Python\Python37\python.exe
# -*- coding: utf-8 -*-

import save_db as sd
import pymysql
import json

"""
Modulo que leera la cantidad de censos realizados por fechas, para la realizacion del grafico
"""

print("Content-type: text/html; charset=UTF-8")
print("")

# conexion a base de datos
db = sd.AnimalitosDb("root", "")

try:

    messages = db.read_censos()
    msg = {}
    mascotas = []
    cantidad = []
    k = 0
    for i in messages:

        comuna = messages[k][1]
        arr = [messages[k][0], messages[k][2], messages[k][3], messages[k][4], messages[k][5], messages[k][6], messages[k][7], messages[k][8]]
        if comuna in msg:

            msg[comuna].append(arr)

        else:
            msg[comuna] = [arr]

        k += 1

    msg[0] = mascotas
    msg[1] = cantidad
    print(json.dumps(msg))
except pymysql.Error as e:
    mensaje = 'Error con base de datos: {0} {1} '.format(e.args[0], e.args[1])

