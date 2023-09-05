class Node:
    def __init__(self, val, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def clone_graph(self, node):
        copy = {}
        
        def dfs(node):
            if not node:
                return
            
            if node in copy:
                return copy[node]
            
            copy[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                copy[node].neighbors.append(dfs(neighbor))
            
            return copy[node]
    
        return dfs(node)