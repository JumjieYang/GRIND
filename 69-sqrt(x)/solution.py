class Solution:
    def my_sqrt(self, x):
        l, r = 1, x

        while l <= r:
            mid = (l + r) // 2

            res = mid ** 2

            if res == x:
                return mid

            elif res < x:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1
