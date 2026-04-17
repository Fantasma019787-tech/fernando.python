vocales=0
consonantes=0
nombre=input("ingrese su nombre ")
for i in nombre:
    if i in "aeiouAEIOU":
       vocales=vocales+1
    elif i==" ":
       ""
    else:
     consonantes=consonantes+1
print("el numero de vocales de su nombre es:", vocales)
print("el numero de consonantes de su nombre es:", consonantes)
