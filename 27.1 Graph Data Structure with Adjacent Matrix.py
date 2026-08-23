class Graph:
    def __init__(self, vertex):
        self.vertex_count = vertex
        self.adj_matrix = [[0]*vertex for v in range(0, vertex)]

    def add_edge(self, node1, node2):
        if node1-1 < self.vertex_count and node2-1 < self.vertex_count:

            self.adj_matrix[node1-1][node2-1] = 1
            self.adj_matrix[node2-1][node1-1] = 1
        
        else:
            print("Invalid Vertex")
    
    def remove_edge(self, node1, node2):
        if node1-1 < self.vertex_count and node2-1 < self.vertex_count:

            self.adj_matrix[node1-1][node2-1] = 0
            self.adj_matrix[node2-1][node1-1] = 0
        else:
            print("Invalid Vertex")
        
    def has_edge(self, node1, node2):
        if node1-1 < self.vertex_count and node2-1 < self.vertex_count:

            if self.adj_matrix[node1-1][node2-1]:
                print("Nodes are connected")
            
            else:
                print("Nodes are not connected directly")
        else:
            print("Invalid Vertex")

    def print_adj_matrix(self):
        for i in range(0, len(self.adj_matrix)):
            for j in range(0, len(self.adj_matrix)):
                print(f"{self.adj_matrix[i][j] } ", end="")

            print()
        print("GRAPH PRINTED SUCCESSFULLY")

    
graph = Graph(5)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.print_adj_matrix()
graph.remove_edge(1, 3)
graph.print_adj_matrix()
