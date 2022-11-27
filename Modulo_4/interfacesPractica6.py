"""
Autor: Roberto Rico Sandoval
Fille: interfáz gráfica práctica 6
Dete: 21/ 10/ 2022
"""

from tkinter import *

class Colores():

    def __init__(self, master):
        self.master = master
        self.master.geometry("1020x1020")

        # Rectangulos.

        canvas = Canvas(width=300, height=210)
        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_rectangle(10, 10, 200, 200, width=5, fill='blue')

        canvas2 = Canvas(width=300, height=210)
        canvas2.pack(expand=YES, fill=BOTH)
        canvas2.create_rectangle(10, 10, 200, 200, width=5, fill='orange')

        canvas3 = Canvas(width=300, height=210)
        canvas3.pack(expand=YES, fill=BOTH)
        canvas3.create_rectangle(10, 10, 200, 200, width=5, fill='green')

        canvas4 = Canvas(width=300, height=210)
        canvas4.pack(expand=YES, fill=BOTH)
        canvas4.create_rectangle(10, 10, 200, 200, width=5, fill='pink')

        # Nombre de colores.

        self.colorName = Label(self.master, text="Azul", font=("arial", "16", "italic", "bold"), fg="black")
        self.colorName.place(x= "210", y= "100")

        self.colorName2 = Label(self.master, text="Naranja", font=("arial", "16", "italic", "bold"), fg="black")
        self.colorName2.place(x= "210", y= "330")

        self.colorName3 = Label(self.master, text="Verde", font=("arial", "16", "italic", "bold"), fg="black")
        self.colorName3.place(x= "210", y= "560")

        self.colorName4 = Label(self.master, text="Rosa", font=("arial", "16", "italic", "bold"), fg="black")
        self.colorName4.place(x= "210", y= "800")

        self.intro = Label(self.master, text="Selecciona un color preferido: ", font=("tahoma", "14", "bold"))
        self.intro.place(x= "10", y= "10")

        # Botones.

        self.select = Button(text="Select", bg="black", fg="white")
        self.select.place(x= "310", y= "100")

        self.select2 = Button(text="Select", bg="black", fg="white")
        self.select2.place(x= "310", y= "330")

        self.select3 = Button(text="Select", bg="black", fg="white")
        self.select3.place(x= "310", y= "560")

        self.select4 = Button(text="Select", bg="black", fg="white")
        self.select4.place(x= "310", y= "800")


root = Tk()

# Fondo Background.

root.title("Selección de colores")
root.config(bg="blue")          # color de fondo, background
root.config(cursor="pirate")    # tipo de cursor (arrow defecto)
root.config(relief="sunken")    # relieve del root 
root.config(bd=25)              # tamaño del borde en píxeles

gui = Colores(root)

root.mainloop()

