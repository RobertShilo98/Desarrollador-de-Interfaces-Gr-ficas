"""
Autor: Roberto Rico Sandoval.
Fille: Práctica 4.
Date: 19/ 10/ 2022
"""

from tkinter import *

class registro():

    def __init__(self, padre):

        self.padre = padre
        self.padre.geometry("800x650")
        
        self.etiqueta = Label(self.padre, text="Nombre: ", font=("arial", "14", "bold"), padx="10")
        self.etiqueta.place(x= 10 , y= 10)

        self.etiqueta2 = Label(self.padre, text="Dirección: ", font=("arial", "14", "bold"), padx="10")
        self.etiqueta2.place(x= 10 , y= 50)

        self.usuario = Entry(self.padre, show="")
        self.usuario.place(x= 115 , y= 15)
        self.usuario.bind("<Key-Return>", self.ejecuciones)

        self.direccion = Entry(self.padre, show="")
        self.direccion.place(x= 130 , y= 55)
        self.usuario.bind("<Key-Return>", self.ejecuciones)

        self.etiqueta2 = Label(self.padre, bg="#C8FAFF", padx="10", width="50", height="20")
        self.etiqueta2.pack(side="top", pady="150")

        self.boton = Button(self.padre, text="Cerrar", bg="black", fg="white", width="8", 
        command= self.padre.quit)
        self.boton.place(x= 720 , y= 610)

        self.boton2 = Button(self.padre, text="Ejecutar", bg="black", fg="white")
        self.boton2.place(x= 630 , y= 610)

    def ejecuciones(self):

        self.llamada = self.usuario.get()
        self.localizacion = self.direccion.get()
        self.usuario.delete(0,END)
        self.direccion.delete(0,END)

        self.etiqueta3 = Label(self.padre)

        self.etiqueta3.pack(side="top") 

raiz = Tk()

raiz.minsize(200,200)
raiz.title("Registro")

gui = registro(raiz)

raiz.mainloop()

