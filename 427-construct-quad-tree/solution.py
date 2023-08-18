class Node:
    def __init__(self, val, is_leaf, top_left, top_right, bottom_left, bottom_right):
        self.val = val
        self.is_leaf = is_leaf
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right


class Solution:
    def construct(self, grid):
        def dfs(n, r, c):
            all_same = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break

            if all_same:
                return Node(grid[r][c] == 1, True, None, None, None, None)

            n //= 2
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            return Node(grid[r][c] == 1, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(len(grid), 0, 0)
