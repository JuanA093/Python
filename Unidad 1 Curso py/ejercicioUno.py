def main():

    platoPrincipal = {'Bajo Taco': 4.00, 'Burrito':7.50, 'Bowl': 8.50, 'Super Burrito': 8.50, 'Super Quesadilla': 9.50, 'Taco': 3.00, 'Tortilla Salad': 8.00}

    while True:
        try:
            eleccionPlato = input("Seleccione su plato principal:\n Bajo Taco\n Burrito\n Bowl\n Super Burrito\n Super Quesadilla\n Taco\n Tortilla Salad\n")
        except ValueError:
            break

        total = 0
        for plato in platoPrincipal:   
            if eleccionPlato == plato:
                print(f"Usted ha seleccionado {eleccionPlato}") 
                print("eleccion: ", plato)
                total += platoPrincipal[eleccionPlato]
                print(f"El total de su comida es ${total}")
                break 
            else :
                print("plato no encontrado")
main()        
