class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # For Kruskal (Edge List)
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.node_names = []

    def add_node_names(self, names):
        """Assign human-readable names to vertices."""
        self.node_names = names

    def add_edge(self, u, v, w):
        """Add edge between node u and v with weight w"""
        self.graph.append([u, v, w])
        self.adj_matrix[u][v] = w
        self.adj_matrix[v][u] = w

    def print_adj_matrix(self):
        """Display adjacency matrix"""
        print("\nAdjacency Matrix:")
        print("     " + "  ".join(f"{name[:3]}" for name in self.node_names))
        for i, row in enumerate(self.adj_matrix):
            print(f"{self.node_names[i][:3]}:  " + "  ".join(f"{val:2}" for val in row))

    def adjacency_list(self):
        """Convert adjacency matrix to adjacency list"""
        adj_list = {self.node_names[i]: [] for i in range(self.V)}
        for i in range(self.V):
            for j in range(self.V):
                if self.adj_matrix[i][j] != 0:
                    adj_list[self.node_names[i]].append((self.node_names[j], self.adj_matrix[i][j]))
        return adj_list

    # ---------- Kruskal’s Algorithm ----------
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []  # Store MST edges
        i, e = 0, 0  # i: edge counter, e: result counter
        self.graph = sorted(self.graph, key=lambda item: item[2])  # sort edges by weight

        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        total_weight = sum(w for _, _, w in result)
        print("\n📘 Kruskal’s Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"  {self.node_names[u]} -- {self.node_names[v]}  ({weight} m)")
        print(f"➡️ Total Minimum Distance: {total_weight} m")

    # ---------- Prim’s Algorithm ----------
    def prim_mst(self):
        selected = [False] * self.V
        no_edge = 0
        selected[0] = True
        print("\n📗 Prim’s Minimum Spanning Tree:")
        total_weight = 0

        while no_edge < self.V - 1:
            minimum = float('inf')
            x = 0
            y = 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if (not selected[j]) and self.adj_matrix[i][j]:
                            if minimum > self.adj_matrix[i][j]:
                                minimum = self.adj_matrix[i][j]
                                x = i
                                y = j
            print(f"  {self.node_names[x]} -- {self.node_names[y]}  ({self.adj_matrix[x][y]} m)")
            total_weight += self.adj_matrix[x][y]
            selected[y] = True
            no_edge += 1
        print(f"➡️ Total Minimum Distance: {total_weight} m")


# -------------------------------------------
# Example: College Campus Graph
# -------------------------------------------

# Define departments/buildings
names = ["Admin", "CS Dept", "AIML Dept", "Library", "Canteen", "Workshop"]

# Create graph
g = Graph(len(names))
g.add_node_names(names)

# Add weighted edges (distances in meters)
g.add_edge(0, 1, 10)  # Admin - CS
g.add_edge(0, 2, 15)  # Admin - AIML
g.add_edge(1, 3, 12)  # CS - Library
g.add_edge(2, 3, 13)  # AIML - Library
g.add_edge(1, 4, 15)  # CS - Canteen
g.add_edge(3, 5, 5)   # Library - Workshop
g.add_edge(4, 5, 10)  # Canteen - Workshop

# Display representations
g.print_adj_matrix()

print("\nAdjacency List:")
for k, v in g.adjacency_list().items():
    print(f" {k} -> {v}")

# Run MST Algorithms
g.kruskal_mst()
g.prim_mst()





# Experiment No 5: Minimum Spanning Tree (MST) of College Campus Graph
# COs: CO1, CO2, CO3
# Aim
# Represent a graph of the college campus using adjacency list / adjacency matrix, where nodes represent
# departments and edges represent distances. Find the Minimum Spanning Tree (MST) using:
# 1. Kruskal’s Algorithm
# 2. Prim’s Algorithm
# Objectives
# ● Understand graph representation using adjacency list and matrix.
# ● Learn how to compute MST using Kruskal’s and Prim’s algorithms.
# ● Apply greedy approach to find minimum total distance connecting all departments.
# ● Compare results from Kruskal’s and Prim’s algorithms.
# Graph Representation
# Graphs can be represented in mainly two ways:
# 1. Adjacency Matrix
# 2. Adjacency List
# 1. Adjacency Matrix
# ● Definition:
# An adjacency matrix is a 2D array (matrix) of size V × V (where V = number of vertices).
# Each cell (i, j) indicates whether there is an edge between vertex i and vertex j.
# ● Structure:
# ○ For an undirected graph: Matrix is symmetric.
# ○ For directed graph: Entry (i, j) may not be equal to (j, i).
# ○ If weighted graph: The entry stores the weight instead of just 1.
# ● Representation:
# ○ adj[i][j] = 1 → edge exists between i and j
# ○ adj[i][j] = 0 → no edge between i and j

# Example:
# For graph with vertices {A, B, C} and edges {A-B, B-C}:
#  A B C
# A 0 1 0
# B 1 0 1
# C 0 1 0
# ● Complexity:
# ○ Space: O(V^2)
# ○ Check edge existence: O(1)
# ○ Traversing neighbors of a vertex: O(V)
# ● Advantages:
# ○ Very simple and easy to implement.
# ○ Fast to check if an edge exists (direct lookup).
# ○ Useful when graph is dense (many edges).
# ● Disadvantages:
# ○ Requires large space even if graph has few edges.
# ○ Iterating over neighbors is less efficient.
# 2. Adjacency List
# ● Definition:
# An adjacency list is a list of lists where each vertex stores a list of its adjacent vertices.
# ● Structure:
# ○ Usually implemented using linked list or dynamic arrays (like vector in C++).
# ○ For weighted graph: store pair (neighbor, weight).
# ● Representation:
# Graph with vertices {A, B, C} and edges {A-B, B-C}:
# A → B
# B → A, C
# C → B

# ● Complexity:
# ○ Space: O(V + E) (much better for sparse graphs).
# ○ Check edge existence: O(degree of vertex)
# ○ Traversing neighbors: proportional to number of neighbors.
# ● Advantages:
# ○ Efficient in space for sparse graphs.
# ○ Easy to iterate over neighbors.
# ○ Widely used in graph algorithms like BFS, DFS, Dijkstra, Kruskal, etc.
# ● Disadvantages:
# ○ Slower edge existence check compared to adjacency matrix.
# ○ Implementation slightly more complex.
# Comparison: Adjacency Matrix vs Adjacency List
# Feature Adjacency Matrix Adjacency List
# Space Complexity O(V^2) O(V + E)
# Edge Existence Check O(1) O(degree of vertex)
# Traversal (neighbors) O(V) O(degree of vertex)
# Best for Dense graphs Sparse graphs
# Ease of Implementation Very easy Slightly complex
# Memory Use High (even if few edges exist) Low (proportional to edges)
# Applications Graphs with many edges, quick
# checks
# Graph algorithms, real-world
# networks
#  NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 4 Asst.Prof.Salunkhe A.A
# Minimum Spanning Tree (MST)
#  A Spanning Tree of a graph is a subgraph that:
# 1. Includes all vertices of the graph.
# 2. Is a tree (connected and acyclic).
# ● A Minimum Spanning Tree (MST) is a spanning tree in which the sum of edge weights is
# minimum among all possible spanning trees.
# Properties of MST
# 1. MST contains exactly V – 1 edges (where V is number of vertices).
# 2. The MST is not unique if multiple edges have the same weight.
# 3. Every connected, weighted, undirected graph has at least one MST.
# 4. MST is useful for problems involving network design (roads, cables, pipelines, etc.).
# Applications of MST
# ● Designing least-cost communication networks (telephone, internet).
# ● Connecting cities with minimum cost roads.
# ● Reducing circuit wiring cost in VLSI design.
# ● Cluster analysis in Machine Learning (Kruskal’s MST-based clustering).
# MST Algorithms
# A. Kruskal’s Algorithm
# ● Approach: Greedy (sort edges by weight, add smallest edge if it doesn’t form a cycle).
# ● Steps:
# 1. Sort all edges by weight (ascending).
# 2. Pick smallest edge that doesn’t form a cycle (use Disjoint Set Union / Union-Find).
# 3. Repeat until you have V – 1 edges.
# ● Complexity: O(E log E) (E = number of edges).

# B. Prim’s Algorithm
# ● Approach: Greedy (grow MST from a starting vertex).
# ● Steps:
# ○ Start from any vertex.
# ○ At each step, choose the smallest edge connecting a vertex inside MST to a vertex outside
# MST.
# ○ Repeat until all vertices are included.
# ● Complexity:
# ○ With adjacency matrix: O(V^2)
# ○ With min-heap & adjacency list: O(E log V)
# Example
# Graph:
# Vertices: {A, B, C, D}
# Edges:
# A-B (1), A-C (3), B-C (2), B-D (4), C-D (5)
# MST using Kruskal:
# 1. Sort edges: (A-B:1), (B-C:2), (A-C:3), (B-D:4), (C-D:5)
# 2. Pick A-B (1)
# 3. Pick B-C (2)
# 4. Pick B-D (4)
# MST Edges = {A-B, B-C, B-D}, Cost = 7

# Comparison of Kruskal vs Prim
# Feature Kruskal’s Algorithm Prim’s Algorithm
# Approach Works on edges Works on vertices
# Data Structure Disjoint Set (Union-Find) Priority Queue / MinHeap
# Best for Sparse graphs Dense graphs
# Complexity O(E log E) O(E log V)
# Nature Global greedy Local greedy
# Approach Edge-based Node-based
# Suitable Sparse graphs Dense graphs
# Cycle check Needed Not needed
# Implementation Sort edges Min-heap or adjacency
#  NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 7 Asst.Prof.Salunkhe A.A
# Observation / Result
# ● Both Kruskal’s and Prim’s algorithms produce MST with minimum total weight.
# ● Kruskal’s works edge-based; Prim’s works node-based.
# ● MST ensures all departments are connected with minimum total distance.
# Conclusion
# ● Implemented MST for college campus graph successfully.
# ● Kruskal’s and Prim’s algorithms provide same total minimum weight.
# ● Students understand greedy approach, graph representation, and MST concepts.
# ● Useful for real-world applications like network design, road planning, and communication
# systems.



# Python Code
# # Python program for MST of college campus graph using Kruskal & Prim
# # Nodes represent departments (0: CSE, 1: IT, 2: E&TC, 3: MECH, 4: CIVIL)
# # ---------------------- Kruskal's Algorithm ----------------------
# class DisjointSet:
#  def __init__(self, n):
#  self.parent = list(range(n))

#  def find(self, u):
#  if self.parent[u] != u:
#  self.parent[u] = self.find(self.parent[u])
#  return self.parent[u]
#  def union(self, u, v):
#  pu, pv = self.find(u), self.find(v)
#  if pu != pv:
#  self.parent[pu] = pv
# def kruskal(n, edges):
#  edges.sort(key=lambda x: x[2]) # sort by weight
#  ds = DisjointSet(n)
#  mst = []
#  total_weight = 0
#  for u, v, w in edges:
#  if ds.find(u) != ds.find(v):
#  ds.union(u, v)
#  mst.append((u, v, w))
#  total_weight += w
#  return mst, total_weight
# # ---------------------- Prim's Algorithm ----------------------
# import heapq
# def prim(n, adj):
#  visited = [False] * n
#  min_heap = [(0, 0, -1)] # (weight, node, parent)
#  mst = []
#  total_weight = 0
#  while min_heap:
#  w, u, parent = heapq.heappop(min_heap)
#  if visited[u]:
#  continue
#  NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 9 Asst.Prof.Salunkhe A.A
#  visited[u] = True
#  if parent != -1:
#  mst.append((parent, u, w))
#  total_weight += w
#  for v, weight in adj[u]:
#  if not visited[v]:
#  heapq.heappush(min_heap, (weight, v, u))
#  return mst, total_weight
# # ---------------------- Main Code ----------------------
# departments = ["CSE", "IT", "E&TC", "MECH", "CIVIL"]
# n = len(departments)
# # Edges (u, v, weight) - distances between departments
# edges = [
#  (0, 1, 2), (0, 2, 3), (1, 2, 1),
#  (1, 3, 4), (2, 3, 5), (3, 4, 7), (2, 4, 6)
# ]
# # Adjacency list for Prim's
# adj = [[] for _ in range(n)]
# for u, v, w in edges:
#  adj[u].append((v, w))
#  adj[v].append((u, w))
# # Kruskal's MST
# mst_kruskal, total_kruskal = kruskal(n, edges)
# print("Kruskal's MST:")
# for u, v, w in mst_kruskal:
#  print(f"{departments[u]} - {departments[v]} : {w}")
# print("Total weight:", total_kruskal)
# # Prim's MST
# mst_prim, total_prim = prim(n, adj)
# print("\nPrim's MST:")
# for u, v, w in mst_prim:
#  print(f"{departments[u]} - {departments[v]} : {w}")
# print("Total weight:", total_prim)
#  NAVSAHYADRI EDUCATION SOCIETY’S, GROUP OF INSTITUTIONS
#  Savitribai Phule Pune University
# Second Year of Artificial Intelligence and Machine Learning (2024 Course)
# Course Code: PCC-204-AIM Course Name: Data Structures & Algorithms Lab
# 10 Asst.Prof.Salunkhe A.A
# Output
# Kruskal's MST:
# IT - E&TC : 1
# CSE - IT : 2
# CSE - E&TC : 3
# MECH - CIVIL : 7
# Total weight: 13
# Prim's MST:
# CSE - IT : 2
# IT - E&TC : 1
# CSE - E&TC : 3
# MECH - CIVIL : 7
# Total weight: 13