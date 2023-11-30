camel_case = input("Ingrese el nombre de una variable en camelCase: ")
snakeCase = ""

for i in range(len(camel_case)):
    if camel_case[i].isupper():
        snakeCase +="_" + camel_case[i].lower()
    else:
        snakeCase += camel_case[i]
print(f"El nombre de la variable en snake_case es: {snakeCase}")




