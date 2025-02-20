#Funciones para atributos
class Persona():
    edad = int(input("Ingrese su edad: "))
    nombre = input("Ingrese su nombre: ")

Ingeniero = Persona()
print("El Ingeniero tiene una edad? ",hasattr(Ingeniero, "edad"))
print("Antes era: ",Ingeniero.nombre)
setattr(Ingeniero, 'nombre','Camilo')
print("Ahora se llama: ",Ingeniero.nombre)