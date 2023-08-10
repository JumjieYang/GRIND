class Solution:
    def ship_within_days(self, weights, days):
        def feasible(cap):
            num_days = 1
            cur_cap = cap

            for w in weights:
                if cur_cap < w:
                    num_days += 1
                    cur_cap = cap
                cur_cap -= w

            return num_days <= days

        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2

            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1

        return r + 1
