#djkastra ADJANCENTY MATRIX

graph={
    "A":[["C",3],["F",2]],
    "C":[["A",3],["D",4],["E",1],["F",2]],
    "B":[["D",1],["E",2],["G",2]],
    "D":[["C",4],["B",1]],
    "E":[["C",1],["F",3],["B",2]],
    "F":[["A",2],["B",6],["C",2],["E",3],["G",5]],
    "G":[["F",5],["B",2]]
}


import heapq

def dijkstra(graph, start):
    # Inicializar distancias y camino más corto
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distancia, nodo)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si encontramos una distancia mayor a la conocida, lo ignoramos
        if current_distance > distances[current_node]:
            continue
        
        # Revisar los vecinos
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Si encontramos una distancia más corta, actualizamos y añadimos a la cola de prioridad
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances



start_node = "A"
shortest_paths = dijkstra(graph, start_node)
print(f"Las distancias más cortas desde el nodo {start_node} son:")
for node, distance in shortest_paths.items():
    print(f"Distancia desde {start_node} a {node} es {distance}")


