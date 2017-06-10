# See incidence matrix: http://eduinf.waw.pl/inf/alg/001_search/0124.php

class Graph():
    graph = {}
    adjacency_matrix = {}

    def __init__(self, connections, cities):
        self.graph = [[0 for x in range(len(connections))] for y in range(int(len(cities)))]
        for (i, key) in enumerate(connections.keys()):
            ab = key.split(',')
            a = ab[0]
            b = ab[1]
            self.graph[int(a)][i] = 1
            self.graph[int(b)][i] = -1

    def create_adjacency_matrix(self, connections, cities):
        for key, city in enumerate(cities):
            self.adjacency_matrix[key] = set([])

        for conn in connections:
            nodes = conn.split(',')
            nodeA = int(nodes[0])
            nodeB = int(nodes[1])

            try:
                self.adjacency_matrix[nodeA].add(nodeB)
                self.adjacency_matrix[nodeB].add(nodeA)
            except KeyError:
                pass

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

                # for edge in enumarate(self.graph[node]:
                #     pass

        return visited

    def bfs_adj(self, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.adjacency_matrix[vertex] - visited)
        return visited

    def bfs_paths_adj(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.adjacency_matrix[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))

    def shortest_path(self, start, goal):
        try:
            return next(self.bfs_paths_adj(start, goal))
        except StopIteration:
            return None
