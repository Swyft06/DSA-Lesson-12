class Graph:
    def __init__(self, n):
        self.adj = [[] for i in range(n)]

    def addEdge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def countNeighbors(self, node_index):
        return len(self.adj[node_index])

g = Graph(5)

g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(0, 1)
g.addEdge(3, 4)

print("Number of neighbors:", g.countNeighbors(2))