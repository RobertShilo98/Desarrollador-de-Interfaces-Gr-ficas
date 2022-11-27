"""
Autor: Roberto Rico Sandoval.
Fille: Diseño de interaces en libreria TKinter.
Date: 19/ 10/ 2022
"""

from tkinter import *

"""

    *** DOCUMENTACIÓN TKINTER ***

interfazRaíz.minsize(Base, Altura) = Definición miníma del tamaño de la ventana de la interfaz.
interfazRaíz.maxsize(Base, Altura) = Definición máxima del tamaño de la ventana de la interfaz.
interfazRaíz.geometry(Base, Altura) = Definición predeterminada de la ventana de la interfaz.
interfazRaíz.title(Titulo de la vetnana de la interfaz actual).

widget.pack(side= "Posición del widget en la interfaz gráfica.", padx= "Espaciado entre widgets en el eje x",
pady= "Espaciado entre widgets en el eje y".

"""
class Interfaz():

    def __init__(self, master):
        self.master = master
        self.master.geometry("900x300")
        self.crearWidget()

    def crearWidget(self):
        self.etiqueta = Label(self.master, cursor="pencil", fg="red", bg="white", text=("Texo de la etiqueta"),
        font=("Times","12","italic"))
        self.etiqueta.pack(side= "left")

        # Creación de Widget botón.
        self.boton = Button(self.master, text="Cerrar ventana", command= self.master.quit)
        self.boton.pack(side= "bottom", padx= "20", pady="80")

        self.etiqueta2 = Label(self.master, text="Hola mundo papus :v")
        self.etiqueta2.pack()

root = Tk()

#root.minsize(300,300)
#root.maxsize(900,900)
#root.geometry("900x300")
root.title("Mi primera interfaz gráfica")

# Creación de objeto con parámetro de interfaz gráfica.
gui = Interfaz(root)

root.mainloop()

