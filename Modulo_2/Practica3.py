"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Práctica 3.
Date: 18/ 10/ 2022
"""

# *** Primer ejercicio ***.

lPlatillo = [["      Pollo a la crema   ", 20], ["      Pescado a la plancha   ", 30]]

lBebida = [["      Agua de sabor   ", 5], ["      Jugo de fruta o verdura   ", 10]]

# 10 espacios entre columnas.
arg = ["          Concepto   ", "          Costo   "]

# 6 espacios entre filas.
menu = ["Platillos:      ", "Bebidas:      "]

def imprimirMenu():
    
    print(arg[0] + arg[1])
    print(f"\n{menu[0]}\n")
    
    for i in range(2):
        print(lPlatillo[i])
        
    print(f"\n\n{menu[1]}\n")
    
    for e in range(2):
        print(lBebida[e])

# *** Segundo ejercicio ***.

def generarCombinaciones():
    
    combinaciones = {}
    contador = 1
    init = 0
    
    for elemento in range(2):
        combinaciones["Opción " + str(contador) + ":"] = [lPlatillo[init][init], lBebida[elemento][0]]
        contador += 1

    for inter in range(2):

        if contador >= 2:
            
            init = 1
            combinaciones["Opción " + str(contador) + ":"] = [lPlatillo[init][0], lBebida[inter][0]]
            contador += 1
    
    return print(combinaciones)

