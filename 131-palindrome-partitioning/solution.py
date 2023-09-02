class Solution:
    def partition(self, s):
        dp = [[] for _ in range(len(s)) + 1]
        dp[0] = [[]]
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                cur = s[j: i]
                
                if cur == cur[::-1]:
                    for comb in dp[j]:
                        dp[i].append(comb + [cur])
        
        return dp[-1]