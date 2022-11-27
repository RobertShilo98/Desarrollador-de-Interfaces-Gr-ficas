"""
Autor: Roberto Rico Sandoval.
Fille: Creación de ejecutable.
Date: 23/ 11/ 2022
"""

from cx_Freeze import setup, Executable

setup(name= "Creación de ejecutable.",
      version= "0.1",
      description= "Creación de ejecutable.",
      executables= [Executable("Practica4.py")])

