"""
Autor: Roberto Rico Sandoval.
Fille: Interacción con el canva.
Date: 26/ 11/ 2022

"""

from tkinter import *

class Dibujo:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Caballete")
        self.Principal()

    def Principal(self):
        
        # Widget canva, para dibujos y trazos.
        self.lienzo = Canvas(self.root, width= "1200", height= "500", bg= "white")

        self.boton = Button(self.root, text= "Dibujar", command= self.Dibujo)
        self.boton.place(x= 3500, y= 200, width=100, height=30)
        
        self.lienzo.create_window(200, 10, window= self.boton)
        
        self.lienzo.pack()
        
    def Dibujo(self):
        
        self.lienzo.bind("<B1-Motion>", 
                         lambda e: self.lienzo.create_oval(e.x -2,
                                                           e.y - 2,
                                                           e.x + 2,
                                                           e.y + 2,
                                                           fill= "blue"))
        
        
gui = Tk()
pintura = Dibujo(gui)
gui.mainloop()

