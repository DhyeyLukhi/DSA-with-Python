class Graph:
    def __init__(self, vtx):
        self.vertex = vtx
        self.graph = {v+1:[0*v for v in range(vtx)] for v in range(vtx)}
        self.graph2 = {0: [0, 0, 0, 0, 0]}

    def addEdge(self, node1, node2):
        if node1 < self.vertex and node2-1 < self.vertex:
            self.graph[node1][node2-1] = 1   
            self.graph[node2][node1-1] = 1   
    
    def removEdge(self, node1, node2):
        if node1 < self.vertex and node2-1 < self.vertex:
            self.graph[node1][node2-1] = 0 
            self.graph[node2][node1-1] = 0
    
    def hasEdge(self, node1, node2):
        if self.graph[node1][node2-1] == 1:
            print(f"Node {node1} and {node2} are connected")
        
        else:
            print(f"Node {node1} and {node2} are not connected directly")
    
    def printGraph(self):
        for v in range(self.vertex):
            print(f"Node {v+1}: {self.graph[v+1]}")


myGraph = Graph(5)
myGraph.addEdge(2, 3)
myGraph.addEdge(3, 4)
myGraph.addEdge(1, 5)
myGraph.printGraph()
