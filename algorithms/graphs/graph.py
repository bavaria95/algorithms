class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = set()

    def add_neighbour(self, v):
        if not isinstance(v, Vertex):
            raise Exception('Only another vertex can be a neighbour')

        self.neighbours.add(v)
