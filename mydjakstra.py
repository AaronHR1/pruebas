import heapq
graph={
    "A":[["C",3],["F",2]],
    "C":[["A",3],["D",4],["E",1],["F",2]],
    "B":[["D",1],["E",2],["G",2]],
    "D":[["C",4],["B",1]],
    "E":[["C",1],["F",3],["B",2]],
    "F":[["A",2],["B",6],["C",2],["E",3],["G",5]],
    "G":[["F",5],["B",2]]
}


def dijakstra(graph,node):
    pq = []
    distancias={
        
    }
    for i in graph.keys():
        distancias[i]=9**9
    distancias[node]=0
    
    heapq.heappush(pq,(0,node))    
    
    while pq:
        distanciaActual,nodo=heapq.heappop(pq)
        if distanciaActual>distancias[nodo]:
            continue
        
        for vecino,weigt in graph[nodo]:
            distancia=distanciaActual+weigt
            if distancia < distancias[vecino]:
                distancias[vecino]=distancia
                heapq.heappush(pq,(distancia,vecino))
        
    
    return distancias

nuevoDic=dijakstra(graph,"A")

for nodos,peso in nuevoDic.items():
    print("Nodo:" + nodos + ", distanciaMenor:" + str(peso))
        