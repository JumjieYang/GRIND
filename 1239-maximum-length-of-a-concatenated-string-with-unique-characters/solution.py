class Solution:
    def max_length(self, arr):
        unique = ['']
        
        res = 0
        
        for w in arr:
            for u in unique:
                local = w + u
                
                if len(local) != len(set(local)):
                    continue
                
                unique.append(local)
                
                res = max(res, len(local))
        
        return res