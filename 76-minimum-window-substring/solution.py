import math
from collections import Counter


class Solution:
    def min_window(self, s, t):
        m, n = len(s), len(t)

        if m < n:
            return ''

        formed, window = Counter(), Counter(t)

        len_s, len_t = 0, len(window)

        l = 0

        res = (math.inf, None, None)
        for r in range(m):
            formed[s[r]] += 1

            if s[r] in window and formed[s[r]] == window[s[r]]:
                len_s += 1

            while l <= r and len_s == len_t:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r + 1)

                formed[s[l]] -= 1

                if s[l] in window and window[s[l]] > formed[s[l]]:
                    len_s -= 1

                l += 1

        return '' if res[0] == math.inf else s[res[1]: res[2]]
