class Solution:
    def find_smallest_set_of_vertices(self, n, edges):
        degrees = [0] * n
        
        for _, b in edges:
            degrees[b] += 1
        
        res = []
        
        for i in range(n):
            if degrees[i] == 0:
                res.append(i)
        
        return res
        
        