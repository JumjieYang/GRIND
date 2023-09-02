class Solution:
    def subsets(self, nums):
        res = []
        
        def dfs(i, cur):
            if i == len(nums):
                res.append(cur)
                return
            
            dfs(i + 1, cur)
            dfs(i + 1, cur + [nums[i]])
        
        dfs(0, [])
        
        return res