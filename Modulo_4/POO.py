"""
Autor: Roberto Rico Sandoval.
Fille: POO.
Date: 19/ 10/ 2022
"""

class Menu():
    
    def __init__(self, cliente, platillo, bebida, boton):
        
        self.cliente = cliente
        self.platillo = platillo
        self.bebida = bebida
        self.boton = boton
        self.menuHoy = ["Pizza", "Burritos", "Papas a la francesa"]
        self.costoProducto = [89, 50, 30]
    
    def saludo(self):
        return print(f"\nHola, bienvenido: {self.cliente}")
        
    def menuDeHoy(self):
        
        print(f"\nEl menú de hoy es:\n")
        
        for comida in range(len(self.menuHoy)):
            print(f"** {self.menuHoy[comida]} $ {self.costoProducto[comida]}")
            
    def eleccion(self):
        
        print(f"\nElige que comerás hoy:\nPizza (Botón 1)\nPizza (Botón )\nPizza (Botón 3)")
        
        while self.boton <= 0 or self.boton > 3:
            print(f"\nOpción no encontrada: Botón {self.boton}. Vuelve a intenatarlo.")
            break
        
        if self.boton == 1:
            print(f"\n1 {self.menuHoy[self.boton]} Pagá ${self.costoProducto[self.boton]}")
            
        elif self.boton == 2:
            print(f"\n1 {self.menuHoy[self.boton]} Pagá ${self.costoProducto[self.boton]}")
            
        elif self.boton == 3:
            print(f"\n1 {self.menuHoy[self.boton]} Pagá ${self.costoProducto[self.boton]}")
        
persona = Menu("Roberto", "Pizza", "Agua de sabor", 2)

print(persona.saludo())
print(persona.menuDeHoy())
print(persona.eleccion())

