
import random 
import time
# num=random.randint(1,10)
# print(num)
# for i in range(num):
#     print("hola mundo")
# dado=random.randint
# print("el dado salio", dado)


# num=int(input("ingrese un numero: "))
# for i in range (1,24):
#     print(f"{num} x {i} = {num*i}")


# strike=random.randint(10,80)
# if strike>60:
#     print("GOLPE CRITICO!", strike)
# else:
#     print("golpe normal", strike)


# cont_p=0
# for i in range(24):
#     cont_p+i
#     print(f"usted avanza {cont_p} casillas")


# player1=random.randint(60,190)
# player2=random.randint(60,190)
# player3=random.randint(60,190)
# time.sleep(1)
# print(f"el jugador 1 llego {player1} metros")
# print(f"el jugador 2 llego {player2} metros")
# print(f"el jugador 3 llego {player3} metros")
# time.sleep(2)
# if player1>player2 and player1>player3:
#     print("el jugador 1 llego más lejos")
# elif player2>player3 and player2>player1:
#     print("el jugador 2 llego más lejos")
# else:
#     print("el jugador 3 llego más lejos")

# turno=1
# if turno%2==0:
#     print("turno uno")
# else:
#     print("turno dos")

# alacran=100
# subcerro=100
# alacran=random.randint(15,45)
# subcerro=random.randint(15,45)
# time.sleep(1)
# print(f"alacran hizo {alacran} daño")
# print(f"subcerro hizo {subcerro} daño")


# num=random.randint(1,9)

# while abs(-3)!=num:
#     print(num)
#     time.sleep(1)
#     num=random.randint(1,9)


# n1=int(input("ingrese el valor de limite inferior"))
# n2=int(input("ingrese el valor de limite superior"))
# num=random.randint(n1,n2)
# if n1>n2:
#     print(f"{n1} es mayor a {n2} el numero es {num}")
# else:
#     print("rango fallido")

# while n1>n2:
#     print("el limite superior debe ser mayor")
#     n2=int(input("ingrese el valor de limite superior"))
# num=random.randint(n1,n2)
# print(num)



# lata=0
# plancha=0
# pez=random.randint(10,20)
# for i in range(pez):
#     peso=random.randint(400,3000)
#     if peso<=800 :
#         print("va a la lata")
#         lata+=1
#     elif peso>=801 and peso<=3000:
#         print("huele a quemado?")
#         plancha+=1
# print(f"hay un total de {lata} latas, y un total de {plancha} peces en la plancha")


# exportacion=["nacional", "internacional"]
# latas=0
# peso=int(input("ingrese el peso del producto"))
# for i in range(latas):
#     sodio=random.randint(1,100)
#     nacion=random.choice(exportacion)
#     peso=random.randint(100,1500)

nombres=["Elver","Adolf","Jefri"]
apellidos=["Galarga","Hitler","Einstein"]

no=input("ingrese un nombre: ")
ap=input("ingrese un apellido: ")
nombres.append(no)
apellidos.append(ap)

for n in range(len(nombres)):
    print(nombres[n], apellidos[n])

# juguetes=["yo-yo","tetris"]
# def mostrar():
#     c=1
#     for j in juguetes:
#       print(c,".-",j)
#     c+=1
#     print("-"*30)


# def actualizar():
#     mostrar()
#     print("Que juguete desea actualizar: ")
#     actu=int(input())
#     nj=input("ingrese un nuevo juguete: ")
#     juguetes[actu-1]=nj

# def eliminar():
#     mostrar()
#     eliminar=int(input("que juguete desea eliminar"))
#     juguetes.pop(eliminar-1)
#     print("juguete eliminado")

# def agregar():
#     ju=input("ingrese un juguete")
#     juguetes.append(ju)

# def menu():
#     print("1.- Agregar juguete")
#     print("2.- Eliminar juguete")
#     print("3.- Actualizar juguete")
#     print("4.- Mostrar juguetes")
#     print("5.- Salir")
# while True:
#     menu()
#     try:
#         op=int(input("seleccione una opcion: "))
#         match op:
#             case 1:
#                 agregar()
#             case 2:
#                 eliminar()
#             case 3:
#                 actualizar()
#             case 4:
#                 mostrar()
#             case 5:
#                 print("saliendo")
#                 break
#             case _:
#                 print("opcion invalida")
#     except ValueError as E:
#         print("debes ingresar numeros enteros")
#         print(E)



# numeros=input("ingrese numeros separados por espacios: ")
# listanumeros=numeros.split()
# listanumerosInt=[]
# pares=[]
# impares=[]

# for n in listanumeros:
#     listanumerosInt.append(int(n))
#     print(n)
# for hh in listanumerosInt:
#     if hh%2==0:
#         pares.append(hh)
#     else:
#         impares.append(hh)
# print(f"los numeros pares son {pares}")
# print(f"los numeros impares son {impares}")

