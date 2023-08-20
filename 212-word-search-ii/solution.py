class Solution:
    def find_words(self, board, words):
        root = {}

        for word in words:
            cur = root

            for c in word:
                cur = cur.setdefault(c, {})

            cur['$'] = word

        m, n = len(board), len(board[0])

        res = []

        def backtrack(r, c, parent):
            char = board[r][c]

            board[r][c] = '.'

            cur = parent[char]

            if '$' in cur:
                res.append(cur['$'])
                cur.pop('$')

            for i, j in (1, 0), (0, 1), (-1, 0), (0, -1):
                dx, dy = r + i, c + j

                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] in cur:
                    backtrack(dx, dy, cur)

            if not cur:
                parent.pop(char)

            board[r][c] = char

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    backtrack(i, j, root)

        return res
