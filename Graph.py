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

    def show_matrix(self):
        # Wyświetlenie grafu incydencji.
        print('\n'.join([' '.join(['{:3}'.format(item) for item in row]) for row in self.graph]))

    def bfs(self, start_node):
        visited = set()
        queue = [start_node]

        # node_index = 0
        # for edge in self.graph[node]:
        #     if edge == 1:
        #         queue.append(node_index)
        #     node_index += 1

        while queue:
            node = queue.pop(0)

            if node not in visited:
                visited.add(node)

                for edge in enumarate(self.graph[node]:
                    pass

        return visited
