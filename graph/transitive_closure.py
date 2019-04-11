# Transitive Closure of a Graph using DFS
from collections import defaultdict


class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)
        # to store transitive closure
        self.tc = [[0 for j in range(self.vertices)] for i in range(self.vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, u, v):
        self.tc[u][v] = 1

        for i in self.graph[v]:
            if self.tc[u][i] == 0:
                self.dfs(u, i)

    def transitive_closure(self):
        for i in range(self.vertices):
            self.dfs(i, i)
        print str(self.tc)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.transitive_closure()
