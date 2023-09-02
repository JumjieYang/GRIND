class Solution:
    def total_n_queens(self, n):
        diags = set()
        anti_diags = set()
        cols = set()

        state = [['.' for _ in range(n)] for _ in range(n)]

        res = 0

        def dfs(r):

            if r == n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                diag = r - c
                anti_diag = r + c

                if diag in diags or anti_diag in anti_diags or c in cols:
                    continue

                state[r][c] = 'Q'
                diags.add(diag)
                anti_diags.add(anti_diag)
                cols.add(c)

                dfs(r + 1)

                state[r][c] = '.'
                diags.remove(diag)
                anti_diags.remove(anti_diag)
                cols.remove(c)

        dfs(0)

        return res