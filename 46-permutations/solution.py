class Solution:
    def permute(self, nums):
        res = []
        
        visited = set()
        
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur)
                return
        
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    
                    dfs(cur + [num])
                    visited.remove(num)
        
        dfs([])
        
        return res