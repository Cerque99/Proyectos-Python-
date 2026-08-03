#Inciamos el coste de la cocacola
deuda = 50
#El bucle se ejecutara hasta que la deuda sea 0
while deuda> 0:
    print(f"Amount due: {deuda}")
    #Pedimos la moneda y la pasamos a numero entero
    moneda = int(input("Insert coint: "))
    #Comprobamos si es una moneda aceptada
    if moneda == 25 or moneda == 10 or moneda == 5:
        #Si es valida restamos la moneda a la deuda
        deuda = deuda - moneda
#Cuando el bucle termina calculamos el cambio que le tenemos que dar
cambio = abs(deuda)
print(f"Change Owed: {cambio}")

