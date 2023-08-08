from collections import Counter


class Solution:
    def interchangeable_rectangles(self, rectangles):
        counter = Counter()

        for w, h in rectangles:
            counter[w / h] += 1

        res = 0

        for val in counter.values():
            res += (val * (val - 1)) // 2

        return res
