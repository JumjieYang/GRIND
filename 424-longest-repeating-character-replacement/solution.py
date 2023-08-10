from collections import Counter


class Solution:
    def character_replacement(self, s, k):
        freqs = Counter()

        l = 0
        max_freq = 0

        res = 0
        for r in range(len(s)):
            freqs[s[r]] += 1

            max_freq = max(max_freq, freqs[s[r]])

            if r - l + 1 - max_freq > k:
                freqs[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
