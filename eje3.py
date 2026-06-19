notas=[4.6, 7.0, 3.4, 6.6 , 3.9]
def calculaprom(n):
    return round(sum(n)/len(n),1)
print("el promedio es", calculaprom(notas))