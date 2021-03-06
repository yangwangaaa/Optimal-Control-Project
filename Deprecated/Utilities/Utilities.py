import heapq
import copy
# There is no expectation this code will be fast, rather the objective is to
# be methodical in the problem setup and consider optimization later
import numpy as np
# A node in an unstructured grid,
class Node:
    def __init__(self, neighbors, position):
        self.X = position
        self.N = neighbors
        self.u = 10**9
    def __lt__(self, other):
        return(self.u < other.u)
    def __eq__(self, other):
        return(self.u == other.u)
    def __gt__(self, other):
        return(self.u > other.u)
# A min max cost problem on a grid with running cost `Cost`
class LeastCost:
    def __init__(self, Cost, Base_Node, Nodes= None):
        self.Exit = Base_Node
        self.Exit.u = 0
        self.Frontier = copy.copy(self.Exit.N)
        heapq.heapify(self.Frontier)
        self.K  = Cost
        self.positions = []
        self.costs = []
        for node in self.Frontier:
            node.u = max(self.Exit.u, self.K(node.X))
    def Find_Values(self, Nodes):
        loops = 0
        while(len(self.Frontier) != 0):
            current_node = heapq.heappop(self.Frontier)
            self.positions.append(current_node.X)
            self.costs.append(current_node.u)
            #print([node.u for node in self.Frontier])
            for neighbor in current_node.N:
                print (neighbor.u, current_node.u)
                if neighbor.u > current_node.u:
                    print(Nodes.index(neighbor))
                    neighbor.u = max(current_node.u, self.K(neighbor.X))
                    if not (neighbor in self.Frontier):
                        heapq.heappush(self.Frontier, neighbor)
        return np.array(self.positions), np.array(self.costs)


# Given an adjacency matrix, create a graph and return a node of the graph
def Graph_from_Adjacency(Adj, Pos):
    Nodes = []
    length =  Adj.shape[0]
    #print(length)
    for i in range(length):
        Nodes.append(Node([],Pos[:,i]))
    for i in range(length):
        Nodes[i].N =  np.array(Nodes).\
            take(np.nonzero(np.arange(length)*Adj[i,:])).tolist()[0]
        #print(np.nonzero(np.arange(length)*Adj[i,:]))
        #print(Nodes[i].N)
    return Nodes
