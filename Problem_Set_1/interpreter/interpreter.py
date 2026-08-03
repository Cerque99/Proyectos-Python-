#Pedimos al usuario la expresion
expresion = input("Expresion matematica: ")
#Separamos el texto en 3 partes
x, y, z = expresion.split(" ")
#Convertimos los numeros en float
x = float(x)
z = float(z)
#Evaluamos que operador ha introducido
if y == "+":
    resultado = x + z
elif y == "-":
    resultado = x - z
elif y == "*":
    resultado = x * z
elif y == "/":
    #El enunciado dice que z no es 0 asi que no hay que poner comprobacion
    resultado = x / z
#Mostramos el resultado con 1 decimal
print(f"{resultado:.1f}")

