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

    def add_edge(self, u, v, bidirectional=True):
        if not isinstance(u, Vertex):
            raise Exception('You can only have edge between vertices')

        if not isinstance(v, Vertex):
            raise Exception('You can only have edge between vertices')

        if u.name not in self.vertices or v.name not in self.vertices:
            raise Exception('Vertex doesn\' exist')

        self.vertices[u.name].add_neighbour(v)

        if bidirectional:
            self.vertices[v.name].add_neighbour(u)


if __name__ == '__main__':
    graph = Graph()

    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')
    g = Vertex('G')
    h = Vertex('H')

    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_vertex(d)
    graph.add_vertex(e)
    graph.add_vertex(f)
    graph.add_vertex(g)
    graph.add_vertex(h)

    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(b, c)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(e, g)
    graph.add_edge(e, f)
    graph.add_edge(f, g)
    graph.add_edge(b, c)
    graph.add_edge(f, a)
    graph.add_edge(h, a)
