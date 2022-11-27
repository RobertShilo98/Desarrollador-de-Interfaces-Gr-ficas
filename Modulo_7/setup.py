"""
Autor: Roberto Rico Sandoval.
Fille: Conversión de ejecutable (El juego del gato).
Date: 25/ 11/ 2022

"""

from cx_Freeze import setup, Executable

setup(name= "Creación de ejecutable del juego del gato.",
      version= "0.1",
      description= "",
      executables= [Executable("GUI_juego_del_gato.py")])

