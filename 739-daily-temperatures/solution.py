class Solution:
    def daily_temperatures(self, temperatues):
        n = len(temperatues)

        res = [0] * n

        hottest = 0

        for i in range(n - 1, -1, -1):
            if hottest <= temperatues[i]:
                hottest = temperatues[i]
                continue

            days = 1

            while temperatues[i + days] <= temperatues[i]:
                days += res[i + days]

            res[i] = days

        return res
