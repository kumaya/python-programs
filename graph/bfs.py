# BFS of a graph


class Vertex(object):
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.edge = []

    @property
    def nextVertex(self):
        return self.edge

    @nextVertex.setter
    def nextVertex(self, dest):
        self.edge.append(dest)


def bfs(vertex):
    queue = list()
    queue.append(vertex)
    vertex.visited = True
    while queue:
        s = queue.pop(0)
        print s.data,
        for i in s.nextVertex:
            if not i.visited:
                queue.append(i)
                i.visited = True


if __name__ == '__main__':
    v0 = Vertex(10)
    v1 = Vertex(11)
    v2 = Vertex(12)
    v3 = Vertex(13)
    v0.nextVertex = v1
    v0.nextVertex = v2
    v1.nextVertex = v2
    v2.nextVertex = v0
    v2.nextVertex = v3
    v3.nextVertex = v3

    bfs(v2)
