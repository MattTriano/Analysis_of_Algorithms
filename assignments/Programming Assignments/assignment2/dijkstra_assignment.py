import sys
from heapq import heapify, heappop


# vertex.pi: predecessor vertex
class Vertex:
    def __init__(self, node):
        self.id = node
        self.prev = None
        self.path_dist = sys.maxsize  # an approximation for infinity
        self.adj = {}
        self.explored = False

    def __repr__(self):
        return 'Vertex ' + str(self.id)

    def __lt__(self, other):
        return self.get_path_dist() < other.get_path_dist()

    def get_id(self):
        return self.id

    def get_path_dist(self):
        return self.path_dist

    def set_path_dist(self, dist):
        self.path_dist = dist

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def set_explored(self):
        self.explored = True

    def get_adjacent_vertices(self):
        return self.adj.keys()

    def get_edge_weight(self, adj_node):
        return self.adj[adj_node]

    def add_adjacent(self, adjacent, edge_weight=0):
        self.adj[adjacent] = edge_weight


    def adj_print(self):
        adj = []
        pretty_adj = []
        for adj_node in self.get_adjacent_vertices():
            adj.append(str(adj_node) + ' (dist = ' + str(self.get_edge_weight(adj_node)) + ')')
        num_adj = len(adj)
        if num_adj > 0:
            pretty_adj.append(' is adjacent to ')
            for i in range(num_adj):
                if i == 0:
                    pretty_adj.append(adj[i])
                elif i == num_adj - 1:
                    pretty_adj.append(', and ' + adj[i])
                else:
                    pretty_adj.append(', ' + adj[i])
            pretty_adj_string = ''.join(pretty_adj)
        else:
            pretty_adj_string = ' is not adjacent to any nodes.'
        print(self.id + pretty_adj_string)


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.get_vertices())

    def get_vertices(self):
        return self.vertices

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
        # self.vertices[node_b].add_adjacent(self.vertices[node_a], pair_dist)


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
    return network


def graph_printer(graph):
    for node_id in graph.get_vertices():
        node = graph.get_vertex(node_id)
        node.adj_print()


def relax(node_tail, node_head):
    relaxed_path_dist = node_tail.get_path_dist() + node_tail.get_edge_weight(node_head)
    if node_head.get_path_dist() > relaxed_path_dist:
        node_head.set_path_dist(relaxed_path_dist)
        node_head.set_prev(node_tail)


def shortest_path_dijkstras(graph_filename, start_node, end_node):
    graph = make_graph(graph_filename)
    graph.get_vertex(start_node).set_path_dist(0)
    unexplored_node_heap = []
    # shortest_path = []
    for node_id in graph.get_vertices():
        node = graph.get_vertex(node_id)
        unexplored_node_heap.append(node)
    heapify(unexplored_node_heap)
    while unexplored_node_heap:
        node_u = heappop(unexplored_node_heap)
        node_u.set_explored()
        # shortest_path.append(node_u)
        if node_u == graph.get_vertex(end_node):
            return graph

        for adj_node in node_u.get_adjacent_vertices():
            if not adj_node.explored:
                relax(node_u, adj_node)
        heapify(unexplored_node_heap)

    return None


def path_printer(graph, end_node):
    path = []
    node = graph.get_vertex(end_node)
    path_length = node.get_path_dist()
    while node:
        path.extend(node.get_id())
        if node.get_prev():
            path.extend(' ')
        node = node.get_prev()
    path = path.reverse()
    path = ''.join(path)
    print(path_length)
    print(path)



def main():
    # graph_data1 = make_graph('Case1.txt')
    # graph_printer(graph_data1)
    path = shortest_path_dijkstras('Case1.txt', 'A', 'B')
    path_printer(path, 'B')
    # graph_data_printer(graph_data1)
    print('hi')


if __name__ == "__main__":
    sys.exit(main())