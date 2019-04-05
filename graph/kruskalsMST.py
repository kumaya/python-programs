class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def get_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.get_parent(parent, parent[i])

    # establish parent child relation if not exists
    def union(self, parent, x, y):
        x_p = self.get_parent(parent, x)
        y_p = self.get_parent(parent, y)
        parent[x_p] = y_p

    def kruskals(self):
        mst = []
        parent = []
        for i in range(self.vertices):
            parent.append(i)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        e = 0
        i = 0
        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.get_parent(parent, u)
            y = self.get_parent(parent, v)
            # if this edge is not part of mst add it and increase used
            # edge count and also establish a parent child relation between u,v
            if x != y:
                e += 1
                mst.append([u, v, w])
                self.union(parent, x, y)
            else:
                # don't do anything as this u,v is already in mast
                pass
        return mst


if __name__ == '__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 0, 8)
    g.add_edge(7, 8, 7)

    # g = Graph(4)
    # g.add_edge(0, 1, 10)
    # g.add_edge(0, 2, 6)
    # g.add_edge(0, 3, 5)
    # g.add_edge(1, 3, 15)
    # g.add_edge(2, 3, 4)

    mst = g.kruskals()
    for u, v, weight in mst:
        print u, "-->", v, "==", weight
