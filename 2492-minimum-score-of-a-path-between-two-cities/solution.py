import math


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
    def min_score(self, n, roads):
        uf = UF()
        
        res = math.inf
        
        for a, b, _ in roads:
            uf.union(a, b)
        
        for a, _, dist in roads:
            if uf.find(1) == uf.find(a):
                res = min(res, dist)
        
        return res
                