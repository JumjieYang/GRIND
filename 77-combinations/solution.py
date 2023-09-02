class Solution:
    def combine(self, n, k):
        res = []
        
        def dfs(i, cur):
            if len(cur) == k:
                res.append(cur)
                return
            
            for j in range(i, n + 1):
                dfs(j + 1, cur + [j])
        
        dfs(1, [])
        
        return res