def ejercicioDescuento():
    venta=float(input("Ingrese el valor total de la venta sin descuento: --------> "))
    descuento= 0.15

    descuentoTotal= descuento * venta
    precioFinal = venta - descuentoTotal
    print(f"El valor total de su compra es: {precioFinal: .2f}")

ejercicioDescuento()    
