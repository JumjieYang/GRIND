class UF:
    def __init__(self, n):
        self.n = n
        self.root = {}

    def find(self, x):
        y = self.root.get(x, x)

        if y != x:
            y = self.find(y)
            self.root[x] = y

        return y

    def union(self, x, y):
        r1, r2 = self.find(x), self.find(y)

        if r1 == r2:
            return 0

        self.root[r1] = r2

        self.n -= 1

        return 1

    def is_connected(self):
        return self.n == 1


class Solution:
    def max_num_edges_to_remove(self, n, edges):
        alice, bob = UF(n), UF(n)

        res = 0

        edges.sort(reversed=True)

        for t, u, v in edges:
            if t == 3:
                res += alice.union(u, v) | bob.union(u, v)
            elif t == 2:
                res += alice.union(u, v)
            else:
                res += bob.union(u, v)

        return len(edges) - res if alice.is_connected() and bob.is_connected() else -1
