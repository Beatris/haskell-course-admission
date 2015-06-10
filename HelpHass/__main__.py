from graph_constructor import GraphConstructor


routes = []

# Procces the input:
print("Input:")
while True:
    input_str = raw_input("> ")
    route = input_str.split(" ")
    if input_str == "":
        break
    else:
        routes.append(route)

# Construct the graph:
graph_constructor = GraphConstructor(routes)
graph = graph_constructor.construct_graph()

