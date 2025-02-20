import math

def tryExceptDos():


    while True:
        try:
            
            num = int(input("Ingrese un numero entero positivo: "))

            if num > 0:

                numC = math.sqrt(num)

                print("La raiz cuadrada de {} es {}".format(num,numC))

                break

            else:
                print("Error X: Ingrese un nuevo numero positivo")

        except ValueError:
            print("Ingrese un valor numerico")

        

tryExceptDos()