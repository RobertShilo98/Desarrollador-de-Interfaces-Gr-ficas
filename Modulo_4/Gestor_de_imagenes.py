"""
Autor: Roberto Rico Sandoval.
Fille: Gestión de imagenes.
Date: 14/ 11/ 2022

"""

from tkinter import *
from PIL import ImageTk

root = Tk()
imagen = ImageTk.PhotoImage(file= 'C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/gato.jpg')

etiqueta = Label(compound= RIGHT, text= "Vive de tal modo que desees vivir otra vez.", fg= "blue", 
font= ("Times", "35", "italic"), image= imagen)

etiqueta.pack()

root.title("Mensaje uwu")
root.minsize(300, 350)
root.mainloop()

