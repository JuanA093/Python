class Persona():

    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI


    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,a):
        self.nombre = a
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self,a):
        self.edad = a

    def get_DNI(self):
        return self.DNI
    
    def set_DNI(self,a):
        self.DNI = a

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.DNI}")

    def esMayorDeEdad(self):

        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("No es mayor de edad")
        


nombre = input("Ingrese su nombre ")
edad = int(input("Ingrese su edad "))
DNI = int(input("Ingrese su DNI "))

persona = Persona(nombre,edad,DNI)

persona.mostrar()
persona.esMayorDeEdad()


        