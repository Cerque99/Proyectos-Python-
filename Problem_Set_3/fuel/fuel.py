#Hacemos un bucle infinito hasta que el usuario responda bien
while True:
    try:
        #Pedimos la fraccion
        fraccion = input("Fraction: ")
        #Separamos la x y la y usando \
        x_str, y_str = fraccion.split("/")
        #Los pasamos a integers
        x = int(x_str)
        y = int(y_str)
        #Creamos la condicion de que x no puede ser mayor que y, si esto ocurre vuelve al principio
        if x > y or x < 0 or y < 0:
            continue
        #Calculamos el porcentaje
        porcentaje = (x / y) * 100
        #Redondeamos al entero mas cercano
        porcentaje_redondeado = round(porcentaje)
        #Si todo va bien hasta aqui rompemos el bucle
        break
    #Atrapamos los errores que nos pide el ejercicio
    except (ValueError, ZeroDivisionError):
        #Usamos el pass para que ignore el error y vuelva al bucle
        pass
  #Una vez tenemos el resultado evaluamos el porcentaje final
if porcentaje_redondeado <= 1:
    print("E")
elif porcentaje_redondeado >= 99:
    print("F")
else:
    print(f"{porcentaje_redondeado}%")


