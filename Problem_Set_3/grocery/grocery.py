#Creamos una lista vacia para ir metiendo los productos
lista_compra = {}
#Hacemos un bucle infinito hasta que el usuario decida parar
while True:
    try:
        #Pedimos el articulo, lo pasamos directamente a mayus
        item = input().strip().upper()
        #Si el articulo esta en la lista sumamos 1 a la cantidad
        if item in lista_compra:
            lista_compra[item] += 1
        else:
            #Si no esta en la lista ponemos 1 unidad
            lista_compra[item] = 1
    except EOFError:
        break
#Una vez fuera de la lista la ordenamos y la mostramos
#usamos sorted() que ordena alfabeticamente
for item in sorted(lista_compra.keys()):
    #Mostramos la cantidad seguida del nombre del articulo
    print(f"{lista_compra[item]} {item}")
