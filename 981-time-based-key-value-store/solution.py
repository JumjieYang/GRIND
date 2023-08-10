from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key, value, timestamp):
        self.dict[key].append((timestamp, value))

    def get(self, key, timestamp):
        vals = self.dict[key]

        l, r = 0, len(vals) - 1

        res = -1

        while l <= r:
            mid = (l + r) // 2

            if vals[mid][0] <= timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return '' if res == -1 else vals[res][1]
