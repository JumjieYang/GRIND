from collections import Counter


class Solution:
    def count_palindromic_subsequence(self, s):
        res = set()
        left = set()

        right = Counter(s)

        for c in s:
            right[c] -= 1

            if right[c] == 0:
                right.pop(c)

            for l in left:
                if l in right:
                    res.add((c, l))

            left.add(c)

        return len(res)
