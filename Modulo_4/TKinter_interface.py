"""
Autor: Roberto Rico Sandoval.
Fille: Diseño de interaces en libreria TKinter.
Date: 19/ 10/ 2022
"""

from tkinter import *

# Creación de la ventana raíz.
principal = Tk()

"""
    *** DOCUMENTACIÓN TKINTER ***

Label = Creación de etiqueta (Ventana raíz, caracteristícas del widget).
Button = Creación de Botón didáctico (Ventana raíz)

cursor= Caracteristicas del cursor sobre la interfaz grágica.
fg= Color del texto.
bg = Color del fondo de la etiqueta.
text= Texto que tendrá la etiqueta.
font= (Tipo de fuente de letra, tamaño de la letra, efecto especial sobre la letra).

command= principal.quit (Para cerrar la ventana, una vez, se haga click sobre un botón)
ventanaRaiz.mainloop() = Muestra a la interfaz en una ventana emergente.
widget.pack() = Muestra a las caracteristicas del widgt sobre la interfaz gráfica.

"""
# Creación de Widget label / etiqueta.

etiqueta = Label(principal, cursor="pencil", fg="red", bg="white", text=("Texo de la etiqueta"),
font=("Times","12","italic"))

# Creación de Widget botón.
boton = Button(principal, text="Cerrar ventana", command= principal.quit)

# Visualización de widgets en la ventana(Interfaz).
etiqueta.pack()
boton.pack()

# Código para viasulizar la ventana raíz.
principal.mainloop()

