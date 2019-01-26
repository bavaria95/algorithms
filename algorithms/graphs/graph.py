class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = set()

    def add_neighbour(self, v):
        if not isinstance(v, Vertex):
            raise Exception('Only another vertex can be a neighbour')

        self.neighbours.add(v)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v):
        if not isinstance(v, Vertex):
            raise Exception('You can only add vertices to the graph')

        if v.name in self.vertices:
            raise Exception('Vertex is already present')

        self.vertices[v.name] = v

    def add_edge(self, u, v):
        if not isinstance(u, Vertex):
            raise Exception('You can only have edge between vertices')

        if not isinstance(v, Vertex):
            raise Exception('You can only have edge between vertices')

        if u.name not in self.vertices or v.name not in self.vertices:
            raise Exception('Vertex doesn\' exist')

        self.vertices[u.name].add_neighbour(v)
        self.vertices[v.name].add_neighbour(u)

