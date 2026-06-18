
nombre=input("ingrese su nombre")
prev=input("ingrese la prevencion del paciente nuevo: ")
temp=float(input("ingrese la temperatura del nuevopaciente"))
pacientes.append({"nombre": nombre, "prevencion": prev,
                  "temperatura": temp, "grave": validTemp(temp)})
print(pacientes)
while True:
    try:
        print("1.- agregar paciente")
        print("2.- quitar paciente")
        print("3.- mostrar pacientes")
        print("4.- eliminar paciente")



        opcion=int(input("ingrese la opcion"))