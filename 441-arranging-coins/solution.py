class Solution:
    def arrange_coins(self, n):
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2

            count = mid * (mid + 1) // 2

            if count == n:
                return mid
            elif count < n:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1
