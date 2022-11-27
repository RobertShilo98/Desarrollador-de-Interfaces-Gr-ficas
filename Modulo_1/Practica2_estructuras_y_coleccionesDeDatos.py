"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Colecciones de datos y estructuras de control.
Date: 17/ 10/ 2022
"""

""" Declaración de EnCoding (Codificación) """
# -*- coding: <utf-8> -*-

""" Caso 1 """
# Tupla.
alumnos = ("Ana", "Beto", "Claudia")

# Lista.
notas = [6.7, 8.2, 9.6]

# Diccionarios.
calificaciones = {
    
    "Ana" : 6.7,
    "Beto" : 8.2,
    "Claudia" : 9.6
    
    }

""" Caso 2 """
# Iteración en bucle while.
calificaciones2 = {}
i = 0

while i < len(alumnos):
    calificaciones2[i] = notas[i]
    i += 1
    
print(calificaciones2)


# Iteración en bucle for.
calificaciones2 = {}
i = 0

for i in range(len(alumnos)):
    calificaciones2[i] = notas[i]
    
print(calificaciones2)


""" Caso 3 """

entrada = ["Sopa", "Crema de verduras", "Spaguetti"]

platipllo_principal = ["Res", "Pollo", "Pescado"]

postre = ["Pastel", "Gelatina", "Flan"]

menu = {}


for elemento in range(3):
    
    menu["Opción " + str(elemento)] = entrada[elemento] + ", " + platipllo_principal[elemento] + ", " + postre[elemento]
    
print("\nEl menú de hoy: \n")

for clave, valor in menu.items():
    print(clave)
    print(valor)
    print("")

