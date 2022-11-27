"""
Autor: Roberto Rico Sandoval.
Fille: Menú desplegable.
Date: 15/ 11/ 2022

"""

from tkinter import *

class Textos:

    def __init__(self, root):

        self.root = root
        self.root.title("Hoja de textos")
        self.principal()

    def principal(self):

        barraMenu = Menu(self.root)         # Widget Menú.

        # Atributo tearoff= 0: Evita que los submenus se dispercen.
        menuArchivo = Menu(barraMenu, tearoff= 0)
        menuEditar = Menu(barraMenu, tearoff= 0)
        menuAyuda = Menu(barraMenu, tearoff= 0)
        menuEmergente = Menu(barraMenu, tearoff= 0)

        for i in ('Nuevo', 'Abrir', 'Guardar'):
            menuArchivo.add_command(label= i, command= self.llamada)

        for e in ('Copiar', 'Pegar'):
            menuEditar.add_command(label= e, command= self.llamada)

        menuAyuda.add_command(label= 'Acerca de: ', command= self.llamada)

        for a in ('Información', 'Cortar', 'Pegar'):
            menuEmergente.add_command(label= a, command= self.llamada)

        barraMenu.add_cascade(label= 'Archivo', menu = menuArchivo)
        barraMenu.add_cascade(label= 'Editar', menu = menuEditar)
        barraMenu.add_cascade(label= 'Ayuda', menu = menuAyuda)

        texto = Text()
        texto.pack()

        # Creación del menú en coordenadas x, y.
        texto.bind("<Button-3>", lambda evento: menuEmergente.post(evento.x_root, evento.y_root))

        self.root.config(menu = barraMenu)

    def llamada():
        print("Función no implementada.")

root = Tk()
hoja = Textos(root)
root.mainloop()

