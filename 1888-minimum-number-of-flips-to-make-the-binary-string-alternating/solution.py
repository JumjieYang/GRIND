class Solution:
    def min_flips(self, s):
        n = len(s)

        s += s

        alt1 = ''
        alt2 = ''

        for i in range(2 * n):
            alt1 += '1' if i % 2 else '0'
            alt2 += '0' if i % 2 else '1'

        res = n

        diff1 = diff2 = 0

        l = 0
        for r in range(2 * n):
            diff1 += 1 if s[r] != alt1[r] else 0
            diff2 += 1 if s[r] != alt2[r] else 0

            if r - l + 1 > n:
                diff1 -= 1 if s[l] != alt1[l] else 0
                diff2 -= 1 if s[l] != alt2[l] else 0

                l += 1

            if r - l + 1 == n:
                res = min(res, diff1, diff2)

        return res
