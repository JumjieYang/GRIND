class Solution:
    def is_subsequence(self, s, t):
        m, n = len(s), len(t)

        if m == 0:
            return True

        if m > n:
            return False

        i = j = 0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if i == m:
                return True

        return False
