from collections import Counter


class Solution:
    def total_fruit(self, fruits):
        freqs = Counter()

        l = 0
        res = 0
        count = 0
        for r in range(len(fruits)):
            freqs[fruits[r]] += 1

            count += 1
            while len(freqs) > 2:
                f = fruits[l]

                freqs[f] -= 1
                count -= 1

                if freqs[f] == 0:
                    freqs.pop(f)

            res = max(res, count)

        return res
