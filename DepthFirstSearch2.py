
class depth_first:
    def __init__(self):
        self.visited = []

        
    def dfs(self, graph):
        for ver in graph:
            if ver not in self.visited:
                self.dfs_visit(graph, ver)
        return self.visited
    
    def dfs_visit(self, graph, vertex):
        if vertex not in self.visited:
            self.visited.append(vertex)
            for nb in graph[vertex]:
                self.dfs_visit(graph, nb)



g1 = {
    's': ['b', 'c'],
    'b': ['d', 'c'],
    'd': ['f'],
    'f': ['c'],
    'c': ['d']
    }

d = depth_first()
print(d.dfs(g1))



