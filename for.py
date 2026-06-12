# num=int(input("ingrese su numero: "))
# if num<=-1:
#     print("este es un numero negativo")
# elif num == 1:
#     print(" este numero es positivo")
# else:
#     print("este numero es 0")

# edad=int(input("ingrese su edad: "))
# if edad>=18:
#     print("eres un adulto ")
# elif edad <=17 and edad>=1:
#     print("eres un cabro chico ")
# else:
#     print("mentiroso conchetumare")

# num1=int(input("ingrese un numero: "))
# for i in range (10):
#     print(f"{num1} x {i+1} = {num1*(i+1)}")

# palabra=input("escriba una palabra: ")
# contador=0
# for letra in palabra:
#     print(letra)
#     contador+=1
# print(f"la palabra tiene {contador} letras. ")

# i=1
# suma=0
# while i <=5: 
#  suma+=i
#  i+=1
# print(suma)

# nom=input("ingrese su nombre: ")
# ap=input("ingrese su apellido: ")
# print(nom.capitalize(), ap.capitalize())

while True:
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Potencia")
    print("6.- salir")
    operacion=int(input("Elija una operación: "))
    match operacion:
        case 1:
            num1=int(input("Ingrese un numero: "))
            num2=int(input("Ingrese otro numero: "))
            print(f"{num1} + {num2} = {num1+num2}")
        case 2:
            num1=int(input("Ingrese un numero: "))
            num2=int(input("Ingrese otro numero: "))
            print(f"{num1} - {num2} = {num1-num2}")
        case 3:
            num1=int(input("Ingrese un numero: "))
            num2=int(input("Ingrese otro numero: "))
            print(f"{num1} x {num2} = {num1*num2}")
        case 4:
            num1=int(input("Ingrese un numero: "))
            num2=int(input("Ingrese otro numero: "))
            while num2==0:
                print("No se puede dividir por 0")
                num2=int(input("Ingrese otro numero: "))
            print(f"{num1} / {num2} = {num1/num2}")
        case 5:
            num1=int(input("Ingrese un numero base: "))
            num2=int(input("Ingrese otro numero exponente: "))
            print(f"{num1} ^ {num2} = {num1**num2}")
        case 6:
            print("Saliendo")
            break
        case _:
            print("opcion invalida")



