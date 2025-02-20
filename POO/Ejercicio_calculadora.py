class Calculadora():
    def __init__(self):
        dato1= float(input("Ingrese el primer valor: "))
        dato2= float(input("Ingrese el segundo valor: "))

        self.suma = dato1 + dato2
        self.resta = dato1 - dato2
        self.multiplicacion = dato1 * dato2
        self.division = dato1 / dato2

Operar = Calculadora()

print("El total de la suma es: ",Operar.suma)
print("El total de la resta es: ",Operar.resta)
print("El total de la multiplicacion es: ",Operar.multiplicacion)
print("El total de la division es: ",Operar.division)

