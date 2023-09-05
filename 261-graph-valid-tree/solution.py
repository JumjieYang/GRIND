class UF:
    def __init__(self):
        self.root = {}

    def find(self, x):
        y = self.root.get(x, x)

        if y != x:
            y = self.find(y)

            self.root[x] = y

        return y

    def union(self, x, y):
        self.root[self.find(x)] = self.find(y)
        

class Solution:
    def valid_tree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        uf = UF()
        
        for v1, v2 in edges:
            if uf.find(v1) == uf.find(v2):
                return False
            
            uf.union(v1, v2)
        
        return True