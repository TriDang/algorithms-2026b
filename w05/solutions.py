from examples import MatrixGraph, ListGraph

# Problem 1
# Implement a graph data structure to model a collection of one-way streets

# Solution: you can modify the examples.py to represent one-way streets. For example, you can modify the add_edge method to only add an edge from u to v, but not from v to u. Then you can use BFS or DFS to traverse the graph and find paths between nodes.

# Problem 2
# Implement an algorithm to check if an undirected graph is connected.

# Idea: you can use BFS or DFS to traverse the graph from any starting node.
# If you can visit all nodes, then the graph is connected. Otherwise, it is not connected.

# Below is an implementation of the above idea using DFS
# We will modify the DFS algorithm to count the number of visited nodes in one DFS traversal
# and then compare it with the total number of nodes in the graph.
# If they are equal, then the graph is connected.

def dfs(graph):
    visited = [False] * graph.num_vertices
    total_visited = dfs_recursive(graph, 0, visited) # start DFS from vertex 0
    return total_visited == graph.num_vertices

def dfs_recursive(graph, vertex, visited):
    visited[vertex] = True
    total_visited = 1  # Count the current vertex
    for neighbor in graph.adjacency_list[vertex]:
        if not visited[neighbor]:
            total_visited += dfs_recursive(graph, neighbor, visited)
    return total_visited

# test
# Create the graph on slide 35 of the lecture
# With some edges removed to make it disconnected
# A = 0, B = 1, C = 2, D = 3, E = 4
graph3 = ListGraph(5)
graph3.add_edge(0, 1) # A-B
graph3.add_edge(0, 2) # A-C
graph3.add_edge(0, 4) # A-E
# print("Is the graph connected?", dfs(graph3)) # False
graph3.add_edge(2, 3) # C-D
# print("Is the graph connected?", dfs(graph3)) # True

# Problem 3
# In a graph G, find a path from a node A to another node B using DFS and BFS
# The path should not visit any node more than once

# Idea: you can modify the BFS and DFS algorithms to add a parent pointer to keep track of the 
# previous vertex of each visited vertex. This way, when you reach the target node B
# you can backtrack using the parent pointers to construct the path from A to B
# If you finish the traversal without finding B, then there is no path from A to B

def bfs_path(graph, start, target):
    visited = [False] * graph.num_vertices
    parent = [None] * graph.num_vertices
    queue = [start]
    visited[start] = True
    while queue:
        current_vertex = queue.pop(0)
        if current_vertex == target:
            # backtrack to construct the path
            path = []
            while current_vertex != start:
                path.append(current_vertex)
                current_vertex = parent[current_vertex]
            path.append(start)
            return path
        for neighbor in range(graph.num_vertices):
            if graph.has_edge(current_vertex, neighbor) and not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current_vertex
                queue.append(neighbor)
    return None  # no path found

# test
# path from A to D
# print("Path from A to D:", bfs_path(graph3, 0, 3)) # [A -> C -> D] [3, 2, 0] backward direction
# path from A to E
# print("Path from A to E:", bfs_path(graph3, 0, 4)) # [A -> C -> E] [4, 0] backward direction

# Problem 4
# RMIT needs to schedule final exams over two days. If two courses share at least one student, their exams cannot be scheduled on the same day. Given the list of courses and their conflict pairs, determine whether it is possible to schedule all exams without conflicts.

# This is a bipartite graph problem
# We can represent the courses as vertices and the conflicts as edges
# Then we can use a graph coloring algorithm to check if the graph can be colored with two colors
# (representing the two days). If it can be colored with two colors,
# then it is possible to schedule the exams without conflicts. Otherwise, it is not possible.

# Idea: Use BFS/DFS and start with any vertex, color it with one color (e.g., 0)
# and then color all its neighbors with the other color (e.g., 1)
# If we find a neighbor that is already colored with the same color
# then the graph is not bipartite

def is_bipartite(graph):
    schedule = [None] * graph.num_vertices
    for vertex in range(graph.num_vertices):
        if schedule[vertex] is None:
            schedule[vertex] = "Day 1"  # start coloring with Day 1
            if not dfs_color(graph, vertex, schedule):
                print("Not possible to schedule exams without conflicts.")
                return
    print("Possible to schedule exams without conflicts.")
    day1 = []
    day2 = []
    for i in range(graph.num_vertices):
        if schedule[i] == "Day 1":
            day1.append(i)
        else:
            day2.append(i)
    print("Day 1:", day1)
    print("Day 2:", day2)

def dfs_color(graph, vertex, schedule):
    possible = True
    for neighbor in graph.adjacency_list[vertex]:
        if schedule[neighbor] is None:
            # color with the opposite color
            schedule[neighbor] = "Day 2" if schedule[vertex] == "Day 1" else "Day 1"
            possible &= dfs_color(graph, neighbor, schedule)
        elif schedule[neighbor] == schedule[vertex]:
            # found a neighbor with the same color, not bipartite
            return False
    return possible

# test
# Example 1
# Courses: A, B, C, D
# Conflicts: A - B, B - C
# Answer: Possible (e.g., Day 1: A, C; Day 2: B, D)
example1 = ListGraph(4)
example1.add_edge(0, 1) # A-B
example1.add_edge(1, 2) # B-C
print("Example 1:")
is_bipartite(example1) # Possible to schedule exams without conflicts

# Example 2
# Courses: A, B, C
# Conflicts: A - B, B - C, C - A
# Answer: Not possible
example2 = ListGraph(3)
example2.add_edge(0, 1) # A-B
example2.add_edge(1, 2) # B-C
example2.add_edge(2, 0) # C-A
print("Example 2:")
is_bipartite(example2) # Not possible to schedule exams without conflicts

# Example 3
# Courses: A, B, C, D, E
# Conflicts: A - B, A - C, D - E
# Answer: Possible (e.g., Day 1: A, D; Day 2: B, C, E)
example3 = ListGraph(5)
example3.add_edge(0, 1) # A-B
example3.add_edge(0, 2) # A-C
example3.add_edge(3, 4) # D-E
print("Example 3:")
is_bipartite(example3) # Possible to schedule exams without conflicts