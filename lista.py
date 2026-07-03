pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"}, #0
    {"color": "azul", "capacidad": 1500, "formato": "tarro"}, #1
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"}, #2
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"}, #3
]

def cb(lista, color):
    for i in lista:
        if i["color"] == color:
            print("disponible")
        else:
            print("el color no esta diponible. ")
        

cael=input("que color va a elegir? ")
          
cb(pinturas, cael)


nums=[23, 65, 87, 2, 5, -67, -26, 36]
def buscan(lista, num):
    for n in lista:
        if n==num:
            return "numero encontrado"
    return "no se encontro el numero"
print(buscan(nums, -67))
