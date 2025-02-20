class cuentaBancaria():

    def __init__(self):

        self.numeroCuenta = int(input("Ingrese el numero de cuenta ----> "))
        self.nombreTitular = input("Ingrese el nombre del titular ----> ")
        self.saldoCuenta = float(input("Ingrese el saldo de la cuenta ------> "))

        print("Marque la opcion del servivio a realizar: ")
        self.selectorTransaccion=(int(input("1, para realizar un deposito, 2 para realizar un retiro----->")))

        if self.selectorTransaccion == 1:
            self.depositarDinero()     

        elif self.selectorTransaccion == 2:
             self.retirarDinero()    


    def depositarDinero(self):

            cantidadDeposito = float(input("Que cantidad desea ingresar? "))

            if cantidadDeposito > 0:

                self.saldoCuenta = self.saldoCuenta + cantidadDeposito

                print(f"Usted ha despositado {cantidadDeposito}")
                print(f"El nuevo saldo de su cuenta es {self.saldoCuenta}")

            else:
            
                print("Ingrese una cantidad mayor a cero. ")

    def retirarDinero(self):

        if self.saldoCuenta >= 0:  

            cantidadRetiro = float(input("Que cantidad desea retirar? "))
 
            if cantidadRetiro < self.saldoCuenta:

                self.saldoCuenta = self.saldoCuenta - cantidadRetiro

                print(f"Usted ha retirado la cantidad de {cantidadRetiro}")
                print(f"Su nuevo saldo es {self.saldoCuenta}")

            else:
                print("No tiene dinero suficiente en la cuenta para realizar este retiro")          



    def imprimirDatos(self):
        print(f"El numero de cuenta es: {self.numeroCuenta}, el nombre del titular es: {self.nombreTitular} y tiene un saldo de: {self.saldoCuenta}")


cuenta = cuentaBancaria()

cuenta.imprimirDatos()






        



