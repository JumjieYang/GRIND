class Solution:
    def letter_combinations(self, digits):
        if len(digits) == 0:
            return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        res = []
        
        def dfs(i, cur):
            if i == len(digits):
                res.append(''.join(cur))
                return
            
            for char in digit_map[digits[i]]:
                dfs(i + 1, cur + [char])
        
        dfs(0, [])
        
        return res