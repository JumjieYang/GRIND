class Solution:
    def partion_string(self, s):
        res = 1

        visited = set()

        for c in s:
            if c in visited:
                res += 1
                visited = set()

            visited.add(c)

        return res
