class Solution:
    def permute_unique(self, nums):
        res = []
        counter = Counter(nums)
        
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur)
                return
            
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    
                    dfs(cur + [num])
                    
                    counter[num] += 1
        
        dfs([])
        
        return res