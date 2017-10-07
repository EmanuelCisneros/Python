import math
import queue as Q

inf = math.inf


class Graph:
    def __init__(self, v, e):
        self.__v = v
        self.__e = e
        self.__adj_list = [[] for i in range(self.__v)]
        self.__dist = [inf] * self.__v

    def add_edge(self, u, v, w):
        self.__adj_list[u].append([v, w])
        self.__adj_list[v].append([u, w])

    def shortest_path(self, src):
        pq = Q.PriorityQueue()
        pq.put((0, src))
        self.__dist[src] = 0

        while not pq.empty():
            u = pq.get()[1]
            for i in self.__adj_list[u]:
                v = i[0]
                weight = i[1]
                if self.__dist[v] > self.__dist[u] + weight:
                    self.__dist[v] = self.__dist[u] + weight
                    pq.put((self.__dist[v], v))

    def print_distances(self, src, end):
        print("Vertex\t Min distance from src")
        for j in range(len(self.__dist)):
            print(j, "\t\t\t\t", self.__dist[j])


def main():

    print("Number of vertices and edges: ", end="")
    v, e = list(map(int, input().split()))

    g = Graph(v, e)
    print("Src (start point) and end point: ", end="")
    src, end = list(map(int, input().split()))

    for i in range(e):
        print("start vertex, end vertex and weight: ", end="")
        vi, vf, w = list(map(int, input().split()))
        g.add_edge(vi, vf, w)

    g.shortest_path(src)
    g.print_distances(src, end)


if __name__ == '__main__':
    main()