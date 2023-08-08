class Solution:
    def max_product(self, s):
        pali = {}

        n = len(s)

        for mask in range(1, 1 << n):
            cur = []

            for i in range(n):
                if mask & (1 << i):
                    cur.append(s[i])

            if cur == cur[::-1]:
                pali[mask] = len(cur)

        res = 0

        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1] * pali[m2])

        return res
