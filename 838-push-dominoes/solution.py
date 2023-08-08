from collections import deque


class Solution:
    def push_dominoes(self, dominoes):
        dominoes = list(dominoes)

        q = deque()

        for i, d in enumerate(dominoes):

            if d != '.':
                q.append((i, d))

        while q:
            idx, node = q.popleft()

            if node == 'L' and idx > 0 and dominoes[idx - 1] == '.':
                dominoes[idx - 1] = 'L'
                q.append((idx - 1, 'L'))

            elif node == 'R' and idx < len(dominoes) - 1 and dominoes[idx + 1] == '.':
                if idx == len(dominoes) - 2 or dominoes[idx + 2] != 'L':
                    q.append((idx + 1, 'R'))
                    dominoes[idx + 1] = 'R'
                else:
                    q.popleft()

        return ''.join(dominoes)
