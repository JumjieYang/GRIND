class Solution:
    def generate_parenthesis(self, n):
        res = []

        def backtrack(l, r, cur):
            if l == r == 0:
                res.append(''.join(cur))
                return

            if l > r:
                return

            if l > 0:
                cur.append('(')
                backtrack(l - 1, r, cur)
                cur.pop()

            if r > l:
                cur.append(')')
                backtrack(l, r - 1, cur)
                cur.pop()

        backtrack(n, n, [])

        return res
