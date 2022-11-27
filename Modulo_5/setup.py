"""
Autor: Roberto Rico Sandoval.
Fille: Ejecutable
Date: 15/ 11/ 2022

"""

from cx_Freeze import setup, Executable

setup(name= "Ejecutable de caja de texto",
      version= "0.1",
      description= "Conversión de archivo ejecutable python a ejecutable .exe",
      executables= [Executable("Diseño_de_menu_desplegable.py")])

