class Solution:
    def find_anagrams(self, s, p):
        m, n = len(s), len(p)

        if m < n:
            return []

        res = []

        window, formed = [0] * 26, [0] * 26

        a = ord('a')
        for c in p:
            window[ord(c) - a] += 1

        for i in range(n):
            formed[ord(s[i]) - a] += 1

        if window == formed:
            res.append(0)

        for i in range(n, m):
            formed[ord(s[i]) - a] += 1
            formed[ord(s[i - n]) - a] -= 1

            if window == formed:
                res.append(i - n + 1)

        return res
