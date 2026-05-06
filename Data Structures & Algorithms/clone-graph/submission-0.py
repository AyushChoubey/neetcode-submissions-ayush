"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        def dfs(node):
            if node in self.visited:
                   return self.visited[node]
            
            new_node = Node(node.val)
            self.visited[node] = new_node
            
            

            for n in node.neighbors:
                
                
                # if n not in visited:
                    # visited.append(n)
                    
                    new_node.neighbors.append(dfs(n))
            return new_node
        self.visited = {}    
        if node:     
            return dfs(node)
        else:
            return node
        





        
        