class Solution:
    def subsets_with_dup(self, nums):
        res = set()
        
        nums.sort()
        
        def dfs(i, cur):
            if i == len(nums):
                res.add(tuple(cur))
                return
        
            if tuple(cur) in res:
                return
        
            dfs(i + 1, cur + [nums[i]])
            dfs(i + 1, cur)
    
        dfs(0, [])
        
        return res