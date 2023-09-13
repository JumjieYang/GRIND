from collections import defaultdict


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
    def number_of_good_paths(self, vals, edges):
        adj = defaultdict(list)
        
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        val_to_idx = defaultdict(list)
        
        for i, val in enumerate(vals):
            val_to_idx[val].append(i)
        
        uf = UF()
        
        res = 0
        
        for val in sorted(val_to_idx.keys()):
            for i in val_to_idx[val]:
                for neighbor in adj[i]:
                    if vals[neighbor] <= vals[i]:
                        uf.union(neighbor, i)
            
            counter = defaultdict(int)
            
            for i in val_to_idx[val]:
                counter[uf.find(i)] += 1
                res += counter[uf.find(i)]
        
        return res