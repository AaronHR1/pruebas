
arreglo=[1,4,1,2,7,5,2]

index=[0]*10

for elemento in arreglo:
    index[elemento]+=1

print(index)

suma=0
for inx in range(len(index)):
    suma=suma+index[inx]
    index[inx]=suma

nuevoArreglo=[0]*len(arreglo)

for elemento in arreglo:
    nuevoIndex=index[elemento]
    nuevoArreglo[nuevoIndex-1]=elemento
    index[elemento]-=1
    
print(nuevoArreglo)