"""
Autor: Roberto Rico Sandoval.
Fille: Práctica 8.
Date: 25/ 11/ 2022

"""

from tkinter import *

class juegoCoche:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica_8")
        
        self.limite = 600
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        
        self.k = []
        
        self.widgets()
        self.muros()
    
    def widgets(self):
        self.lienzo = Canvas(self.root, width= self.limite, height= self.limite, bg= "gray")
        
        
        self.boton1 = Button(self.root, text= "Izquierda", bg= "black", fg= "white", 
                             command = lambda: self.mover('a'))
        
        self.boton1.place(x= "20", y= "550")
        
        self.boton2 = Button(self.root, text= "Derecha", bg= "black", fg= "white",
                             command = lambda: self.mover('b'))
        
        self.boton2.place(x= "120", y= "550")
        
        self.boton3 = Button(self.root, text= "Velocidad", bg= "black", fg= "white")
        self.boton3.place(x= "220", y= "550")
        
        self.muro1 = self.lienzo.create_rectangle(1, 1, 250, 30, fill= "brown")
        self.muro2 = self.lienzo.create_rectangle(350, 300, 600, 330, fill= "brown")
        
        self.carro = self.lienzo.create_rectangle(360, 550, 330, 500, fill= "blue")
        
        self.lienzo.pack()
    
    def muros(self):
        
        self.posicion = self.lienzo.create_rectangle(1, 1, 250, 30, fill= "brown")
        
        self.d = 500
        
        if self.d <= 500:
            
            a,b,c,self.d = 0, 0, 100, 20 
            a2,b2,c2,self.d2 = 100, 160, 200, 180 
            self.lienzo.coords(a, b + 5, c, self.d + 5) 
            self.lienzo.coords(a2, b2 + 5, c2, self.d2 + 5) 

        
        self.x1,self.y1,self.x2,self.y2 = self.lienzo.coords(self.posicion) 
        
        self.juegoPerdido()
        self.root.after(50, self.muros)
        
    
    def juegoPerdido(self):
        if  self.d >= self.y1 and self.k =='a': 
            print('Chocaste izquierda') 
 
        elif self.d2 > self.y1 and (self.k =='b' or self.k == ''): 
            print('Chocaste derecha') 
    
    
    def mover(self, k):
        self.k = k 
        self.x1,self.y1,self.x2,self.y2 = self.lienzo.coords(self.posicion)
        
        if self.k == 'a': 
            self.lienzo.coords(self.posicion, self.x1-100, self.y1, self.x2-100, self.y2)
        
        elif self.k == 'b': 
            self.lienzo.coords(self.posicion, self.x1+100, self.y1, self.x2+100, self.y2)
            
        self.juegoPerdido()


gui = Tk()
gui.minsize(600, 600)
gui.maxsize(600, 600)

raiz = juegoCoche(gui)
gui.mainloop()

