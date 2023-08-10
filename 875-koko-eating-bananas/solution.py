import math


class Solution:
    def min_eating_speed(self, piles, h):
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2

            time_needed = 0

            for p in piles:
                time_needed += math.ceil(p / mid)

            if time_needed <= h:
                r = mid - 1
            else:
                l = mid + 1

        return r + 1
