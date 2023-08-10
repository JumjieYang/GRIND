import math


class Solution:
    def max_profit(self, prices):
        res = 0
        min_price = math.inf

        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)

        return res
