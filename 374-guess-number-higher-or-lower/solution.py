class Solution:
    def guess_number(self, n):
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == 1:
                l = mid + 1
            else:
                r = mid - 1
