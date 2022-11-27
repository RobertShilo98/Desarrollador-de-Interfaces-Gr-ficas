"""
Autor: Roberto Rico Sandoval.
Fille: Cajas de texto.
Date: 15/ 11/ 2022

"""

from tkinter import *
from tkinter import messagebox      # Librería para ventanas emergentes en Python / TKinter.

class Emergente:

    def __init__(self, master):

        self.master = master
        self.master.title("Mensajes emergentes")
        self.master.geometry("500x500")

        self.Principal()

    def Principal(self):
        self.botonInstalar = Button(text= "Instalar", command= self.Cancelar)
        self.botonInstalar.pack()

    def Cancelar(self):
        
        # Informar con cuadro emergente una pregunta (SI / NO)
        if messagebox.askyesno('ADVERTENCIA', '¿Deseas continuar?'):

            # Sí, se preciona el botón sí. Se arroja una ventana emergente informativa.
            messagebox.showinfo('Gracias', 'La instalación continuara.')

        else:
            # Sí, se preciona el botón no. Se arroja una ventana emergente de advertencia.
            messagebox.showwarning('Lo sentimos', 'Instalación cancelada.')


master = Tk()
mensajesEmergentes = Emergente(master)
master.mainloop()

