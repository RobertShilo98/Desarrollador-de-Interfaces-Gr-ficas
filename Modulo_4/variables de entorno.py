"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Variables de entorno en GUI
Date: 23/ 10/ 2022
"""

from tkinter import *

class App():

    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300")
        self.Principal()

    def Principal(self):
        self.Decimal = DoubleVar()   # Declaración de variables de entorno.
        self.String = StringVar()

        #self.Decimal = (0.0)        # Inicialización de variables.
        #self.String = ("")

        #self.Decimal.trace("w", self.Cambio)    # Localización de la variable declarada (Escrita).

        self.entrada = Entry(self.root, textvariable= self.Decimal)

        self.radio = Radiobutton(self.root, text= "redondear", variable= self.String, value="a", 
        command= self.Redondante)

        self.radio2 = Radiobutton(self.root, text= "truncar", variable= self.String, value= "b",
        command= self.Truncar)

        self.entrada.pack()
        self.radio.pack()
        self.radio2.pack()
        
    def Redondante(self):
        self.numRed = round(self.Decimal.get(), 2)
        print("Entrada redondeada:", self.numRed) 

    def Truncar(self):
        self.numRed2 = int(self.Decimal.get())
        print(f"\nEntrada truncada: {self.numRed2}")

    #def Cambio(self, *args):
        #print(f"\nLa entrada cambio a: {self.Decimal}")


root = Tk()
iniciar = App(root)
root.mainloop()

