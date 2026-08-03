# Graph representatio with adjacency matrix
class MatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1  # assume this is an undirected graph
    
    def has_edge(self, u, v):
        return self.adjacency_matrix[u][v] == 1

# create the graph on slide 35 of the lecture
# A = 0, B = 1, C = 2, D = 3, E = 4
graph = MatrixGraph(5)
graph.add_edge(0, 1) # A-B
graph.add_edge(0, 2) # A-C
graph.add_edge(0, 4) # A-E
graph.add_edge(2, 3) # C-D
graph.add_edge(2, 4) # C-E
graph.add_edge(3, 4) # D-E

# BFS on the graph
def bfs(graph):
    visited = [False] * graph.num_vertices
    for start in range(graph.num_vertices):
        if not visited[start]:
            # start BFS from vertex start
            queue = [start]
            visited[start] = True
            while queue:
                current_vertex = queue.pop(0)
                print(current_vertex) # this is the "visit" operation
                for neighbor in range(graph.num_vertices):
                    if graph.has_edge(current_vertex, neighbor) and not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

# print("BFS on the graph starting from vertex A:")
# bfs(graph) # start BFS from vertex A: 0(A), 1(B), 2(C), 4(E), 3(D)

# Graph representatio with adjacency list
class ListGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # assume this is an undirected graph
    
    def has_edge(self, u, v):
        return v in self.adjacency_list[u]

# create the graph on slide 35 of the lecture
# A = 0, B = 1, C = 2, D = 3, E = 4
graph2 = ListGraph(5)
graph2.add_edge(0, 1) # A-B
graph2.add_edge(0, 2) # A-C
graph2.add_edge(0, 4) # A-E
graph2.add_edge(2, 3) # C-D
graph2.add_edge(2, 4) # C-E
graph2.add_edge(3, 4) # D-E

# DFS on the second graph using recursion
def dfs(graph):
    visited = [False] * graph.num_vertices
    for start in range(graph.num_vertices):
        if not visited[start]:
            dfs_recursive(graph, start, visited)

def dfs_recursive(graph, vertex, visited):
    visited[vertex] = True
    print(vertex)  # this is the "visit" operation
    for neighbor in graph.adjacency_list[vertex]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)

# print("DFS on the graph starting from vertex A:")
# dfs(graph2) # start DFS from vertex A: 0(A), 1(B), 2(C), 3(D), 4(E)