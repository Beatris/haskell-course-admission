class FastestRouteCalculator():

    def __init__(self, graph, start, end, path=''):
        self.graph = graph
        self.start = start
        self.end = end
        self.path = path
        self.paths = []

    def find_all_routes(self, graph, start, end, path=''):
        '''
        Find all possible paths between
        two nodes in a graph.
        '''
        paths = []
        path = list(path) + [start]

        for node in graph[start]:
            if node not in path:
                if (node in graph) and (node != end):
                    new_paths = self.find_all_routes(graph, node, end, path)
                    for new_path in new_paths:
                        paths.append(new_path)
                else:
                    new_path = path + [node]
                    paths.append(new_path)
        return paths

    def find_fastest_route(self):
        '''
        Find the shortest path from all
        possible paths between nodes in a graph.
        '''
        self.paths =\
         self.find_all_routes(self.graph, self.start, self.end, self.path)

        fastest_route = min(self.paths, key=len)
        return fastest_route