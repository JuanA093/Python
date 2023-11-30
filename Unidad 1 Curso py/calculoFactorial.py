def factorial():
    n = int(input("Ingrese el dato a calcular --> "))

    factorial = 1

    if n >= 0:
        for i in range(1, n + 1 ):
            factorial *= i
        print(f"El resultado factorial es : {factorial}")

    else:
        print("Ingrese un numero positivo!")
    


factorial()
       