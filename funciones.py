
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

turno=1
if turno%2==0:
    print("turno uno")
else:
    print("turno dos")

alacran=100
subcerro=100
alacran=random.randint(15,45)
subcerro=random.randint(15,45)
time.sleep(1)
print(f"alacran hizo {alacran} daño")
print(f"subcerro hizo {subcerro} daño")


