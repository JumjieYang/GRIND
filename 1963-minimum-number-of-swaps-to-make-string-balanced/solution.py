class Solution:
    def min_swaps(self, s):
        max_close = 0
        cur = 0

        for c in s:
            if c == ']':
                cur += 1
            else:
                cur -= 1

            max_close = max(max_close, cur)

        return (max_close + 1) // 2
