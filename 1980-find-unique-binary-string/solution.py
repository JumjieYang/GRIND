class Solution:
    def find_different_binary_string(self, nums):
        nums = set(nums)
        
        def dfs(cur):
            if len(cur) == len(nums):
                if cur not in nums:
                    return cur
                
                return None
            
            add_1 = dfs(cur + '1')
            
            if add_1:
                return add_1
            
            add_0 = dfs(cur + '0')
            
            if add_0:
                return add_0
            
            return None
        
        return dfs('')