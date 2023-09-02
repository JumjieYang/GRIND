class Solution:
    def makesquare(self, matchsticks):
        sums = sum(matchsticks)
        
        if sums % 4 != 0:
            return False
    
        target = sums // 4
        
        matchsticks.sort(reverse=True)
        
        used = [False] * len(matchsticks)
        
        def dfs(i, k, cur_sums):
            if k == 0:
                return True
            
            if cur_sums == target:
                return dfs(0, k - 1, 0)
            
            for j in range(i, len(matchsticks)):
                if j > 0 and not used[j - 1] and matchsticks[j] == matchsticks[j - 1]:
                    continue
                
                if used[j] or cur_sums + matchsticks[j] > target:
                    continue
                
                used[j] = True
                
                if dfs(j + 1, k, cur_sums + matchsticks[j]):
                    return True
                
                used[j] = False
            
            return False
        
        return dfs(0, 4, 0)