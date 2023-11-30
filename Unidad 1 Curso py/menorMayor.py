def mayorMenor():
    dato1 = int(input("Ingrese el dato 1 --> "))
    dato2 = int(input("Ingrese el dato 2 --> "))
    dato3 = int(input("Ingrese el dato 3 --> "))
    dato4 = int(input("Ingrese el dato 4 --> "))
    dato5 = int(input("Ingrese el dato 5 --> "))

    listaDatos = [dato1,dato2,dato3, dato4, dato5]

    listaDatos.sort()

    print(f"La lista ordenada es: {listaDatos}")
mayorMenor()    