# Declaración de clase.
class Coches():
    
    # Creación de constructor
    def __init__(self,marca,modelo):
        
        #Declaración de atributos.
        self.marca = marca
        self.modelo = modelo
        self.color = "Rojo"
    
    # Creación de métodos.
    def elColor(self):
        return self.color

# Creación de objeto.               
miCoche = Coches("Camaro", 2017)



# Impresión de atributos.
print(f"Marca: {miCoche.marca} \nModelo: {miCoche.modelo}")

# Impresión de mètodos.
print(f"Color: {miCoche.elColor()}")

#Impresión del tipo de dato objeto.
print("Tipo de objeto y clase:",type(miCoche))

# Declaración de subclase (Heredada).
class CocheDeportivo(Coches):
    def __init__(self, marca, modelo, velMax):
        Coches.__init__(self, marca, modelo)
        self.velMax = velMax

# Impresión de atributos de la subclase.        
segundoCoche = CocheDeportivo("Subaru", 2015, "250 kPs")

print("\nEsta es una subclase:", segundoCoche)
print(f"Velocidad máxima del carro deportivo es: {segundoCoche.velMax}")
print(f"Marca del carro deportivo es: {segundoCoche.marca}\nModelo del carro deportivo es: {segundoCoche.modelo}")

# Comprobación de instancia de la subclase cocheDeportivo en Coche.
print(f"\n¿El objeto segundoCohe pertenece a la subclase CocheDeportivo? : {isinstance(segundoCoche, CocheDeportivo)}")
print(f"\n¿El objeto segundoCohe pertenece a la clase padre Coches? : {isinstance(segundoCoche, Coches)}")