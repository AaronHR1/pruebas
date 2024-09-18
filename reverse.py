

cadena="3+2+1+3+1+1+1+2+2+3+1+3+2+1"

def funcion(cadena):
    numeros=[]
    for caracter in cadena:
        if caracter != '+':
            numeros.append(int(caracter))
            
    nuevoArreglo=countingSort(numeros)
    cadenaNueva=""
    for i in range(len(nuevoArreglo)):
        cadenaNueva+=str(nuevoArreglo[i])
        if i!=len(nuevoArreglo)-1:
            cadenaNueva+="+"
        
    print(cadenaNueva)
        
         
    

def countingSort(numeros):
    index=[0]*4
    
    for i in numeros:
        index[i]+=1
    suma=0
    for inx in range(len(index)):
        suma=suma+index[inx]
        index[inx]=suma
    
    nuevoArreglo=[0]*len(numeros)

    for elemento in numeros:
        nuevoIndex=index[elemento]
        nuevoArreglo[nuevoIndex-1]=elemento
        index[elemento]-=1
    
    return nuevoArreglo
    
    
funcion(cadena)
    