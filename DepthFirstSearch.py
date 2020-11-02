g1 = {
    's': ['b', 'c'],
    'b': ['d', 'c'],
    'd': ['f'],
    'f': ['c'],
    'c': ['d']
    }


def dfs(graph, vertex, path=[]):
    path += [vertex]

    for n in graph[vertex]:
        if n not in path:
            path = dfs(graph, n, path)
    return path
        
    
print(dfs(g1, 's'))
