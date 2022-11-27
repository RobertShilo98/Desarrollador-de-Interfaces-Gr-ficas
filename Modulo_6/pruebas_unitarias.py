"""
Autor: Roberto Rico Sandoval.
Fille: Pruebas unitarias.
Date: 25/ 11/ 2022

"""

import doctest

def calculo_primo(nume):
    
    # Bloque de __main__
    """
    >>> calculo_primo(0)
    El número: 0 NO es primo.
    >>> calculo_primo(1)
    El número: 1 NO es primo.
    >>> calculo_primo(2)
    El número: 2 SI es primo.
    >>> calculo_primo(97)
    El número: 97 SI es primo.
    >>> calculo_primo(95)
    El número: 95 NO es primo. 
    """
    
    if nume < 2:
        print("El número: " + str(nume) + " NO es primo.")
        
    elif nume == 2:
        print("El número: " + str(nume) + " SI es primo.")
        
    else:
        for i in range(2, nume):
            
            if nume %i == 0:
                print("El número: " + str(nume) + " NO es primo.")
                break
        
        else:
            print("El número: " + str(nume) + " SI es primo.")
    
    # Bloque testeador de errores.        
    if __name__ == "__main__":
        doctest.testmod()


print(calculo_primo(3))

