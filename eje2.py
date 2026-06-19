peliculas=[
    {"titulo": "inception", "director": "christopher nolan",
     "genero": "ciencia ficcion", "año": 2010},
         {"titulo": "jurasic park", "director": "steven spilberg",
     "genero": "ciencia ficcion", "año": 1993},
         {"titulo": "se7en", "director": "christopher nolan",
     "genero": "thiller", "año": 1997},
]

'''
1.- ingresar pelicula
2.- quitar pelicula
3.- actualizar pelicula
4.- mostrar pelicula
5.- mostrar solo los titulos
6.- salir
'''
def validarAño(año):
   if año>2026 or año<1960:
       return True 
   else:
       return False


def mostrarPeliculas():
    if len(peliculas)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in peliculas:
            print(f"{c} .- {p}")
            c+=1


def eliminarPaciente():
    mostrarPeliculas()
    peli=int(input("Que paciente se vá?: "))
    peliculas.pop(peli-1)
    print("Pelicula eliminada.")


def agregarPelicula():
    nombre=input("Ingrese nombre: ")
    año=int(input("Ingrese temp: "))
    director=input("")
    peliculas.append({"nombre": nombre,
                "año":año, "grave": validarAño(año)})
    print("Paciente agregado al listado")








def menupacientes():
    while True:
        try:
            print("1.- Ingresar paciente")
            print("2.- Quitar paciente")
            print("3.- Tomar Temperatura")
            print("4.- Cobra atencion")
            print("5.- Mostrar Pacientes")
            print("9.- Salir")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    print("")
                case 2:
                    print("")
                case 3:
                    print("")
                case 4:
                    print("")
                case 5:
                    print("")
                case 9:
                    print("")
                    break
                case _:
                    print("")
        except Exception as e:
            print("Error:" , e)