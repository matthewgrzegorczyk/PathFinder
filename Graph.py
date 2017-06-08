
# See incidence matrix: http://eduinf.waw.pl/inf/alg/001_search/0124.php 

class Graph():

    graph = {}
    def __init__(self, connections, cities):
        self.graph = [[0 for x in range(len(connections))] for y in range(int(len(cities)))]
        for (i, key) in enumerate(connections.keys()):
            ab = key.split(',')
            a = ab[0]
            b = ab[1]
            self.graph[int(a)][i] = 1
            self.graph[int(b)][i] = -1