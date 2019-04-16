from collections import defaultdict


class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, src, dist, paths):
        visited = [False] * self.vertices
        # distance of any node from itself is 0
        dist[src] = 0
        # there is always 1 way to move from node to itself
        paths[src] = 1

        queue = list()
        queue.append(src)
        visited[src] = True

        while queue:
            curr = queue.pop(0)
            for vertex in self.graph[curr]:
                if not visited[vertex]:
                    queue.append(vertex)
                    visited[vertex] = True

                # print curr, vertex, dist[curr], dist[vertex], queue
                # new shortest path
                if dist[vertex] > dist[curr] + 1:
                    dist[vertex] = dist[curr] + 1
                    paths[vertex] = paths[curr]
                # another shortest path
                elif dist[vertex] == dist[curr] + 1:
                    paths[vertex] += 1
        print dist
        print paths

    def num_shortest_path(self, src, dst):
        dist = [1000000] * self.vertices
        paths = [0] * self.vertices
        g.bfs(src, dist, paths)
        return paths[dst]


if __name__ == '__main__':
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 6)

    src = 2
    dst = 6
    print("Number of shortest path from %d to %d = %d" % (src, dst, g.num_shortest_path(src, dst)))