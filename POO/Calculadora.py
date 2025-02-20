def Calculadora():
    dato1=int(input("Ingrese el primer valor: "))
    dato2=int(input("Ingrese el segundo valor: "))
    print()
    print("*****Opciones de cálculo****")
    print()
    operacion=int(input("Seleccione 1 para suma: \nSeleccione 2 para resta:\nSeleccione 3 para division: \nSeleccione 4 para producto: \n"))
    if operacion == 1:
        print("El resultado de su operacion es: ",dato1 + dato2)
    elif operacion == 2:
        print("El resultado de su operacion es: ",dato1 - dato2)
    elif operacion == 3:
        print("El resultado de su operacion es: ",dato1 / dato2)
    elif operacion == 4:
        print("El resultado de su operacion es: ",dato1 * dato2)            

    
Calculadora()             