import sys
from helpers import absPath#Abrir archivos locales
from PySide6.QtSql import QSqlDatabase,QSqlQuery#componente

conexion=QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

#print(conexion.databaseName(),conexion.connectionName())

if not conexion.open():
    print("No se pude conectar a la base de datos")
    sys-exit(True)
else:
    print("Conexion abierta?",conexion.isOpen())

consulta=QSqlQuery()
consulta.exec("DROP TABLE IF EXISTS contactos")
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
""")
#print(conexion.tables())
nombre,empleo,email="Hector","Instructor","hector@ejemplo.com"
consulta.exec(f"""
    INSERT INTO contactos(nombre,empleo,email)
    VALUES('{nombre}','{empleo}','{email}')
""")

contactos=[
    ("Manuel","Desarrollador Web","manuel@ejemplo.com"),
    ("Lorena","Gestora de proyectos","lorena@ejemplo.com"),
    ("Javier","Analista de datos","javier@ejemplo.com"),
    ("Marta","Experta en Python","marta@ejemplo.com")
]
consulta.prepare("INSERT INTO contactos(nombre,empleo,email)VALUES(?,?,?)")

for nombre, empleo, email in contactos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(email)
    consulta.exec()

consulta.exec("SELECT nombre,empleo,email FROM contactos")
# if consulta.first():
#     print(consulta.value("nombre"),consulta.value("empleo"),consulta.value("email"))
while consulta.next():
    print(consulta.value("nombre"),consulta.value("empleo"),consulta.value("email"))

conexion.close()
print("Conexion cerrada?",not conexion.isOpen())