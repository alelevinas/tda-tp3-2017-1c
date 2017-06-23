class Graph:
    """
    Grafo dirigido con un número fijo de vértices.

    Los vértices son siempre números enteros no negativos. El primer vértice
    es 0.

    El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
    creadas, las aristas no se pueden eliminar, pero siempre se pueden añadir
    nuevas aristas.
    """

    def __init__(self, v):
        if v < 0:
            raise ValueError("El numero de vertices en un grafo debe ser mayor a cero")
        self.v = v
        self.e = 0
        self.adj = {}               # lista de adyascencia de Edges
        for i in range(v):
            self.adj[i] = []

    def V(self):
        return self.v

    def E(self):
        return self.e

    def validate_vertex(self, v):
        """
        Valida la existencia del vertice en el grafo
        :param v: el vertice
        :return: None
        :raises ValueError si :param v no esta en el grafo
        """
        if v < 0 or v >= self.V():
            raise ValueError("El vertice no esta entre 0 y {}".format(self.V()))

    def add_edge(self, u, v, weight = 0):
        """
        Agrega una arista desde u hasta v al grafo.
        :param u: vertice fuente
        :param v: vertice destino
        :param weight: peso de la arista
        :return: None
        :raises ValueError si :param u o :param v no estan en el grafo
        """
        self.validate_vertex(u)
        self.validate_vertex(v)
        self.adj[u].append(Edge(u, v, weight))
        self.e += 1

    def adj_e(self, v):
        """
        Devuelve una lista con todas las aristas incidentes de v (v -> w)
        :param v: numero de vertice
        :return: una lista con todas las aristas incidentes de v (v -> w)
        :raises ValueError si :param v no esta en el grafo
        """
        self.validate_vertex(v)
        return self.adj[v]

    def adj_list(self,v):
        """
        Devuelve una lista con los vertices adjacentes a v
        :param v: el vertice
        :return: lista con los vertices adjacentes a v
        :raises ValueError si :param v no esta en el grafo
        """
        self.validate_vertex(v)
        return [e.dst for e in self.adj[v]]

    def __iter__(self):
        """
        Itera de 0 a V.
        :return: un iterable de los vertices del grafo
        """
        return iter(range(self.V()))

    def iter_edges(self):
        """
        Itera sobre todas las aristas del grafo.

        Las aristas devueltas tienen los siguientes atributos de solo lectura:
                • e.src
                • e.dst
                • e.weight
        :return: un iterable de las aristas del grafo
        """
        return iter([e for v in range(self.V()) for e in self.adj[v]])

    def __str__(self):
        """
        Devuelve una representacion en string del grafo
        :return: una representacion en string del grafo
        """
        g = "{} vertices, {} edges\n".format(self.V(), self.E())
        for v in self.adj:
            g += "{}: {}\n".format(v, str(self.adj_list(v)))
        return g

    def __len__(self):
        return self.v


class Edge:
    """
    Arista de un grafo.
    """
    def __init__(self, src, dst, weight = 0):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __str__(self):
        return "Edge from " + self.src + "to " + self.dst + ", weight: " + str(self.weight)


def create_graph_from_file(file, is_directed=True):
    with open(file, "r") as file:
        num_v = int(file.readline())
        num_e = int(file.readline())
        g = Digraph(num_v)
        for i in range(num_e):
            vertexes = file.readline().split()
            u, v = int(vertexes[0]), int(vertexes[1])
            weight = float(vertexes[2]) if len(vertexes) >= 3 else 0
            g.add_edge(u, v, weight)
            if not is_directed:
                g.add_edge(v, u, weight)
    return g
