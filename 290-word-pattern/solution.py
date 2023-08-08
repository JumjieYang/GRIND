class Solution:
    def word_pattern(self, pattern, s):
        s = s.split(' ')

        m, n = len(pattern), len(s)

        if m != n:
            return False

        mappingPS, mappingSP = {}, {}

        for i in range(n):
            pi = pattern[i]
            si = s[i]

            if (pi in mappingPS and mappingPS[pi] != si) or (si in mappingSP and mappingSP[si] != pi):
                return False

            mappingPS[pi] = si
            mappingSP[si] = pi

        return True
