def mergeSort(arreglo):
    if len(arreglo) <=1:
        return arreglo
    
    mid=len(arreglo)//2
    left=arreglo[:mid]
    right=arreglo[mid:]
    
    leftSorted=mergeSort(left)
    rightSorted=mergeSort(right)
    
    return merge(leftSorted,rightSorted)
    
    
    
    
def merge(left,right):
    sorted=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
        
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

array = [5, 4, 2, 5, 1, 5, 9, 6, 7, 1, 65, 8, 42]
sorted_array = mergeSort(array)
print("Sorted array:", sorted_array)