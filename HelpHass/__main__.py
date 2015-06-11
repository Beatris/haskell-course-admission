from graph_constructor import GraphConstructor
from fastest_route_calculator import FastestRouteCalculator


START_STATION = 'H'
END_STATION = 'L'
routes = []

# Procces the input:
print "Input:"
while True:
    input_str = raw_input()
    route = input_str.split(" ")
    if input_str == "":
        break
    else:
        routes.append(route)

# Construct the graph:
graph_constructor = GraphConstructor(routes)
graph = graph_constructor.construct_graph()

# Find the shortest path between given nodes:
fastest_route_calculator =\
    FastestRouteCalculator(graph, START_STATION, END_STATION)

fastest_route = fastest_route_calculator.find_fastest_route()
print "Output:"
print ' '.join(fastest_route)
