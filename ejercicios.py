
# num_ticket=int(input("bienvenido, cual es el numero de su ticket: "))
# if num_ticket>= 1000 and num_ticket<=8500:
#     print("ticket valido")
#     print("ingrese su edad: ")
#     edad=int(input("ingrese su edad"))
#     if edad>= 15:
#         print("puede pasar al concierto")
#     else:
#         print("no puede pasar")

# num1=int(input("ingrese un numero: "))
# for i in range(10):
#     print(f"{num1} x {i+1} = {num1*(i+1)}")

# cont=0
# while cont<3:
#     print(f"contador {cont}")
#     cont+=1

# for i in range(1):
#     print("ingrese las notas del alumno ")
#     suma=0
#     for k in range(3):
#         n=int(input())
#         suma=suma+n
#     prom=suma/3
#     print(f"el promedio de notas es {prom}")
#     if prom>40:
#         print("el alumno aprobó")
#     else:
#         print("waja aweonao")

# c_num=0
# num=int(input("ingrese un numero: "))
# for i in range(1,11):
#     c_num=+1
#     print(f"{num} x {i} = {num*i}")

# num=int(input("ingrese un numero: "))
# cont=1
# while c<=10:
#         print(f"{num}x{c}={num*c}")
#         cont+=1

# edad=int(input("ingrese su edad: "))

# if edad>=18 and edad<100 :
#     print("eres mayor de edad")
# elif edad<18 and edad>=1:
#     print("eres menor de edad")
# else:
#     print("WHERE IS OMNI-MAN")

# op =0
# totalap=0
# while op !=4:
#     print("bienvenido")
#     print("1.- manzanas $500")
#     print("2.- naranjas $600")
#     print("3.- sandia $2000")
#     print("4.-salir")
#     op=int(input("elija una opcion: "))
#     match op:
#         case 1:
#             print("usted compro manzanas")
#             totalap+=500
#         case 2:
#             print("usted compro naranjas")
#             totalap+=600
#         case 3:
#             print("usted compro sandia")
#             totalap+=2000
#         case 4: 
#             print("saliendo del sistema")
#             print("gracias por su compra")
#         case _:
#             print("opcion invalida")
# print(f"el total a pagar es {totalap}")


# op=0
# while op !=5:
#     print("1.-suma")
#     print("2.-resta")
#     print("3.-multiplipicar")
#     print("4.-dividir")
#     print("5.- salir")
#     op=int(input("que quiere hacer: "))
#     match op:
#         case 1:
#           def sumar():
#             num1=int(input("ingrese su numero: "))
#             num2=int(input("ingrese otro numero: "))
#             suma=num1+num2
#             print(f"el resultado es{suma}")
#           sumar()
#         case 2:
#           def resta():
#             num1=int(input("ingrese su numero: "))
#             num2=int(input("ingrese otro numero: "))
#             resta=num1-num2
#             print(f"el resultado es{resta}")
#           resta()
#         case 3:
#           def multi():
#             num1=int(input("ingrese su numero: "))
#             num2=int(input("ingrese otro numero: "))
#             multi=num1*num2
#             print(f"el resultado es{multi}")
#           multi()
#         case 4:
#           def div():
#             num1=int(input("ingrese su numero: "))
#             num2=int(input("ingrese otro numero: "))
#             div=num1//num2
#             print(f"el resultado es{div}")
#           div()
#         case 5:
#           print("saliendo")
#         case _:
#           print("opcion incorrecta")







# def sumar():
#     num1=int(input("ingrese su numero"))
#     num2=int(input("ingrese otro numero"))
#     suma=num1+num2
#     print(f"el resultado es{suma}")
# sumar()

# def dividir():
#    num1=int(input("ingrese su numero"))
#    num2=int(input("ingrese otro numero")) 
#    div=num1/num2
#    print(f"el resultado es{div}")
# dividir()


import random
# j1=input("ingrese su nombre: ")
# j2=input("ingrese su nombre: ")
# j3=input("ingrese su nombre: ")

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)
# dado3=random.randint(1,6)
# if dado1>dado2 and dado1>dado3:
#     print(f"el ganador es {j1} con {dado1} puntos ")
#     print(f"la puntuacion de {j2} es {dado2}")
#     print(f"la puntuacion de {j3} es {dado3}")
# elif dado2>dado3:
#         print(f"el ganador es {j2} con {dado2} puntos ")
#         print(f"la puntuacion de {j1} es {dado1}")
#         print(f"la puntuacion de {j3} es {dado3}")
# else:
#         print(f"el ganador es {j3} con {dado3} puntos ")
#         print(f"la puntuacion de {j2} es {dado2}")
#         print(f"la puntuacion de {j1} es {dado1}")

# alacran=100
# subcerro=100
# turno=1
# while alacran>0 and subcerro>0:
#     print(f" estamos en el turno {turno}")
#     golpe1=random.randint(7,15)
#     golpe2=random.randint(7,15)
#     subcerro -=golpe1
#     alacran -=golpe2
#     turno+=1
#     if alacran>subcerro:
#         print("alacran gana el mortal kumbias")
#     else:
#         print("subcerro gana el mortal kumbias")


# num=int(input("ingrese un numero: "))
# if num>=1:
#     print("el numero es positivo")
# elif num<=-1:
#     print("el numero es negativo")
# else:
#     print("el numero es cero")

# nombre=input("ingrese su nombre: ")
# print(nombre.upper())
# print(nombre.capitalize())
# print(nombre.lower())

# num=int(input("ingrese un numero: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# num=random.randint(1,10)
# resp=int(input("cual es el numero?"))
# while resp!=num: 
#     resp=int(input("cual es el numero?"))
#     print("numero incorrecto intente otra vez")
# print("numero correcto")

# palabra=input("escriba una palabra: ")
# contador=0
# for letra in palabra:
#     print(letra)
#     contador+=1
# print(f"la palabra tiene {contador} letras. ")

# word=input("ingrese una palabra: ")
# cons=0
# voc=0
# for letra in word:
#    if letra in "AEIOUaeiou":
#       voc+=1
#    else:
#       cons+=1
# print(f"el total de vocales en su palabra son {voc} y el numero de consonantes en su palabra son {cons}")

# contra = "Duoc.2024"
# intento=0
# while intento  <=3 :
#     code=input("ingrese la contraseña: ")
#     if code==contra:
#         print("acceso permitido")
#         break
#     else: 
#         intento+=1
#         contra=input("ingrese la contraseña")
 

# def suma(): 
#        num1=int(input("ingrese un numero: "))
#        num2=int(input("ingrese otro numero: "))  
#        suma=num1+num2
#        print(f"{num1} + {num2} = {num1+num2}")


# def resta():
#       num1=int(input("ingrese un numero: "))
#       num2=int(input("ingrese otro numero: "))
#       resta=num1-num2
#       print(f"{num1} - {num2} = {num1-num2}")


# def multi():
#       num1=int(input("ingrese un numero: "))
#       num2=int(input("ingrese otro numero: "))
#       multi=num1*num2
#       print(f"{num1} x {num2} = {num1*num2}")


# def div():
#       num1=int(input("ingrese un numero: "))
#       num2=int(input("ingrese otro numero: "))
#       div=num1/num2
#       print(f"{num1} / {num2} = {num1/num2}")
      


# def poten():
#       num1=int(input("ingrese un numero: "))
#       num2=int(input("ingrese otro numero: "))
#       poten=num1**num2
#       print(f"{num1} /X {num2} = {num1**num2}")
 #calculadora
# op=int(input("operacion "))
# match op :
#       case 1:
#             suma()
#       case 2:
#             resta()
#       case 3:
#             multi()
#       case 4:
#             div()
#       case 5:
#             poten()
#       case _:
#             print("opcion invalida")





# intentos=0
# nom=input("ingrese su nombre: ")
# print(f"{nom.capitalize()} tienes 3 intentos, usalos con sabiduria")
# n1=random.randint(1,7)
# while intentos<3:
#    numero=int(input("ingrese un numero: "))
#    if numero!=n1:
#       print("numero incorrecto")
#       intentos+=1
#    else:
#       print(f"felicidades {nom.capitalize()} colocaste el numero correcto")



a=-10
b=4
abs((a-b))

