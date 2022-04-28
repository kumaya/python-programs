from collections import defaultdict


class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, e, v, r):
        v[e] = True
        for child in self.graph[e]:
            if not v[child]:
                self.dfs(child, v, r)
        r.append(e)

    def topological_sort_dfs(self):
        visited = [False]*self.vertices
        res = []
        for edge in range(self.vertices):
            if not visited[edge]:
                self.dfs(edge, visited, res)
        return res[::-1]

    def topological_sort_bfs(self):
        indegrees = [0]*self.vertices
        for vertex in self.graph:
            for nei in self.graph[vertex]:
                indegrees[nei] += 1
        queue = []
        for i in range(self.vertices):
            if indegrees[i] == 0:
                queue.append(i)
        print indegrees, queue
        res = []
        while len(queue) > 0:
            rem = queue.pop(0)
            res.append(rem)
            for nei in self.graph[rem]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return res


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(1, 0)
    g.add_edge(1, 4)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 3)

    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(4, 3)

    print g.topological_sort_dfs()
    print g.topological_sort_bfs()
