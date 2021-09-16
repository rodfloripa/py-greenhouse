
import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

class Edge(object):
    """ An undirected, capacity limited edge. """
    def __init__(self):
        self.c1 = []
        self.c2 = []

    # Connects two nodes via the edge.
    def connect(self, in_node, out_node):
        self.c1.append(in_node.color)
        self.c2.append(out_node.color)
        

    # Returns the edge's internal constraints.
    def constraints(self):
        #return [cp.pos(self.c2[0] - self.c1[0]) >=1]
        return [cp.pos(self.c1[0] - self.c2[0]) >= 1]
    
class Node(object):
    """ A node with accumulation. """
    def __init__(self, number):
        self.number = number
        #self.color = cp.Variable(nonneg=True)
        #self.color = Z
        if number == max_neigb:
            self.color = 0
        else:
            self.color = cp.Variable(integer=True)

edges = [(1,0),(1,2),(1,3)]
#edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,5),(2,4),(2,6),(1,6),(4,6),(0,5)]
n_nodes = 4
#n_nodes = 7
nodes_lst = []
n_edges = 3
#n_edges = 12
edges_lst = []
max_neigb = []

for i in edges:
    max_neigb.append(i[0])
    max_neigb.append(i[1])
max_neigb = max(max_neigb,key=max_neigb.count)
for i in range(0,n_nodes):
    nodes_lst.append(Node(i))
for i in range(0,n_edges):
    edges_lst.append(Edge())    
for i in range(0,n_edges):
    edges_lst[i].connect(nodes_lst[edges[i][0]],nodes_lst[edges[i][1]])    

sum_ = []
for i in range(0,n_edges):
    sum_.append(edges_lst[i].c1[0])
    sum_.append(edges_lst[i].c2[0])

constraints = []
for obj in edges_lst:
    constraints += obj.constraints()
prob = cp.Problem(cp.Minimize(cp.sum(sum_)), constraints)

result = prob.solve(qcp=True)
print(result)