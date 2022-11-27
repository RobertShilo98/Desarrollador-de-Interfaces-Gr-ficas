"""
Autor: Roberto Rico Sandoval.
Fille: Dibujo en Canva.
Date: 25/ 11/ 2022

"""

from tkinter import *

class Dibujo:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Caballete")
        self.Principal()

    def Principal(self):
        
        # Widget canva, para dibujos y trazos.
        lienzo = Canvas(self.root, width= "400", height= "150", bg= "white")
        
        # Creación de líneas simples.
        lienzo.create_line(50, 100, 350, 100, fill= "red")
        
        # Creación de rectangulos.
        lienzo.create_rectangle(0, 25, 50, 75, fill= "blue")
        
        # Creación de figuras complejas poligonales.
        lienzo.create_polygon(120, 50, 50, 75, 350, 75, fill= "green")
        
        # Intregración de textos.
        lienzo.create_text(100, 30, text= "Mi lienzo")
        
        # Creación de arcos o medio circulos.
        xy = 300, 0, 350, 100
        
        lienzo.create_arc(xy, start = 0, extent= 230, fill= "pink")
        lienzo.create_arc(xy, start = 230, extent= 90, fill= "brown")

        # Reeposicionamiento de figuras geométricas.
        posicion = lienzo.create_line(50, 100, 350, 100, fill= "red")
        x1, y1, x2, y2 = lienzo.coords(posicion)
        
        lienzo.coords(x1 + 5, y1 + 5, x2 + 15, y2 + 15)
        lienzo.pack()
        
        
gui = Tk()
pintura = Dibujo(gui)
gui.mainloop()

