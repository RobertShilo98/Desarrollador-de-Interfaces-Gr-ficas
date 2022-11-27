"""
Autor: Roberto Rico Sandoval.
Fille: Formularios en TKinter.
Date: 12/ 11/ 2022

"""

from tkinter import *

class convertorDeTemperatura:


    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de temperatura")
        self.root.geometry("900x300")
        self.inicializar()


    def inicializar(self):
        self.grados = DoubleVar()
        self.grados2 = DoubleVar()

        self.escala = StringVar()
        self.escala.set("c")

        self.escala2 = StringVar()
        self.escala2.set("c")

        self.marco = Frame(self.root)
        self.marco2 = Frame(self.root)

        # Primer entrada de datos.
        self.entrada = Entry(self.marco, textvariable= self.grados)

        self.radio = Radiobutton(self.marco, text="Celsius", variable= self.escala, value="c",
        command= lambda: self.convertir(1))

        self.radio2 = Radiobutton(self.marco, text="Fahrenheit", variable= self.escala, value="f",
        command= lambda: self.convertir(1))

        self.radio3 = Radiobutton(self.marco, text="Kelvin", variable= self.escala, value="k",
        command= lambda: self.convertir(1))

        # Segunda entrada de datos.
        self.entrada2 = Entry(self.marco2, textvariable= self.grados2)

        self.radio4 = Radiobutton(self.marco2, text="Celsius", variable= self.escala2, value="c",
        command= lambda: self.convertir(0))

        self.radio5 = Radiobutton(self.marco2, text="Fahrenheit", variable= self.escala2, value="f",
        command= lambda: self.convertir(0))

        self.radio6 = Radiobutton(self.marco2, text="Kelvin", variable= self.escala2, value="k",
        command= lambda: self.convertir(0))

        # Mostrar widgets hechos marcos.
        self.marco.pack(side= "left")
        self.marco2.pack(side= "right")

        self.entrada.pack()
        self.radio.pack()
        self.radio2.pack()
        self.radio3.pack()

        self.entrada2.pack()
        self.radio4.pack()
        self.radio5.pack()
        self.radio6.pack()


    def convertir(self, key):
        self.key = key

        if self.key == 0:
            self.var = self.grados.get()
            self.tupEscala = (self.escala.get(), self.escala2.get())
            self.configurar = self.grados2

        elif self.key == 1:
            self.var = self.grados2.get()
            self.tupEscala = (self.escala2.get(), self.escala2.get())
            self.configurar = self.grados

        self.diccForm = {
            ("f","c"): 5*(self.var*32) /9,
            ("k","c"): self.var * 273.75,
            ("c","f"): 9*(self.var/5) + 32,
            ("k","f"): 9*(self.var/273.75) /5 + 32,
            ("c","k"): self.var + 273.15,
            ("f","k"): 5*(self.var - 32) /9 + 273.75,
            ("c","c"): self.var,
            ("f","f"): self.var,
            ("k","k"): self.var,
        }

        self.configurar.set(round(self.diccForm[self.tupEscala],2))

root = Tk()
iniciar = convertorDeTemperatura(root)

root.mainloop()

