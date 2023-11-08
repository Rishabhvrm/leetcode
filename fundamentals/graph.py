class Graph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def __str__(self):
        return str(self.graph)



if __name__ == "__main__":
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")

    g.add_edge("A","B")
    g.add_edge("A","C")
    g.add_edge("A","D")
    g.add_edge("C","D")
    g.add_edge("B","D")
    g.add_edge("C","B")
    g.add_edge("D","D")

    print(g)