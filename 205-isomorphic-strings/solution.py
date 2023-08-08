class Solution:
    def is_isomorphic(self, s, t):
        m, n = len(s), len(t)

        if m != n:
            return False

        mappingST, mappingTS = {}, {}

        for i in range(m):
            if (s[i] in mappingST and mappingST[s[i]] != t[i]) or (t[i] in mappingTS and mappingTS[t[i]] != s[i]):
                return False

            mappingST[s[i]] = t[i]
            mappingTS[t[i]] = s[i]

        return True
