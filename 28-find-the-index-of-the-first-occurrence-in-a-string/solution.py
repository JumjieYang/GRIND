class Solution:
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)

        if m < n:
            return -1

        if n == 0:
            return 0

        lps = [0] * n

        prev_lps = 0
        i = 1

        while i < n:
            if needle[i] == needle[prev_lps]:
                prev_lps += 1

                lps[i] = prev_lps

                i += 1
            elif prev_lps == 0:
                lps[i] = 0

                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        i = j = 0

        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            if j == n:
                return i - n

        return -1
