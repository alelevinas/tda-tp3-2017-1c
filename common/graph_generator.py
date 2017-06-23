import random

random.seed()
FILE_NAME = "assign-tmp"


def generate_connected_graph(n, e, file_name=FILE_NAME):
    edges = []
    edge_set = set()

    add_random_edges(e, edges, n, edge_set)

    with open(file_name + ".txt", "w") as f:
        f.write(str(n) + "\n")  # Vertices
        f.write(str(e) + "\n")  # Vertices
        [f.write("{} {}\n".format(edg[0], edg[1])) for edg in edges]


def add_edge(edge, edge_set, edges):
    """Add the edge if the graph type allows it."""
    if edge not in edge_set:
        edges.append(edge)
        edge_set.add(edge)
        edge_set.add(edge[::-1])  # add other direction to set.
        return True
    return False


def make_random_edge(nodes):
    """Generate a random edge between any two nodes in the graph."""
    random_edge = tuple(random.sample([i for i in range(nodes)], 2))
    return random_edge


def add_random_edges(total_edges, edges, nodes, edge_set):
    """Add random edges until the number of desired edges is reached."""
    act_nodes = 1
    while len(edges) < total_edges:
        if act_nodes < nodes:
            random_connected_edge = (random.randrange(act_nodes), act_nodes)
            print(random_connected_edge)
            add_edge(random_connected_edge, edge_set, edges)
            act_nodes += 1
        else:
            add_edge(make_random_edge(nodes), edge_set, edges)


def main(argv):
    generate_connected_graph(int(argv[0]), int(argv[0])*2, argv[1])

if __name__ == "__main__":
    main(("10", "10"))

'''
FORMATO DE GRAFO
10 # N°vertices
20 # N°edges
1 0 0.12 #start end weight
5 4 0.90
7 6 0.79
0 1 0.46
6 7 0.12
1 3 0.76
3 6 0.46
0 4 0.23
4 8 0.367
0 5 0.35
4 9 0.3
0 6 0.67
2 8 0.456
0 9 0.345
9 0 0.123
9 1 0.98
8 2 0.76
5 0 0.36
7 3 0.35
6 3 0.4
'''
