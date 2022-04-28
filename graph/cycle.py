# detect cycle in an undirected graph
from collections import defaultdict


class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def get_parent(self, parent, i):
        if parent[i] == -1:
            return i
        # else fetch top level parent
        return self.get_parent(parent, parent[i])

    # establish a parent child relationship between u,v if there does not
    # exists any
    def union(self, parent, x, y):
        x_p = self.get_parent(parent, x)
        y_p = self.get_parent(parent, y)
        parent[x_p] = y_p

    def has_cycle(self):
        parent = [-1]*self.vertices
        for i in self.graph:
            for j in self.graph[i]:
                x = self.get_parent(parent, i)
                y = self.get_parent(parent, j)
                if x == y:
                    return True
                else:
                    self.union(parent, x, y)
        return False


class GraphNew(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    # undirected graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u)

    def cycle(self, edge, visited):
        queue = list()
        queue.append(edge)
        while len(queue) > 0:
            rem = queue.pop(0)
            if visited[rem]:
                return True
            else:
                visited[rem] = True
                for nei in self.graph[rem]:
                    if not visited[nei]:
                        visited[nei] = "seen"
                        queue.append(nei)
        return False

    def is_cyclic(self):
        visited = [False]*self.vertices
        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self.cycle(vertex, visited):
                    return "CYCLIC"
        return "ACYCLIC"


if __name__ == '__main__':
    g = Graph(3)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 1)

    cycle = g.has_cycle()
    if cycle:
        print "Cyclic"
    else:
        print "Acyclic"

    g = GraphNew(6)
    g.add_edge(1, 0)
    g.add_edge(1, 4)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(4, 5)

    g = GraphNew(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 1)

    g = GraphNew(2)
    g.add_edge(1, 0)
    g.add_edge(0, 1)
    print g.is_cyclic()
