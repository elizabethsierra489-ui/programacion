#Actividad 1: TAD NaveEspacial 

#Imagina que estás desarrollando un videojuego RPG. En lugar de crear un simple "Usuario", vas 
#a modelar una clase NaveEspacial que servirá para instanciar las naves que pilotan los jugadores 
#en el espacio. 

#• Requerimientos: 
#1. Crea la clase NaveEspacial con los atributos: nombre, piloto y nivel_escudo (un 
#valor entero, por ejemplo, 100). 
#2. Instancia dos naves distintas (por ejemplo, el "Halcón Milenario" pilotado por 
#"Han Solo" y el "X-Wing" pilotado por "Luke Skywalker"). 
#3. Imprime en pantalla las características iniciales de ambas naves.
class NaveEspacial:
    def __init__(self, nombre: str, piloto: str, nivel_escudo: int):
        self.nombre = nombre
        self.piloto = piloto
        self.nivel_escudo = nivel_escudo

# 2. Instanciación de las dos naves
nave1 = NaveEspacial("Halcón Milenario", "Han Solo", 100)
nave2 = NaveEspacial("X-Wing", "Luke Skywalker", 100)

# 3. Impresión de características iniciales
print("CARACTERÍSTICAS INICIALES DE LAS NAVES ")
print(f"Nave: {nave1.nombre} | Piloto: {nave1.piloto} | Escudo: {nave1.nivel_escudo}")
print(f"Nave: {nave2.nombre} | Piloto: {nave2.piloto} | Escudo: {nave2.nivel_escudo}")