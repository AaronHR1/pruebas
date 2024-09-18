def frequencySort(nums):
    frecuencia = [[] for _ in range(len(nums))]
    diccionario={
        
    }
    nuevoArreglo=[]
    for num in nums:
        if num in diccionario:
            diccionario[num]+=1
        else:
            diccionario[num]=1
    
    
    for i in diccionario.keys():
        valor=int(i)
        frecu=int(diccionario[i])
        frecuencia[frecu-1].append(valor)
        
    print(frecuencia)
      
    
    for i in range(len(frecuencia)):
        
        arreglo=frecuencia[i]
        longitud=len(arreglo)
        
        if longitud==0:
            continue
        arreglo.sort(reverse=True)
        for elemento in arreglo:
            for j in range(i+1):
                nuevoArreglo.append(elemento)
                
    return nuevoArreglo      
            
    
    
arreglo=frequencySort([-6,-6,-6])
print(arreglo)