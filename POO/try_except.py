def try_except():

    

    try:

        numberOne = int(input("Ingrese el primer valor entero: "))
        numberTwo = int(input("Ingrese el segundo valor entero: "))

        resultado = numberOne / numberTwo

        print("El resultado es: {}".format(resultado))


    except ValueError:
        
        print("Ingrese un numero entero")

    except ZeroDivisionError:

        print("No se puede dividir por cero. ")


try_except()
