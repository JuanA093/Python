def media():
    dato1 = float(input("Ingrese el dato 1 -->"))
    dato2 = float(input("Ingrese el dato 2 -->"))

    datosArray = [dato1, dato2]

    operacion = dato1 + dato2

    media = operacion / len(datosArray)

    print(f"La media de los datos ingresados es: {media}")

media()