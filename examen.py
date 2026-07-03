autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}

def vehiculo(d):
    for id, vehiculo in d.items():
        print(f"{id}:{vehiculo}")


def autosvendidios(d):
    for id, vehiculo in d.items():
        if operaciones[id][-1]!="pendiente":
            print(f"{id}:{vehiculo}")
            print("el vehiculo no se encontro")
        else:
            print("vehiculo disponible")

def autosvendidospormarca(marca):
    total=0
    for id, vehiculo in autos.items():
        if vehiculo[0].lower()==marca.lower():
            if operaciones[id][-1]!="pendiente":
                print(f"el total de vehiculos vendidos por la marca {marca} es de {total}")

print(operaciones["A003"][-1])
def actualizar(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else:
        return False
while True:
    id=input("ingrese el id del auto: ")
    fecha=input("ingrese la fecha de venta: ")

    actualizar(id, fecha)
    if actualizar(id, fecha):
        print("Fecha actualizada")
    else:
        print("metio mallas manos")
    next=input("desea actualizar otro vehiculo (s/n)?")
    if next.lower()=="s":
        break

def validarID():
    nid=input("ingrese la id del vehiculo. ")
    if " " in nid and nid=="":
            return False
    else:
            return True

def validarMARCA():
    nmarca=input("ingrse la marca del vehiculo. ")
    if " " in nmarca and nmarca=="":
        return False
    else:
        return True

def validarAÑO():
    naño=int(input("ingrese el año del vehiculo: "))
    if " " in naño and naño=="":
        return False
    else:
        return True
    
def validarMODELO():
    nmodelo=input("ingrese el modelo del vehiculo: ")
    if " " in nmodelo and nmodelo=="":
        return False
    else:
        return True

def validarRANKING():
    nranking=int(input("Ingrese el ranking: "))
    if " " in nranking and nranking=="":
        return False
    else:
        return True

def validarFECHA():
    nfecha_de_ingreso=int(input)
    if " " in nfecha_de_ingreso and nfecha_de_ingreso=="":
        return False
    else:
        return True




