class Solution:
    def longest_common_prefix(self, strs):
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or c != s[i]:
                    return s[:i]
        
        return strs[0]