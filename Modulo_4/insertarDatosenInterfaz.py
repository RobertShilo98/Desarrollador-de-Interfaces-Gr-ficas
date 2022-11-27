"""
Autor: Roberto Rico Sandoval.
Fille: Insertar datos en TKinter.
Date: 19/ 10/ 2022
"""

from tkinter import *

"""
    *** DOCUMENTACIÓN TKINTER ***

Frame(vetanaRaíz, caracteristícas.): Marco o mérgen contenedor de widgets.
Entry(vetanaRaíz, caracteristícas.): Caja de texto o input en la interfáz gráfica.

show="": Muestra algún texto predeterminado sobre la caja de texto.

widget.bind(comando, método o atributo): Controlador de eventos en la interfáz gráfica.
<Key-Return>: Retorna un valor proporcionado por un evento controlado por.bind

widget.get(): Obtiene el contenido escrito en un widget.

self.widget.delete(0,END): Comando para permitir una nueva entrada de valores en un widget.

self.widget['Caracteristíca'] = Valor: Incluir una nueva caracteristíca al widget.

"""
class inicioDeSesion():

    def __init__(self, master):
        
        self.master = master

        self.marcoIngreso()
        self.marcoSalida()
        self.master.geometry("600x300")

    def marcoIngreso(self):
        self.marco = Frame(self.master, pady= "20")
        self.marco.pack()

        self.etiqueta = Label(self.marco, text= "Contraseña")
        self.etiqueta.pack(side= "left")

        self.contraseña = Entry(self.marco, show="*")
        self.contraseña.pack(side= "left")
        self.contraseña.bind("<Key-Return>", self.mostrarSalida)

    def marcoSalida(self):
        self.marco2 = Frame(self.master, pady= "20")
        
        self.etiqueta2 = Label(self.marco2)
        self.etiqueta2.pack()

    def mostrarSalida(self, event):
        self.contenido = self.contraseña.get()
        self.contraseña.delete(0,END)

        if self.contenido == "Carlos":
            self.etiqueta2['text'] = "Contraseña Correcta"

        else:
            self.etiqueta2['text'] = "Contraseña Incorrecta"

        self.marco2.pack()

root = Tk()

gui = inicioDeSesion(root)

root.mainloop()

