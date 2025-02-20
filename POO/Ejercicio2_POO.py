#Funciones para atributos
class Persona():
    edad = int(input("Ingrese su edad: "))
    nombre = input("Ingrese su nombre: ")

Ingeniero = Persona()

print("La edad de",Ingeniero.nombre, "es",Ingeniero.edad)
print("La edad es: ", getattr(Ingeniero,"edad"))


    
    
    