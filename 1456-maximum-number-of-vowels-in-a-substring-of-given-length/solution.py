class Solution:
    def max_vowels(self, s, k):
        vowels = ('a', 'e', 'i', 'o', 'u')

        l = 0

        res = cur = 0

        for r in range(len(s)):
            if s[r] in vowels:
                cur += 1

            if r - l + 1 > k:
                if s[l] in vowels:
                    cur -= 1

                l += 1

            res = max(res, cur)

        return res
