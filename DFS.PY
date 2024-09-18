graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = set()

def dfs(visited,graph,nodo):
    if nodo in visited:
        return 
    else:
        print(nodo)
        visited.add(nodo)
        for i in range(len(graph[nodo])):
            dfs(visited,graph,graph[nodo][i])
        
dfs(visited,graph,'5')