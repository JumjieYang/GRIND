class Solution:
    def combination_sum_2(self, candidates, target):
        candidates.sort()
        res = []
        
        def dfs(i, cur, rem):
            if rem == 0:
                res.append(cur)
                return
        
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                num = candidates[j]
                
                if num > rem:
                    return
            
                dfs(j + 1, cur + [num], rem - num)
        
        dfs(0, [], target)
        
        return res