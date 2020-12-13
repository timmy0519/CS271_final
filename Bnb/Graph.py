from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary
        self.indexMap = {}

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def markindex(self):
        i = 0
        for v in self.V: 
            self.indexMap[v] = i
            i+=1

    def KruskalMST(self):
        self.markindex()
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(len(self.V)):
            parent.append(self.indexMap[self.V[node]])
            rank.append(0)

        while e < len(self.V) -1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, self.indexMap[u])
            y = self.find(parent, self.indexMap[v])
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        for u, v, weight in result:
            minimumCost += weight
        return minimumCost