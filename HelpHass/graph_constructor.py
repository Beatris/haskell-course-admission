class GraphConstructor():

    def __init__(self, routes):
        self.routes = routes

    def construct_graph(self):
        '''
        Construct a graph in a form of list
        by given routes.
        '''
        graph = {}
        for route in self.routes:
            node = route[0]
            arc = route[1]
            if node not in graph.keys():
                graph[node] = arc
            else:
                graph[node] = list(graph[node])
                graph[node].append(arc)

        return graph
