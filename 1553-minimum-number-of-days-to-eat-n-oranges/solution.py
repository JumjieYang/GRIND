class Solution:
    def min_days(self, n):
        dp = {0: 0, 1: 1}
        
        def dfs(n):
            if n in dp:
                return dp[n]
            
            two = n % 2 + dfs(n // 2)
            three = n % 3 + dfs(n // 3)
            
            dp[n] = min(two, three) + 1
            
            return dp[n]
        
        return dfs(n)