"""
Autor: Roberto jaime Rico Sandoval.
Fille: Palabras reservadas de Python.
Date: 16/ 10/ 2022
"""

from keyword import kwlist, iskeyword
 
# Impresión de Python.
print("Hola mundo!")

# Lista de palabras reservadas de Python.
print(f"\nLista de palabras reservadas: {kwlist}")

# Buscar una palabra reservada en especifico de Python.
print("\n¿Se encuentra como palabra reservada from? " + str(iskeyword("from")))

