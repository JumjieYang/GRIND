class Solution:
    def has_all_codes(self, s, k):
        codes = set()

        for i in range(len(s) - k + 1):
            cur = s[i: i + k]

            codes.add(cur)

        return len(codes) == 2 ** k
