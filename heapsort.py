def heap_sort(arreglo):
    # Construir el heap máximo
    buildheap(arreglo)
    print(arreglo)
    # Extraer elementos uno por uno desde el heap
    for i in range(len(arreglo) - 1, 0, -1):
        # Mover la raíz actual al final del arreglo
        arreglo[0], arreglo[i] = arreglo[i], arreglo[0]
        
        # Llamar heapify en el nuevo heap reducido
        heapify(arreglo, 0, i)
    
    return arreglo

def buildheap(arreglo):
    # Convertir el arreglo en un heap máximo
    for i in range(len(arreglo) // 2 - 1, -1, -1):
        heapify(arreglo, i, len(arreglo))

def heapify(arreglo, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Comprobar si el hijo izquierdo existe y es mayor que el nodo actual
    if left < n and arreglo[left] > arreglo[largest]:
        largest = left

    # Comprobar si el hijo derecho existe y es mayor que el nodo actual
    if right < n and arreglo[right] > arreglo[largest]:
        largest = right

    # Si el mayor no es el nodo actual, intercambiarlos y llamar recursivamente a heapify
    if largest != i:
        arreglo[i], arreglo[largest] = arreglo[largest], arreglo[i]
        heapify(arreglo, largest, n)

# Ejemplo de uso
arreglo = [5, 4, 2, 5, 1, 5, 9, 6, 7, 1, 65, 8, 42]
print("Arreglo original:", arreglo)
sorted_arreglo = heap_sort(arreglo)
print("Arreglo ordenado:", sorted_arreglo)