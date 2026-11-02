class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def createEdges(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    def countNeighbors(self,node_index):
        return len(self.adj[node_index])

g = Graph(5)
g.createEdges(2,1)
g.createEdges(2,3)
g.createEdges(5,1)
g.createEdges(3,4)

print(g.countNeighbors(0))
print(g.countNeighbors(1))
print(g.countNeighbors(2))
print(g.countNeighbors(3))
print(g.countNeighbors(4))