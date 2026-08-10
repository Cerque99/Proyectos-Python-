import sys
import requests

#Comprobar que el usuario escribe 2 palabaras
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    #Convertimos lo que escribio el usuario a numero decimal
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

#Conectamos a la API y obtenemos los datos
try:
    api_key = "e701a38207f13558324ae8d5752c805e13f665c662c8ad5fb1986b308078cbae"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    #Hacemos la peticion a la web
    respuesta = requests.get(url)

    #Convertimos la respuesta cruda de internet a un diccionario facil de leer (JSON)
    datos = respuesta.json()

    #Buscamos los cajones del JSON hasta encontrar el precio
    #Lo guarda en "data" y luego en "priceUsd"
    precio_bitcoin = float(datos["data"]["priceUsd"])
#Atrapamos cualquier error de conexion a internet o de la API
except requests.RequestException:
    sys.exit("Error al conectar con la API")
#Atrapamos el error si la API cambia su estructura y o encontramos "priceUsd"\
except (KeyError, TypeError, ValueError):
    sys.exit("Error al leer los datos de JSON")

#Calculo y formato final
coste_total = n * precio_bitcoin

#Imprimos el formato que nos pide Hardvard:
#Usamos "," como separadores de miles.
#Y con 4 decimales con .4f.
print(f"${coste_total:,.4f}")

