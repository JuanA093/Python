def main():
    mensaje = input("Ingrese el mensaje o el twit:\n ")
    resultado = twtr(mensaje)

    print("La palabara abreviada es: "+''.join(resultado))

def twtr(msg):
    msg = msg.lower()
    mensajeLista = []
    for i in range(len(msg)):
        if msg[i] not in ["a","e","i", "o", "u", " "]:
            mensajeLista.append(msg[i])
    return mensajeLista


if __name__ == "__main__":
    main()        