#clave="SHAZAM"
#nom=input("ingresa la clave:")
#if nom.upper () == clave:
#   print ("clave correcta")
#else:
#   print("clave incorrecta")


# print("ingrese su nombre")
# name=input
# if 4<=len(name)<=10:
#   name=print("usuario correcto")
# else :
#    print("usuario fuera de rango")


#pin=int(input("ingrese un numero de 4 digios"))

# op=0
# total=0
# while op!=4:
#  print("1.- PC Ryzen $800.000")
#  print("2.- LGTV 55 pulgadas")
#  print("3.- Parlante JBL Pure Sound $90.000")
#  print("4.- salir")
#  print("seleccione una opcion")
#  op=int(input())
#  match op:
#     case 1:
#         print("tiene que pagar ", 800.000*1.19)
#         total+=800000*1.19
#     case 2:
#         print("tiene que pagar ",450.000*1.19)
#         total+=450000*1.19
#     case 3:
#         print("tiene que pagar ",90.000*1.19)
#         total+=90000*1.19
#     case 4:
#         print("saliendo")
#         print(f"el total a pagar con iva es {round(total,2)}")
#     case _:
#         print("opcion invalida")


# cont=1
# while cont<=3:
#     print(f"contador {cont}")
#     cont+=1


# pin=3535
# code=int(input("ingrese su pin"))
# while pin!=code:
#     print("error intente nuevamente")
#     code=int(input("ingrese su pin"))
# print("pin correcto!")

# num=int(input("ingrese un numero"))
# c=1
# while c<=10:
#     print(f"{num}x{c}={num*c}")
  

# def calculadora():op=0



# def pin():
#     pin=3535
#     code=int(input("ingrese su pin"))
#     while pin!=code:
#         print("error intente nuevamente")
#         code=int(input("ingrese su pin"))
#     print("pin correcto!")


# def calculadora():
#     op=0
#     while op!=5: 
#         print("1.- suma")
#         print("2.- resta")
#         print("3.- multiplicacion")
#         print("4.- divicion")
#         print("5.- salir")
#         print("seleccione una opcion")
#         op=int(input("seleccione una operacion"))
#         match op:
#             case 1:
#              n1=int(input("ingrese un numero: "))
#              n2=int(input("ingrese otro numero"))
#              print(f"el resultado es {n1+n2}")
#             case 2:
#              n1=int(input("ingrese un numero: "))
#              n2=int(input("ingrese ottro numero"))
#              print(f"el resultado es {n1-n2}")
#             case 3:
#              n1=int(input("ingrese un numero: "))
#              n2=int(input("ingrese ottro numero"))
#              print(f"el resultado es {n1*n2}")
#             case 4:
#              n1=int(input("ingrese un numero: "))
#              n2=int(input("ingrese ottro numero"))
#              print(f"el resultado es {n1/n2}")
#             case 5:
#              print("salir")
#             case _:
#              print("opcion invalida")


# def tablaM():
#     c=1
#     num=int(input("ingrese un numero: "))
#     while c<=10:
#         print(f"{num}x{c}={num*c}")
#         c += 1



# op=0
# total=0
# while op!=4:
#     print('''menu
#         1.- calculadora
#         2.- tablaM
#         3.- pin
#         4.- salir
#         seleccione una opcion''')
#     op=int(input())
#     match op:
#        case 1:
#           calculadora()
#        case 2:
#           tablaM()
#        case 3:
#           pin()
#        case 4:
#           print("salir")
#           print(f"intente más tarde")
#        case _: 
#           print("opcion invalida")

# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# # print(alumno)
# # print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

# productos={
#     1:{"nombre": "Control Inalambrico",
#        "categoria": "Electronica",
#        "precio": 45000},
#     2:{"nombre": "Pilas Recargables",
#        "categoria": "Insumos",
#        "precio": 5000},
#     3:{"nombre": "Pasta Termica",
#        "categoria": "Computacion",
#        "precio": 7000},
# }

# print(productos[1]["nombre"])

# '''
# Crear un diccionario de trabajadores 
# '''

# ##CRUD DE VEGETALES

# vegetales={
#    1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
# }

# print(list(vegetales.keys())[-1])


# def agregarVegetales():
#    print("-"*20)
#    agregar=input("Ingrese un vegetal: ")
#    nuevoKey=list(vegetales.keys())[-1]
#    vegetales[nuevoKey+1]=agregar
# def mostrarVegetales():
#    print("-"*40)
#    for num, nombre in vegetales.items():
#          print(f"{num}.- {nombre} ")
# def eliminarVegetal():
#    mostrarVegetales()
#    borrar=int(input("Cual vegetal borrará?: "))
#    del vegetales[borrar]
# def actualizarVegetal():
#    mostrarVegetales()
#    act=int(input("Cual vegetal actualizará?: "))
#    vegetales[act]=input("Ingrese nuevo nombre: ")

# def vegetalesMenu():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarVegetales()
#                case 2:
#                   eliminarVegetal()
#                case 3:
#                   actualizarVegetal()
#                case 4:
#                   mostrarVegetales()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)

# # vegetalesMenu()

# ##Diccionario con diccionarios
# productosDicc={
#    1:{"nombre": "Maracuyá", "precio": 3000},
#    2:{"nombre": "Pera", "precio": 1500},
#    3:{"nombre": "Cebolla", "precio": 1200}
# }
# productosDicc[4]={"nombre": "Piña", "precio": 3500}
# def agregarProducto():
#    print("Cual es el nombre del producto?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())[-1]
#    productosDicc[nuevoKey+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#       print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    borrar=int(input("Cual Producto borrará?: "))
#    del productosDicc[borrar]
# def actualizarProducto():
#    MostrarProducto()
#    num=int(input("Que producto desea actualizar?: "))

#    nombre=input("Cual es el nombre nuevo?: ")
#    precio=int(input("Cual es el precio nuevo?: "))
#    productosDicc[num]={"nombre": nombre, "precio": precio}
# # print(productosDicc[2]["precio"])  # precio de la pera
# # print(productosDicc[3]["nombre"])  # nombre de la cebolla

# # for num, veg in productosDicc.items():
# #     print(f"{num}.- {veg}")

# ##Lista con diccionarios
# productosList=[
#    {"nombre": "Maracuyá", "precio": 3000}, #0
#    {"nombre": "Pera", "precio": 1500},     #1  
#    {"nombre": "Cebolla", "precio": 1200}   #2
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya



# def vegetalesMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarProducto()
#                case 2:
#                   eliminarProducto()
#                case 3:
#                   actualizarProducto()
#                case 4:
#                   MostrarProducto()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)
# vegetalesMenuDiccionario()

# #Cambiar la funcion actualizar para que solo 
# # actualice una solo key 
# # Ademas, crear un CRUD pero con la lista 
# # de diccionarios.

