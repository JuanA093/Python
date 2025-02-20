#Metodo constructor
class Persona:
    pass
    def __init__(self,nombre, edad):
        self.nombre= nombre
        self.edad = edad

    def descripcion(self):
        return " {} tiene {} ".format(self.nombre, self.edad)

    def comentario(self, frase):
        return " {} comento: {} ".format(self.nombre, frase)

        
Ingeniero = Persona('Juan', 26)

print(Ingeniero.descripcion())
print(Ingeniero.comentario("Buena"))