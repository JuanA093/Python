def palindromo():
    palabra = input("Ingrese la palabra a comprobar --> ")

    palabra = palabra.lower()

    polindromo = palabra[::-1]

    if palabra == polindromo:
        print(f"{palabra} es palindromo")
    else:
        print(f"{palabra} no es palindromo")

palindromo()   