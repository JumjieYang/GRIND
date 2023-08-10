class Solution:
    def successful_pairs(self, spells, potions, success):
        potions.sort()

        n = len(potions)

        res = []

        for s in spells:
            idx = n

            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2

                if s * potions[mid] >= success:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1

            res.append(n - idx)

        return res
