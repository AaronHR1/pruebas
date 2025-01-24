def heapsort(arreglo):
    n=len(arreglo)
    for i in range(n//2-1,-1,-1):
        heapify(arreglo,n,i)
    
    
    for i in range(n-1,0,-1):
        aux=arreglo[i]
        arreglo[i]=arreglo[0]
        arreglo[0]=aux
        heapify(arreglo,i,0)

    print(arreglo)

def heapify(arreglo,n,i):
    largest=i
    left=2 * i + 1
    right=2 * i + 2

    if left <n and arreglo[largest]<arreglo[left]:
        largest=left
    
    if right <n and arreglo[largest]<arreglo[right]:
        largest=right

    
    if largest != i:
        aux= arreglo[i]
        arreglo[i]=arreglo[largest]
        arreglo[largest]=aux
    
        heapify(arreglo,n,largest)


heapsort([3,45,24,2,7,8,3,2,5,2435,25467,1,0])