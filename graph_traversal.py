import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

i = np.inf
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

#queue using singly linked list
class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)
        if(self.front == None):
            self.front = new_node
            self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if(self.front == None):
            return -1
        front = self.front
        self.front = front.next
        front.next = None
        if self.front == None:
            self.rear == None
        return front.data


class Graph:
    def __init__(self,matrix):
        self.mat = matrix
    
    def bfs(self, start):
        #nx.Digraph is used to visualize the graph using nx.draw
        G = nx.DiGraph()
        for v in range(len(self.mat)):
            for j in range(len(self.mat)):
                if(self.mat[v][j] != i and self.mat[v][j] != 0):
                    G.add_edge(v, j)
        pos = nx.spring_layout(G) 


        q = queue()
        visited = [False for k in range(len(self.mat))]
        q.enqueue(start)
        visited[start] = True
        traversal = []
        count = 0
        print("BFS:",end=" ")
        while count < len(self.mat):
            cur = q.dequeue()
            print(cur,end=" ")
            traversal.append(cur)
            count = count + 1

            plt.clf()
            plt.title("BFS TRAVERSAL")
            nx.draw(G, pos, with_labels=True, node_color=["yellow" if n in traversal else "lightblue" for n in G.nodes])
            plt.pause(2) 

            for v in range(len(self.mat[cur])):
                if(self.mat[cur][v] != i and self.mat[cur][v] !=0):
                    if visited[v] == False:
                        q.enqueue(v)
                        visited[v] = True
        print("")

    def dfsRec(self,start):
        #nx.Digraph is used to visualize the graph using nx.draw
        G = nx.DiGraph()
        for v in range(len(self.mat)):
            for j in range(len(self.mat)):
                if(self.mat[v][j] != i and self.mat[v][j] != 0):
                    G.add_edge(v, j)
        pos = nx.spring_layout(G) 
        print("dfs:",end=" ")
        def df(vertex,visited,traversal):
            print(vertex,end=" ")
            visited[vertex] = True
            traversal.append(vertex)
            

            plt.clf()
            plt.title("DFS TRAVERSAL")
            nx.draw(G, pos, with_labels=True, node_color=["yellow" if n in traversal else "lightblue" for n in G.nodes])
            plt.pause(2) 
            for v in range(len(self.mat[vertex])):
                if(self.mat[vertex][v]!= 0 and self.mat[vertex][v]!= i):
                    if(visited[v] == False):
                        df(v,visited,traversal)
        visited = [False for k in range(len(self.mat))]
        df(start,visited,[])
        print("")


    def display(self): #visualizing graph
        G = nx.DiGraph()
        for v in range(len(self.mat)):
            for j in range(len(self.mat)):
                if(self.mat[v][j] != i and self.mat[v][j] != 0):
                    G.add_edge(v, j,weight=self.mat[v][j])
        
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=700)
        plt.title("Graph Visualization")
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
        
        
        plt.show()



n = 5 #number of Nodes

adj = [[0,5,i,i,i,3],
       [i,0,2,1,i,i],
       [i,i,0,i,1,i],
       [i,i,1,0,2,i],
       [i,i,i,i,0,i],
       [i,i,2,5,i,0]]

g = Graph(adj)


#call the functions with start vertex as arguments
g.bfs(0)
g.dfsRec(0)

g.display() #visualize graph with a plot