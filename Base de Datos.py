#BASE DE DATOS

import sqlite3

cedula1=input()
cedula2=input()
cedula3=input()
cedula4=input()

base1=sqlite3.connect('BASEDD')
cursor=base1.cursor()

cursor.execute('CREATE TABLE PERSONAS (ID INTEGER PRIMARY KEY AUTOINCREMENT, CEDULA VARCHAR(10))')

listaDatos=[(cedula1), (cedula2), (cedula3), (cedula4)]

cursor.executemany('INSERT INTO PERSONAS VALUES (NULL,?)', listaDatos)

print(listaDatos)

base1.commit()
base1.close()