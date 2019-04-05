# depth first search of a graph


class Vertex(object):
    def __init__(self, v):
        self.data = v
        self.visited = False
        self.edge = []

    @property
    def next_vertex(self):
        return self.edge

    @next_vertex.setter
    def next_vertex(self, d):
        self.edge.append(d)


def dfs(v):
    stack = list()
    stack.append(v)
    v.visited = True
    while stack:
        s = stack.pop()
        print s.data,

        for i in s.next_vertex:
            if not i.visited:
                i.visited = True
                stack.append(i)


def dfs_recursion(v):
    v.visited = True
    print v.data,
    for i in v.next_vertex:
        # print "==", i.data, i.visited
        if not i.visited:
            dfs_recursion(i)


if __name__ == '__main__':
    v0 = Vertex(10)
    v1 = Vertex(11)
    v2 = Vertex(12)
    v3 = Vertex(13)
    v0.next_vertex = v1
    v0.next_vertex = v2
    v1.next_vertex = v2
    v2.next_vertex = v0
    v2.next_vertex = v3
    v3.next_vertex = v3

    # dfs(v2)
    print ""
    # Comment either call before running.
    dfs_recursion(v2)
