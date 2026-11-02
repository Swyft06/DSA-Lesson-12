class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def create_edges(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    #BFS = breadth first search
    def BFS(self,source):
        visited = [False]*self.n
        q = []
        q.append(source)
        visited[source] = True
        result = []

        while len(q) > 0:
            s = q.pop(0)
            result.append(s)
            for node in self.adj[s]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True

        return result


graph = Graph(4)
graph.create_edges(1,2)
graph.create_edges(1,3)
graph.create_edges(2,4)

print(graph.BFS(1))