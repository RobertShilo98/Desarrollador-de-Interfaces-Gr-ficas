"""
Autor: Roberto Rico Sandoval.
Fille: Interfaz del juego gato ###.
Date: 25/ 11/ 2022

"""

from tkinter import *
from PIL import ImageTk

class Gato:
    
    
    def __init__(self, root):
        self.root = root
        self.contador = 0
         
        self.inicio()
        
    def inicio(self):
        self.root.title("Inicio / Juego del gato")
        self.root.geometry("453x580")
        
        self.marcoPrincipal = Frame(self.root)
        self.marcoPrincipal.grid()
        
        # Imágen tematica con el juego.
        imagenGato = ImageTk.PhotoImage(
            file= "C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/imagenes/gato.png")

        bienvenida = Label(self.marcoPrincipal, image= imagenGato)
        bienvenida.grid(row= 0, column= 0)
        bienvenida.image = imagenGato
        
        # Botones de acción de la pantalla inicio.
        nuevaPartida = Button(self.marcoPrincipal, text= "Nueva partida", font= ("Arial", "15", "italic"),
                              fg= "black", bg= "floral white", command= lambda: self.cambiarPantalla('a'),
                              anchor= ('w'))
        
        nuevaPartida.grid(row= 1, column= 0, sticky= 'ew')
        
        records = Button(self.marcoPrincipal, text= "Records", font= ("Arial", "15", "italic"),
                              fg= "black", bg= "floral white", anchor= ('w'), command= self.btnRecords)
        
        records.grid(row= 2, column= 0, sticky= 'ew')
        
        salir = Button(self.marcoPrincipal, text= "Salir", font= ("Arial", "15", "italic"),
                              fg= "white", bg= "OrangeRed2", anchor= ('w'), command= self.root.quit)
        
        salir.grid(row= 3, column= 0, sticky= 'ew')
     
        
    def datos(self):
        self.root.title("Jugadores")
        self.root.geometry("600x200")
        
        self.player1 = ""
        self.player2 = ""
        
        self.marcoNombres = Frame(self.root)
        self.marcoNombres.grid()
        
        # Etiquetas de jugadores.
        juador1 = Label(self.marcoNombres, width= 40, font= ("Times", "12", "italic"), text= "Jugador 1", 
                        fg= "blue", bg= "white")
        juador1.grid(row= 0, column= 0)
        
        juador2 = Label(self.marcoNombres, width= 40, font= ("Times", "12", "italic"), text= "Jugador 2", 
                        fg= "blue", bg= "white")
        juador2.grid(row= 1, column= 0)
        
        # Nombres de los jugadores.
        self.nombre1 = Entry(self.marcoNombres, width= 40, textvariable= self.player1)
        self.nombre1.grid(row= 0, column= 1, sticky= 'nsew')
        
        self.nombre2 = Entry(self.marcoNombres, width= 40, textvariable= self.player2)
        self.nombre2.grid(row= 1, column= 1, sticky= 'nsew') 

        # Botones de acción de la página de datos.
        comenzar = Button(self.marcoNombres, text= "Comenzar", height= 2, font= ("Arial", "13", "bold"),
                          fg= "white", bg= "black", command= lambda: self.cambiarPantalla('b'), anchor= 'w')
        comenzar.grid(row= 2, column= 0, sticky= 'ew', columnspan= 2)
        
        regresar = Button(self.marcoNombres, text= "Regresar", height= 2, font= ("Arial", "13", "bold"),
                          fg= "white", bg= "black", anchor= 'w', command= lambda: self.cambiarPantalla('c'))
        regresar.grid(row= 3, column= 0, sticky= 'ew', columnspan= 2)
        
        salir = Button(self.marcoNombres, text= "Salir", height= 2, font= ("Arial", "13", "bold"),
                          fg= "white", bg= "OrangeRed3", command= self.root.quit, anchor= 'w')
        salir.grid(row= 4, column= 0, sticky= 'ew', columnspan= 2)
        
        
    def partida(self):
        self.root.title("Partida")
        self.root.geometry("910x740")

        self.marcoPartida = Frame(self.root)
        self.marcoPartida.grid()
        
        # Mostrar cuadricula.
        self.casillas = []
        k = 0
        
        for i in range(3):
            for j in range(3):
                self.casillas.append(Button(self.marcoPartida, font= ("Times", "10", "italic"),
                                            fg= "black", bg= "white smoke", bd= 1, width= 42, height= 3,
                                            command= lambda e = k : self.mostrarCasilla(e)))
                self.casillas[k].grid(row= i, column= j)
                
                k += 1
        
        jugarOtraVez = Button(self.marcoPartida, text= "Jugar otra vez", height= 3, width= 1, 
                              font= ("Arial", "13", "bold"), fg= "white", bg= "black", 
                              command= lambda: self.cambiarPantalla('d'), anchor= 'w')
        
        jugarOtraVez.grid(row= 4, column= 0, sticky= 'ew', columnspan= 3)
        
        salir = Button(self.marcoPartida, text= "Salir", height= 3, width= 1, 
                       font= ("Arial", "13", "bold"), fg= "white", bg= "OrangeRed3", 
                       command= self.root.quit, anchor= 'w')
        
        salir.grid(row= 5, column= 0, sticky= 'ew', columnspan= 3)
        
        # Imágen tematica con el juego.
        imagenGato = ImageTk.PhotoImage(
            file= "C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/imagenes/gato.png")

        bienvenida = Label(self.marcoPartida, image= imagenGato)
        bienvenida.grid(row= 6, column= 0, sticky= 'ew', columnspan= 3)
        bienvenida.image = imagenGato
    
    
    def mostrarCasilla(self, e):
        
        """
        Mostrar cuando el jugador marque con X u O. 
        """
        
        self.contador += 1
            
        if self.contador % 2 == 1:
            self.casillas[e].config(text= "X", command= lambda: None)
        
        elif self.contador % 2 == 0:
            self.casillas[e].config(text= "O", command= lambda: None)
            
        # Cuando haya un ganador.
        self.ganador()
        
    
    def ganador(self):
        
        from tkinter import messagebox
        
        # Horizontales.
        texto0 = self.casillas[0]['text'] + self.casillas[1]['text'] + self.casillas[2]['text']
        texto1 = self.casillas[3]['text'] + self.casillas[4]['text'] + self.casillas[5]['text']
        texto2 = self.casillas[6]['text'] + self.casillas[7]['text'] + self.casillas[8]['text']
        
        # Verticales.
        texto3 = self.casillas[0]['text'] + self.casillas[3]['text'] + self.casillas[6]['text']
        texto4 = self.casillas[1]['text'] + self.casillas[4]['text'] + self.casillas[7]['text']
        texto5 = self.casillas[2]['text'] + self.casillas[5]['text'] + self.casillas[8]['text']
        
        # Diagonales.
        texto6 = self.casillas[0]['text'] + self.casillas[4]['text'] + self.casillas[8]['text']
        texto7 = self.casillas[2]['text'] + self.casillas[4]['text'] + self.casillas[6]['text']
        
        # Configuraciones.
        listaTextos = [texto0, texto1, texto2, texto3, texto4, texto5, texto6, texto7]
        
        # Sí alguien a ganado.
        if 'XXX' in listaTextos:
            text= 'Ganó ' + self.nombre1.get() + "\n"
            messagebox.showinfo('Muy bien.', 'Haz ganado. ' + self.nombre1.get())
            
            # Actualizar records y contador.
            self.restaurarRecords(text)
            self.contador = 0
            
        elif 'OOO' in listaTextos:
            text= 'Ganó ' + self.nombre2.get() + "\n"
            messagebox.showinfo('Muy bien.', 'Haz ganado. ' + self.nombre2.get())
            
            # Actualizar records y contador.
            self.restaurarRecords(text)
            self.contador = 0
                
        else:
            cadena = ""
            
            for i in range(8):
                cadena += listaTextos[i]
                
            if len(cadena) == 24:
                text= 'Empate' + '\n'
                messagebox.showinfo('Bien,', 'Han empatado.')
                
                # Actualizar records y contador.
                self.restaurarRecords(text)
                self.contador = 0
             
                
    def restaurarRecords(self, text):
        
        """ 
        Registrar los datos de la partida en archivo .txt
        """
        
        with open("C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/Modulo_7/Records/datos.txt", 
                  "a") as f:
            f.write(text)
            
            
    def btnRecords(self):
        
        """ 
        Abrir el archivo que contiene el registro de los records.
        """
        
        from os import startfile
        startfile("C:/Users/Ruperto/Documents/Diseño de Interfaces graficas/Modulo_7/Records/datos.txt")
        
    
    def cambiarPantalla(self, valor):
        
        """ 
        Cambio de ventana, apartir de la interacción con botenes (Widgets) y el valor de carácteres (a, b, c, d)
        """
        
        if valor == 'a':
            self.marcoPrincipal.grid_remove()
            self.datos()
            
        elif valor == 'b':
            text = self.nombre1.get() + " vs " +  self.nombre2.get() + "\n"
            self.restaurarRecords(text)
            
            self.marcoNombres.grid_remove()
            self.partida()
            
        elif valor == 'c':
            self.marcoNombres.grid_remove()
            self.inicio()
            
        elif valor == 'd':
            self.marcoPartida.grid_remove()
            self.datos()
            
        
juego = Tk()
juego.minsize(453, 200)
juego.maxsize(910, 740)

gui = Gato(juego)
juego.mainloop()    
    

