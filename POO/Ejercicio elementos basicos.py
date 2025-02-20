radio=float(input("Ingrese el valor del radio: -------> "))
pi= 3.1416
def operarArea():
    area = pi * (radio**2)
    area = round(area,2)
    longitud = (2 * pi) * radio
    longitud = round(longitud,2)

    

    print(f"El area de la circunferencia es: {area}  y su longitud equivale a {longitud}")

operarArea()    
