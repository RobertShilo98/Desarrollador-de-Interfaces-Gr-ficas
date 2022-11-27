"""
Autor: Roberto Rico Sandoval.
Fille: Gestión de imagenes.
Date: 14/ 11/ 2022

"""

from tkinter import *
from PIL import Image

imagen = Image.open('C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/hulk.png')

# Creación de nuevo archivo png y cambio de formato en el archivo.
imagen.save('C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/hulk.png')

# Modificar escala de la imágen.
imagen.thumbnail((449, 449))

# Mostrar tamaño de imágen y formato de la imágen.
print(imagen.size, imagen.format)

# Mostrar en formato png a la imágen.
imagen.show()


