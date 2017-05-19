import sys


class Vertex:
    def __init__(self):
        self.id = node
        self.


def file_loader(filename):
    f = open(filename, 'r')
    graph_data = []
    for line in f:
        graph_data.append(line)
    return graph_data


def graph_data_printer(graph_data):
    for line in graph_data:
        print(line.rstrip('\n'))


def main():
    graph_data1 = file_loader('Case1.txt')
    graph_data_printer(graph_data1)


if __name__ == "__main__":
    sys.exit(main())