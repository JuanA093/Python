class Persona():
    edad = int(input("Ingrese su edad: "))
    nombre = input("Ingrese su nombre: ")
    pais = input("Ingrese su pais: ")

Ingeniero = Persona()
delattr(Persona, 'pais')

print(Ingeniero,'pais')
print(Ingeniero.nombre)
print(Ingeniero.edad)