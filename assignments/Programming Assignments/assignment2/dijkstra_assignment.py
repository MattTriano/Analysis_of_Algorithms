import sys


# vertex.pi: predecessor vertex
class Vertex:
    def __init__(self, node):
        self.id = node
        self.pi = None
        self.path_dist = sys.maxsize  # an approximation for infinity
        self.adj = {}

    def add_adjacent(self, adjacent, weight=0):
        self.adj[adjacent] = weight

    def set_prev(self, prev):
        self.pi = prev

    def get_dist(self):
        return self.path_dist

    def get_prev(self):
        return self.pi

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def set_num_vertices(self, num_vertices):
        self.num_vertices = num_vertices

    def add_vertex(self, node):
        this_vertex = Vertex(node)
        self.vertices[node] = this_vertex

    def get_vertex(self, node):
        if node in self.vertices:
            return self.vertices[node]
        else:
            return None

    def add_edge(self, node_a, node_b, pair_dist):
        if node_a not in self.vertices:
            self.add_vertex(node_a)
        if node_b not in self.vertices:
            self.add_vertex(node_b)
        self.vertices[node_a].add_adjacent(self.vertices[node_b], pair_dist)
        self.vertices[node_b].add_adjacent(self.vertices[node_a], pair_dist)

    def get_vertices(self):
        return self.vertices


def file_loader(filename):
    f = open(filename, 'r')
    graph_data = []
    for line in f:
        graph_data.append(line)
    return graph_data


def graph_data_printer(graph_data):
    for line in graph_data:
        print(line.rstrip('\n'))

def make_graph(filename):
    graph_data = file_loader(filename)
    lines = len(graph_data)
    network = Graph()
    for i in range(lines):
        line = graph_data[i]
        if i >= 1:
            parts = line.split(' ')
            network.add_edge(parts[0], parts[1], int(parts[2]))
        elif i == 0:
            network.set_num_vertices(int(line))
    



def main():
    graph_data1 = file_loader('Case1.txt')
    graph_data_printer(graph_data1)


if __name__ == "__main__":
    sys.exit(main())