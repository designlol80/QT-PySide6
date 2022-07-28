import json
from helpers import absPath

datos=[]#apartir de una lista

datos.append({#Diccionario
    "nombre":"Héctor",
    "empleo":"Instructor",
    "email":"hektor@ejemplo.com"
})
#lista con Tuplas
contactos=[
    ("Manuel","Desarrollador Web","manuel@ejemplo.com"),
    ("Lorena","Gestora de proyectos","lorena@ejemplo.com"),
    ("Javier","Analista de datos","javier@ejemplo.com"),
    ("Marta","Experta en Python","marta@ejemplo.com")
]

for nombre,empleo,email in contactos:
    datos.append({#Diccionario
        "nombre":nombre,
        "empleo":empleo,
        "email":email
    })

#guardar registro en un fichero json
with open(absPath("contactos.json"),"w") as fichero:#fichero abierto destro de este bloque de codigo
    json.dump(datos,fichero)#para exportar

datos=None

#mostrar en pantalla
with open(absPath("contactos,json")) as fichero:#fichero abierto destro de este bloque de codigo
    datos=json.load(fichero)#para abrir
    for contacto in datos:
        print(contacto["nombre"],contacto["empleo"],contacto["email"]) 
