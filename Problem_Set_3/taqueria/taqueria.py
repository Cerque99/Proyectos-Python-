#Creamos el diccionario con el menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#Empezamos una cuenta desde 0
total = 0.0
#Bucle infinito para pedir platos continuamente
while True:
    try:
        #Pedimos un plato del menu y adaptamos para que coicidan las mayusculas
        item = input("Item: ").title()
        #Si el plato esta en el menu sumamos el precio
        if item in menu:
            total += menu[item]
            #Imprimimos el total redondeado a 2 decimales
            print(f"Total: ${total:.2f}")
      #Si el usuario presiona Ctrl+D atrapamos el error
    except EOFError:
        #Imprimimos una linea en blanco para que se limpue la terminal
        print()
        #Rompemos el buccle para terminar el programa
        break




