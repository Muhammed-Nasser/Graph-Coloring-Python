# Python3 program to check if a connected
# graph is bipartite or not using DFS
  
# Function to store the connected nodes
def addEdge(adj, u, v):
 
    adj[u].append(v)
    adj[v].append(u)
 
# Function to check whether a graph is
# bipartite or not
def isBipartite(adj, v, visited, color):
 
    for u in adj[v]:
  
        # If vertex u is not explored before
        if (visited[u] == False):
  
            # Mark present vertic as visited
            visited[u] = True
  
            # Mark its color opposite to its parent
            color[u] = not color[v]
  
            # If the subtree rooted at vertex v
            # is not bipartite
            if (not isBipartite(adj, u,
                                visited, color)):
                return False
                 
        # If two adjacent are colored with
        # same color then the graph is not
        # bipartite
        elif (color[u] == color[v]):
            return False
     
    return True

# Driver Code
if __name__=='__main__':
 
    # No of nodes
    N = 6
  
    # To maintain the adjacency list of graph
    adj = [[] for i in range(N + 1)]
  
    # To keep a check on whether
    # a node is discovered or not
    visited = [0 for i in range(N + 1)]
  
    # To color the vertices
    # of graph with 2 color
    color = [0 for i in range(N + 1)]
  
    # Adding edges to the graph
    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 6, 1)
    
  
    # Marking the source node as visited
    visited[1] = True
  
    # Marking the source node with a color
    color[1] = 0
  
    # Function to check if the graph
    # is Bipartite or not
    if (isBipartite(adj, 1, visited, color)):
        print("Graph is Bipartite")
    else:
        print("Graph is not Bipartite")
        
        
