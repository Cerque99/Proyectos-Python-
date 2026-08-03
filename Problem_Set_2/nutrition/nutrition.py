#Creamos un diccionario con las frutas requeridas por la FDA
#En minuscula para que sea mas facil buscar
calorias_frutas = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honerydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80

}

#Pedimos la fruta al usuario, quitamos espacios yl apasmos a minuscula
item = input("Item: ").strip().lower()
#Comprobamos si la fruta esta en el diccionario
if item in calorias_frutas:
    #Si existe, imprimimos su valor correspondiente
    print(f"Calories: {calorias_frutas[item]}")
