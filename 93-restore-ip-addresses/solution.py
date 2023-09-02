class Solution:
    def restore_ip_addresses(self, s):
        n = len(s)
        
        if n > 12:
            return []
        
        res = []
        
        def dfs(i, dot, cur):
            if i == n and dot == 4:
                res.append(cur[:-1])
                return
            
            if dot > 4:
                return
            
            for j in range(i, min(i + 3, n)):
                if int(s[i: j + 1]) < 256 and (j == i or s[i] != '0'):
                    dfs(j + 1, dot + 1, cur + s[i: j + 1] + '.')
        
        dfs(0, 0, '')
        
        return res