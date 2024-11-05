import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
i = np.inf

class Graph:
    def __init__(self,matrix):
        self.mat = matrix  #adjacency Matrix
        
        
    #to get the shortest path Node from source Node at that instance
    def minDist(self,msset): 
        m = i

        for v in msset:
            for av in range(len(self.mat)):
                if self.mat[v][av] !=0 and self.mat[v][av] !=i:
                    if av not in msset:
                        if self.mat[v][av] < m:
                            m = self.mat[v][av]
                            mv = av
                            vv = v
        return mv,vv

    
    
        
    def PrimsMST(self, start):
        n = range(len(self.mat))
        mst = [[0 if k == j else i for k in n] for j in n]
        msset = [start] 
        count = 1  
            
        while count < len(self.mat):
            m, v = self.minDist(msset)  
            
            msset.append(m)
            mst[v][m] = self.mat[v][m]
            mst[m][v] = self.mat[v][m]  
            count += 1
    
        return mst
    
    def find_parent(self, parent, j):  
        if parent[j] == j:  
            return j  
        return self.find_parent(parent, parent[j])  
  
    def union(self, parent, rank, x, y):  
        root_x = self.find_parent(parent, x)  
        root_y = self.find_parent(parent, y)  
        if rank[root_x] < rank[root_y]:  
            parent[root_x] = root_y  
        elif rank[root_x] > rank[root_y]:  
            parent[root_y] = root_x  
        else:  
            parent[root_y] = root_x  
            rank[root_x] += 1  
  
    def kruskal(self):  
        n = len(self.mat)
        mst_matrix = [[i if u != v else 0 for v in range(n)] for u in range(n)]  # Initialize MST matrix with np.inf

        parent = {}
        rank = {}
        vertices = list(range(n))

        for v in vertices:  
            parent[v] = v  
            rank[v] = 0  

        edges = []
        for j in range(n):
            for k in range(j + 1, n):  # Only consider upper triangle for undirected graph
                if self.mat[j][k] != np.inf:  # Only include actual edges
                    edges.append((j, k, self.mat[j][k]))

        sorted_edges = sorted(edges, key=lambda x: x[2])  

        for edge in sorted_edges:  
            u, v, weight = edge  
            root_u = self.find_parent(parent, u)  
            root_v = self.find_parent(parent, v)  
            if root_u != root_v:  
                mst_matrix[u][v] = weight  # Add edge to MST matrix
                mst_matrix[v][u] = weight  # Add symmetric edge
                self.union(parent, rank, root_u, root_v)  
        
        return mst_matrix


    def displayMST(self, mst_matrix):
        G = nx.Graph()
        n = len(mst_matrix)
        
        for u in range(n):
            for v in range(u + 1, n):
                if mst_matrix[u][v] != 0 and mst_matrix[u][v] != i:
                    G.add_edge(u, v, weight=mst_matrix[u][v])
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        
        nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_size=14, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
        plt.show()

    def display(self): #visualizing graph
        G = nx.Graph()
        for v in range(len(self.mat)):
            for j in range(len(self.mat)):
                if(self.mat[v][j] != i and self.mat[v][j] != 0):
                    G.add_edge(v, j,weight=self.mat[v][j])
        
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
        
        plt.title("Graph Visualization")
        plt.show()

adj = [
    [0, 5, i, i, i, 3],
    [5, 0, 2, 1, i, i],
    [i, 2, 0, 1, 1, 2],
    [i, 1, 1, 0, 2, 5],
    [i, i, 1, 2, 0, i],
    [3, i, 2, 5, i, 0]
]

g = Graph(adj)

#these two functions returns a matrix form minimum spanning tree
p = g.PrimsMST(0) 
kr = g.kruskal()

#close each plot window to open next plot

g.displayMST(p)

g.displayMST(kr)

g.display()

