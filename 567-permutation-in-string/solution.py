class Solution:
    def check_inclusion(self, s1, s2):
        m, n = len(s1), len(s2)

        if m < n:
            return False

        window, formed = [0] * 26, [0] * 26

        a = ord('a')

        for c in s1:
            window[ord(c) - a] += 1

        for i in range(m):
            formed[ord(s2[i]) - a] += 1

        if formed == window:
            return True

        for i in range(m, n):
            formed[ord(s2[i]) - a] += 1
            formed[ord(s2[i - m]) - a] -= 1

            if formed == window:
                return True

        return False
