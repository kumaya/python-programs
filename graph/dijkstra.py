from collections import defaultdict, namedtuple
import heapq


class Graph(object):
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        # undirected graph
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def dijkstra2(self, src):
        res = defaultdict(list)
        visited = [False]*self.vertices
        mh = list()
        heapq.heapify(mh)
        heapq.heappush(mh, (0, src, ""+str(src)))
        while mh:
            distance, vertex, path = heapq.heappop(mh)
            if not visited[vertex]:
                visited[vertex] = True
                res[vertex] = [distance, path]
                for nei in self.graph[vertex]:
                    if not visited[nei[0]]:
                        heapq.heappush(mh, (distance+nei[1], nei[0], path+str(nei[0])))
        
        print("Vertex\tDistance\tPathFromSrc")
        for key, val in res.items():
            print(key, "\t\t ", val[0], "\t\t\t", val[1])

    def dijkstra(self, src):
        vd = namedtuple("vertexPath", ["vertex", "pathFromSrc"])
        res = defaultdict(list)
        visited = [False]*self.vertices
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, vd(vertex=src, pathFromSrc=""+str(src))))
        while len(minHeap) > 0:
            distance, pair = heapq.heappop(minHeap)
            # print pair
            if not visited[pair.vertex]:
                visited[pair.vertex] = True
                res[pair.vertex] = [distance, pair.pathFromSrc]
                for neighbour in self.graph[pair.vertex]:
                    if not visited[neighbour[0]]:
                        heapq.heappush(minHeap, (distance+neighbour[1], vd(vertex=neighbour[0], pathFromSrc=pair.pathFromSrc+str(neighbour[0]))))

        print("Vertex\tDistance\tPathFromSrc")
        for key, val in res.items():
            print(key, "\t\t ", val[0], "\t\t\t", val[1])


if __name__ == '__main__':
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
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
    g.add_edge(7, 8, 7)
    g.dijkstra(0)
    g.dijkstra2(0)
