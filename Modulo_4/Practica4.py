"""
Autor: Roberto Rico Sandoval.
Fille: Práctica 4.
Date: 19/ 10/ 2022
"""

from tkinter import *
from PIL import ImageTk

class interfazMenu():

    def __init__(self, root):

        self.root = root
        self.root.geometry("900x300")

        self.lPlatillo = [["pollo", 20], ["pescado", 30], ["res", 45], ["hamburguesa", 40]]
        self.lBebida = [["agua", 5], ["Café", 8], ["jugo", 10], ["refresco", 13]]
        
        self.orden = []
        self.costo = ()
        
        self.imprimirMenu()

    # Impresión de menú.
    def imprimirMenu(self):
        
        # Creación de marco, para los elementos de la GUI.
        self.marco = Frame(self.root)
        self.marco.pack()
        
        # Mostrar im+agen en la interfaz gráfica.
        imagen = ImageTk.PhotoImage(file= 'C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/imagenes/sopaMaruchan.png')
        
        preImagen = Label(self.root, image= imagen)
        preImagen.pack()
        preImagen.image = imagen
        
        barradeMenu = Menu(self.root)
        barradeMenu.add_command(label= "Nueva orden", command= self.nuevaOrden)
        
        self.root.config(menu= barradeMenu)
        
        # Creación de menú.
        self.etiqueta = Label(self.marco, text="Cliente", font=("times","16","italic"))
        self.etiqueta.grid(row=0, column=0)

        self.entrada = Entry(self.marco, show="", width=25)
        self.entrada.grid(row=0, column=1, sticky="ew")

        self.etiqueta2 = Label(self.marco, text="Concepto", font=("times","16","italic"))
        self.etiqueta2.grid(row=1, column=1, sticky="ew")

        self.etiqueta3 = Label(self.marco, text="Costo", font=("times","16","italic"))
        self.etiqueta3.grid(row=1, column=2, sticky="ew")

        self.etiqueta4 = Label(self.marco, text="Platillo", font=("times","16","italic"))
        self.etiqueta4.grid()

        self.casillas = []
        self.casillas2 = []

        # Acomodo de elementos en la GUI.
        k = 0

        for elemento in self.lPlatillo:
            self.casillas.append(Button(self.marco, text= str(elemento[0])))
            self.casillas2.append(Label(self.marco, text= str(elemento[1])))

            self.casillas[k].grid(row = k+2, column= 1, sticky="ew")
            self.casillas2[k].grid(row = k+2, column= 2, sticky="ew")

            k += 1
            
            command = lambda e = k: self.cuenta('a',e)

        self.etiqueta5 = Label(self.marco, text="Bebida", font=("times","16","italic"))
        self.etiqueta5.grid()

        for elemento in self.lBebida:
            self.casillas.append(Button(self.marco, text= str(elemento[0])))
            self.casillas2.append(Label(self.marco, text= str(elemento[1])))

            self.casillas[k].grid(row = k+2, column= 1, sticky="ew")
            self.casillas2[k].grid(row = k+2, column= 2, sticky="ew")

            k += 1
            
            command = lambda e = k: self.cuenta('b',e)

        self.mostrarCuenta = Label(self.root, font= ("Times", "15", "italic"))
        self.mostrarCuenta.pack()
        
    
    # Creación de nuevas ordenes.
    def nuevaOrden(self):
        
        self.orden = []
        self.costo = ()
        
        self.entrada = Entry(self.marco, show="", width=25)
        self.entrada.grid(row=0, column=1, sticky="ew")
        
    
    # Mostrar cuenta.    
    def cuenta(self, key, e):
        
        if key == 'a':
            self.orden.append(self.lPlatillo[e][0])
            self.costo += self.lPlatillo[e][1]
        
        elif key == 'b':
            self.orden.append(self.lBebida[e - len(self.lPlatillo)][0])
            self.costo += self.lBebida[e - len(self.lPlatillo)[1]]


paginaUno = Tk()

paginaUno.title("Bienvenido al restaurante")

paginaUno.minsize(400,400)
paginaUno.maxsize(1200,1200)

miMenu = interfazMenu(paginaUno)

paginaUno.mainloop()

