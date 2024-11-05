import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

i = np.inf  #infinity

class Graph:
    def __init__(self,matrix):
        self.mat = matrix  #adjacency Matrix
        
    #to get the shortest path Node from source Node at that instance
    def minDist(self,arr,d): 
        m = arr[0]
        for j in arr:
            if(d[j] < d[m]):
                m = j
        return m
    
    #dijkstra's algorithm
    def dijkstra(self,source): 
        n =len(self.mat[0])
        d = {}
        for node in range(0,n): 
            d[node] = self.mat[source][node]
        
        unvisited=[] #list of unvisited
        for node in range(0,n):
            if node != source: #adding all the nodes except source node as unvisited
                unvisited.append(node)
        while(len(unvisited) > 0):
            u = self.minDist(unvisited,d)
            unvisited.remove(u)
            for node in unvisited:
                # to check whether the path through current node is shorter than previous path
                if(d[node] > d[u] + self.mat[u][node]):
                    d[node] = d[u] + self.mat[u][node]
        print(d)
        return d
    
    def dynamic_programming(self,destination): 
        n =len(self.mat[0])
        d = {}
        for node in range(0,n): 
            d[node] = self.mat[node][destination]
        
        unvisited=[] #list of unvisited
        for v in range(0,n):
            if node != destination: #adding all the nodes except source node as unvisited
                unvisited.append(node)
        while(len(unvisited) > 0):
            u = self.minDist(unvisited,d)
            unvisited.remove(u)
            for v in unvisited:
                # to check whether the path through current node is shorter than previous path
                if(d[v] > d[u] + self.mat[v][u]):
                    d[v] = d[u] + self.mat[v][u]
        print(d)
        return d

    #floyd
    def floyd(self):
        dist = self.mat
        n = range(len(self.mat))
        for k in n:
            for l in n:
                for j in n:
                    dist[l][j] = min(dist[l][j],dist[l][k] + dist[k][j])
        #displaying distance matrix
        print(end="\t")
        for j in range(len(self.mat)):
            print(j,end="\t")
        print("")
        print("_________________________________________________________")
        for k in range(len(dist)):
            print(k,"|",end="\t")
            for j in dist[k]:
                print(j,end="\t")
            print("")
        return dist
    
    def display(self): #visualizing graph
        G = nx.DiGraph()
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

adj = [[0,5,i,i,i,3],
       [i,0,2,1,i,i],
       [i,i,0,i,1,i],
       [i,i,1,0,2,i],
       [i,i,i,i,0,i],
       [i,i,2,5,i,0]]

g = Graph(adj) #graph is initialized as adjacency matrix
print("\n\n")

source_vertex = 0 #give your source vertex
print(f"dijkstra with start vertex {source_vertex}:",end=" ")
dij = g.dijkstra(source_vertex)

print("\n\n\n\n")

print("floyd's algorithm output:\n")
floy = g.floyd()

print("\n\n\n\n\n\n")


destination_vertex = 4 #give your destination vertex
print(f"dijkstra with start vertex {destination_vertex}:",end=" ")
dyn = g.dynamic_programming(destination_vertex)


print("\n\n\n\n")

g.display()


