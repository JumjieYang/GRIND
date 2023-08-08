import math


class Solution:
    def grid_game(self, grid):
        n = len(grid[0])

        prefix1 = list(grid[0])
        prefix2 = list(grid[1])

        for i in range(1, n):
            prefix1[i] += prefix1[i - 1]
            prefix2[i] += prefix2[i - 1]

        res = math.inf

        for i in range(n):
            go_right = prefix1[-1] - prefix1[i]
            go_bottom = prefix2[i - 1] if i > 0 else 0

            res = min(res, max(go_right, go_bottom))

        return res
