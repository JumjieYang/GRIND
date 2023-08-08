from collections import Counter


class Solution:
    def least_bricks(self, wall):
        freqs = Counter()
        freqs[0] = 0
        for row in wall:
            cur = 0

            for i in row[:-1]:
                cur += i
                freqs[cur] += 1

        return len(wall) - max(freqs.values())
